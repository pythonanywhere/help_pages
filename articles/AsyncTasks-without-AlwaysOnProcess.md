I have an app hosted on PythonAnywhere which has a handful of functions which do some lengthy SQL queries.  I'm using the Django framework.  My system, called WICS (Warehouse Inventory Control System), schedules and records physical inventories and facilitates comparison with SAP, which is the Source Of All Truth in my company.  SAP stock-on-hand is exported through MB52 to a spreadsheet daily and imported into WICS.  The Master Material List is exported from MM60 to a spreadsheet and used to update the WICS Material List once a month or so.  Both of these processes involve queries that take a while to run, and the Material List update routinely takes long enough that my PA delivers a 504 (timeout) response.

While learning how to offload these lengthy queries to an async process, I searched for examples to guide me.  Unfortunately, most async examples available focus on automating a recurring process, usually sending an email.  While these examples were of some help, they left a lot of unanswered questions.
I’m sure I’m not the first person with my use case, nor will I be the last.  So here’s what I came up with, an example for the next sucker who has to figure out how to do this.  I’m going to concentrate on the Material List update here, since that is the more complex of the functions that needed to go async.

Since I was going to offload the Material List update to an async process, I figured I’d also devise a scheme to update the web page client with the progress of the backend.  More on that shortly.

Before this reworking, when the user asked to Update the Material List, a view called fnUpdateMatListfromSAP was run.  It still is, but now instead of doing the entire update by itself, it offloads its work to an asynchronous co-routine.  The fnUpdateMatListfromSAP view and its supporting functions are all below.  The template/HTML which sent the request (frmUpdateMatlListfromSAP_phase0.html) also had to undergo a few changes, primarily the addition of javascript which sends an ajax request (to fnUpdateMatlListfromSAP), then periodically listens for status updates from the server.

Before getting into my implementation of the Material List update, let me say a little about what I rejected and why.  

When I first determined I needed to have Update Material List async, I said ‘async’, and the entire programming community responded ‘task queue and brokers’.  At first I rejected this, because I wanted to depend on as few packages as possible. 

So I looked at handling the async programming “directly” using async def/asyncio/await/etc.  I finally rejected that because there was going to be way too much I had to implement, and PythonAnywhere is WSGI-only, not ASGI.  I saw a few blurbs about running async code in a WSGI environment, and the performance hits may be negligible, but for me, the learning curve was too steep and the work was more than I wanted to put in at this point. Looking at the work involved did have an upside, though: I better understood the idea of task queue and brokers.  If I had done the async work in Python-only, I basically would have had to write a task queue and a broker, and what I would have developed would have been so dependent on each other and specific to this project that I would have had to totally rewrite it in another project, or if this one changed (WHEN this one changes!).  PythonAnywhere’s WSGI-only server is also the reason I decided not to use any of Django’s async features, such as async views (which are just async functions anyhow)

So it was time to reconsider task queues and brokers.  The task queue was actually easy. Celery seems to be the dominant task queue out there, but Celery isn’t supported on PythonAnywhere.  The task queue PythonAnywhere supports and recommends is Django-q (they may support others, but the one mentioned in their help pages is django-q).  For the broker, django-q supports using the ORM itself as a broker.  The django-q docs caution that a more robust broker is appropriate for high-volume traffic, but WICS is not that.  The ORM is adequate for my needs, and should WICS grow, I can switch to another broker.

If you are where I was when I started this journey, you may need to have all this task queue and broker stuff explained.  This is how I understand it.  When your view wants a task done asynchronously, it sends the task to the task queue, and then moves on to return an HttpResponse to the HttpRequest-er (the web page that sent the request that triggered your view).  Depending on your needs, your view can schedule multiple async_tasks before returning a HttpResponse.  Basically, your view is no longer responsible for doing the async_task, but simply passing it off (to the task queue) to be done.  Running in the background is the broker, which picks up the async_task and places it in a Cluster.  The Cluster picks off the tasks and runs them.  This diagram, which seemed daunting at first, actually explains the process very well:
https://django-q.readthedocs.io/en/latest/architecture.html

One of the things that was giving me pause was running an always-on task for the cluster.  There are only two options in WICS which require asynchronous processing.  One of those (the more time-consuming one) is typically run monthly, the other daily.  The monthly process, slow as it is, typically completes in less than 15 (but far more than 3) minutes.  I balked at having a process running 24/7 for 30 days when it will really be used for 15 minutes.

I’m very satisfied with my solution. The initial call to fnUpdateMatListfromSAP starts a django-q process and holds on to the pid (process id).  While I’ve got it, I make the pid do double duty by being the key in my table which records and reports processing status.  When all processing is complete and the results are presented, the result HTML/Javascript does a final ajax call to do cleanup: kill the status record for this run, kill the django-q process and delete the temporary table used to present results.  This means my users cannot refresh the page containing the results, but that’s acceptable in my case.

=======

Later on I’ll explain the code below in some detail, but for now, I’ll simply present it with the hope that you will find either the code or the techniques useful.

Good luck!

    :::python
        #########################################################################
        ############################## procs_SAP.py #############################
        #########################################################################
        #########################################################################
    
        import os, uuid, re as regex
        import subprocess, signal
        import json
        from functools import partial
        from django.contrib.auth.decorators import login_required
        from django.db import connection, transaction
        from django.http import HttpResponse
        from django.shortcuts import render
        from django_q.tasks import async_task
        from openpyxl import load_workbook
        from cMenu.models import getcParm
        from cMenu.utils import ExcelWorkbook_fileext
        import WICS.globals
        from WICS.models import SAPPlants_org
        from WICS.models import WhsePartTypes, MaterialList, tmpMaterialListUpdate
        from WICS.models_async_comm import async_comm, set_async_comm_state
    
     
        ################################################################################
        ################################################################################
        ################################################################################
    
        ##### the suite of procs to support fnUpdateMatlListfromSAP
    
        def proc_MatlListSAPSprsheet_00InitUMLasync_comm(reqid):
            acomm = set_async_comm_state(
                reqid,
                statecode = 'rdng-sprsht-init',
                statetext = 'Initializing ...',
                new_async=True
                )
    
        def proc_MatlListSAPSprsheet_00CopyUMLSpreadsheet(req, reqid):
            acomm = set_async_comm_state(
                reqid,
                statecode = 'uploading-sprsht',
                statetext = 'Uploading Spreadsheet',
                )
    
            SAPFile = req.FILES['SAPFile']
            svdir = getcParm('SAP-FILELOC')
            fName = svdir+"tmpMatlList"+str(uuid.uuid4())+ExcelWorkbook_fileext
            with open(fName, "wb") as destination:
                for chunk in SAPFile.chunks():
                    destination.write(chunk)
        
            return fName
    
    def proc_MatlListSAPSprsheet_01ReadSpreadsheet(reqid, fName):
        acomm = set_async_comm_state(
            reqid,
            statecode = 'rdng-sprsht',
            statetext = 'Reading Spreadsheet',
            )
    
        # tmpMaterialListUpdate does multiple duty: it will store the MM60 spreadsheet, and it will identify 
        # what Material as found in WICS, what needs to be added, and what WICS material is no longer in SAP
        # tmpMaterialListUpdate is also used at the end to report results back to the user
        tmpMaterialListUpdate.objects.all().delete()
    
        SAP_SSName_TableName_map = {
                # dictionary mapping 'name of column in spreadsheet':'name of column in tmpMaterialListUpdate table'
                'Material': 'Material', 
                'Plant': 'Plant',
                # etc
                }
    
        wb = load_workbook(filename=fName, read_only=True)
        ws = wb.active
        SAPcol = {'Plant':None,'Material': None}
        SAPcolmnNames = ws[1]
        # after this loop, SAPcol['name of col in tmpMaterialListUpdate table'] = spreadsheet col# it's in 
        for col in SAPcolmnNames:
            if col.value in SAP_SSName_TableName_map:
                SAPcol[SAP_SSName_TableName_map[col.value]] = col.column - 1
        if (SAPcol['Material'] == None or SAPcol['Plant'] == None):
            set_async_comm_state(
                reqid,
                statecode = 'fatalerr',
                statetext = 'SAP Spreadsheet has bad header row. Plant and/or Material is missing.  See Calvin to fix this.',
                result = 'FAIL - bad spreadsheet',
                )
    
            wb.close()
            os.remove(fName)
            return
    
        numrows = ws.max_row
        nRows = 0
        for row in ws.iter_rows(min_row=2, values_only=True):
            nRows += 1
            if nRows % 100 == 0:
                set_async_comm_state(
                    reqid,
                    statecode = 'rdng-sprsht',
                    statetext = f'Reading Spreadsheet ... record {nRows} of {numrows}',
                    )
    
            # examine the row, adding it to tmpMaterialListUpdate, along with an error message if needed
            if row[SAPcol['Material']]==None: MatNum = ''
            else: MatNum = row[SAPcol['Material']]
            ## refuse to work with special chars embedded in the MatNum
            if regex.match(".*[\n\t\xA0].*",MatNum):
                tmpMaterialListUpdate(
                    recStatus = 'err-MatlNum',
                    errmsg = f'error: {MatNum!a} is an unusable part number. It contains invalid characters and cannot be added to WICS',
                    Material = row[SAPcol['Material']], 
                    # MaterialLink = MaterialLink,
                    Description = row[SAPcol['Description']], 
                    Plant = row[SAPcol['Plant']],
                    # etc
                    ).save()
                continue
            elif len(str(MatNum)):
                _org = SAPPlants_org.objects.filter(SAPPlant=row[SAPcol['Plant']])[0].org
                tmpMaterialListUpdate(
                    org = _org,
                    Material = row[SAPcol['Material']], 
                    # MaterialLink = MaterialLink,
                    Description = row[SAPcol['Description']], 
                    Plant = row[SAPcol['Plant']],
                    # etc
                    ).save()
            # endif invalid Material 
        # endfor
        wb.close()
        os.remove(fName)
    def done_MatlListSAPSprsheet_01ReadSpreadsheet(t):
        reqid = t.args[0]
        statecode = async_comm.objects.get(pk=reqid).statecode
        if statecode != 'fatalerr':
            set_async_comm_state(
                reqid,
                statecode = 'done-rdng-sprsht',
                statetext = f'Finished Reading Spreadsheet',
                )
            # this call is here because 02 CANNOT start before 01 is finished
            task02 = proc_MatlListSAPSprsheet_02_identifyexistingMaterial(reqid)
            done_MatlListSAPSprsheet_02_identifyexistingMaterial(reqid)
        #endif stateocde != 'fatalerr'
    
    def proc_MatlListSAPSprsheet_02_identifyexistingMaterial(reqid):
        set_async_comm_state(
            reqid,
            statecode = 'get-matl-link',
            statetext = f'Finding SAP MM60 Materials already in WICS Material List',
            )
        UpdMaterialLinkSQL = 'UPDATE WICS_tmpmateriallistupdate, (select id, org_id, Material from WICS_materiallist) as MasterMaterials'
        UpdMaterialLinkSQL += ' set WICS_tmpmateriallistupdate.MaterialLink_id = MasterMaterials.id, '
        UpdMaterialLinkSQL += "     WICS_tmpmateriallistupdate.recStatus = 'FOUND' "
        UpdMaterialLinkSQL += ' where WICS_tmpmateriallistupdate.org_id = MasterMaterials.org_id '
        UpdMaterialLinkSQL += '   and WICS_tmpmateriallistupdate.Material = MasterMaterials.Material '
        # tmpMaterialListUpdate.objects.all().update(MaterialLink=Subquery(MaterialList.objects.filter(org=OuterRef('org'), Material=OuterRef('Material'))[0]))
        with connection.cursor() as cursor:
            cursor.execute(UpdMaterialLinkSQL)
        set_async_comm_state(
            reqid,
            statecode = 'get-matl-link-done',
            statetext = f'Finished linking SAP MM60 list to existing WICS Materials',
            )
    def done_MatlListSAPSprsheet_02_identifyexistingMaterial(reqid):
        proc_MatlListSAPSprsheet_03_Remove(reqid)
        proc_MatlListSAPSprsheet_04_Add(reqid)
    
    def proc_MatlListSAPSprsheet_03_Remove(reqid):
        set_async_comm_state(
            reqid,
            statecode = 'id-del-matl',
            statetext = f'Identifying WICS Materials no longer in SAP MM60 Materials',
            )
        MustKeepMatlsCond = []
        MustKeepMatlsCond.append(('.SEL.','id NOT IN (SELECT DISTINCT MaterialLink_id AS Material_id FROM WICS_tmpmateriallistupdate WHERE MaterialLink_id IS NOT NULL)'))
        MustKeepMatlsCond.append(('.DEL.','(org_id, Material) IN (SELECT DISTINCT org_id, Material FROM WICS_tmpmateriallistupdate WHERE recStatus like "DEL%")'))
        MustKeepMatlsCond.append(('.SEL.','id NOT IN (SELECT DISTINCT Material_id FROM WICS_actualcounts)'))
        MustKeepMatlsCond.append(('.SEL.','id NOT IN (SELECT DISTINCT Material_id FROM WICS_countschedule)'))
        MustKeepMatlsCond.append(('.SEL.','id NOT IN (SELECT DISTINCT Material_id FROM WICS_sap_sohrecs)'))
        MustKeepMatlsSelCond = ''
        MustKeepMatlsDelCond = ''
        for sqlsttyp, phr in MustKeepMatlsCond:
            if 'SEL' in sqlsttyp:
                if MustKeepMatlsSelCond: MustKeepMatlsSelCond += ' AND '
                MustKeepMatlsSelCond += f'({phr})'
            if 'DEL' in sqlsttyp:
                if MustKeepMatlsDelCond: MustKeepMatlsDelCond += ' AND '
                MustKeepMatlsDelCond += f'({phr})'
    
        DeleteMatlsSelectSQL = "INSERT INTO WICS_tmpmateriallistupdate (recStatus, MaterialLink_id, org_id, Material, Description, Plant )"
        DeleteMatlsSelectSQL += " SELECT  concat('DEL ',FORMAT(id,0)), NULL, org_id, Material, Description, Plant "
        DeleteMatlsSelectSQL += " FROM WICS_materiallist"
        DeleteMatlsSelectSQL += f" WHERE ({MustKeepMatlsSelCond})"
        with connection.cursor() as cursor:
            cursor.execute(DeleteMatlsSelectSQL)
    
        set_async_comm_state(
            reqid,
            statecode = 'del-matl-2',
            statetext = f'Removing WICS Materials no longer in SAP MM60 Materials',
            )
        # do the Removals
        # I haven't figured out why, but this is the query that takes a loooong time
        DeleteMatlsDoitSQL = "DELETE FROM WICS_materiallist"
        DeleteMatlsDoitSQL += f" WHERE ({MustKeepMatlsDelCond})"
        with connection.cursor() as cursor:
            cursor.execute(DeleteMatlsDoitSQL)
            transaction.on_commit(partial(done_MatlListSAPSprsheet_03_Remove,reqid))
    def done_MatlListSAPSprsheet_03_Remove(reqid):
        key = f'MatlX{reqid}'
        statecodeVal = ".03."
        if async_comm.objects.filter(pk=key).exists():
            MatlXval = async_comm.objects.get(pk=key).statecode + statecodeVal
        else:
            MatlXval = statecodeVal
        set_async_comm_state(
            key, 
            statecode = MatlXval,
            statetext = '',
            new_async = True
            )
        set_async_comm_state(
            reqid,
            statecode = 'del-matl-done',
            statetext = f'Finished Removing WICS Materials no longer in SAP MM60 Materials',
            )
    
    def proc_MatlListSAPSprsheet_04_Add(reqid):
        set_async_comm_state(
            reqid,
            statecode = 'id-add-matl',
            statetext = f'Identifying SAP MM60 Materials new to WICS',
            )
    
        # first pass, for presentation in results - orgname rather than org
        MarkAddMatlsSelectSQL = "UPDATE WICS_tmpmateriallistupdate"
        MarkAddMatlsSelectSQL += " SET recStatus = 'ADD'"
        MarkAddMatlsSelectSQL += " WHERE (MaterialLink_id IS NULL) AND (recStatus is NULL)"
        with connection.cursor() as cursor:
            cursor.execute(MarkAddMatlsSelectSQL)
    
        set_async_comm_state(
            reqid,
            statecode = 'add-matl',
            statetext = f'Adding SAP MM60 Materials new to WICS',
            )
        UnknownTypeID = 18  # internally used code
        # do the adds
        # one day django will implement insert ... select.  Until then ...
        AddMatlsSelectSQL = "SELECT"
        AddMatlsSelectSQL += f" org_id, Material, Description, Plant, {UnknownTypeID} AS PartType_id"
        AddMatlsSelectSQL += " FROM WICS_tmpmateriallistupdate"
        AddMatlsSelectSQL += " WHERE (MaterialLink_id IS NULL) AND (recStatus = 'ADD') "
    
        AddMatlsDoitSQL = "INSERT INTO WICS_materiallist"
        AddMatlsDoitSQL += " (org_id, Material, Description, Plant, PartType_id"
        AddMatlsDoitSQL += ")"
        AddMatlsDoitSQL += f' {AddMatlsSelectSQL}'
        with connection.cursor() as cursor:
            cursor.execute(AddMatlsDoitSQL)
    
        set_async_comm_state(
            reqid,
            statecode = 'add-matl-get-recid',
            statetext = f'Getting Record ids of SAP MM60 Materials new to WICS',
            )
        UpdMaterialLinkSQL = 'UPDATE WICS_tmpmateriallistupdate, (select id, org_id, Material from WICS_materiallist) as MasterMaterials'
        UpdMaterialLinkSQL += ' set WICS_tmpmateriallistupdate.MaterialLink_id = MasterMaterials.id '
        UpdMaterialLinkSQL += ' where WICS_tmpmateriallistupdate.org_id = MasterMaterials.org_id '
        UpdMaterialLinkSQL += '   and WICS_tmpmateriallistupdate.Material = MasterMaterials.Material '
        UpdMaterialLinkSQL += "   and (MaterialLink_id IS NULL) AND (recStatus = 'ADD')"
        with connection.cursor() as cursor:
            cursor.execute(UpdMaterialLinkSQL)
            transaction.on_commit(partial(done_MatlListSAPSprsheet_04_Add,reqid))
    def done_MatlListSAPSprsheet_04_Add(reqid):
        key = f'MatlX{reqid}'
        statecodeVal = ".04."
        if async_comm.objects.filter(pk=key).exists():
            MatlXval = async_comm.objects.get(pk=key).statecode + statecodeVal
        else:
            MatlXval = statecodeVal
        set_async_comm_state(
            key, 
            statecode = MatlXval,
            statetext = '',
            new_async = True
            )
        set_async_comm_state(
            reqid,
            statecode = 'add-matl-done',
            statetext = f'Finished Adding SAP MM60 Materials new to WICS',
            )
    
    def proc_MatlListSAPSprsheet_99_FinalProc(reqid):
        set_async_comm_state(
            reqid,
            statecode = 'done',
            statetext = 'Finished Processing Spreadsheet',
            )
    
    def proc_MatlListSAPSprsheet_99_Cleanup(reqid):
        # also kill reqid, acomm, qcluster process
        async_comm.objects.filter(pk=reqid).delete()
        os.kill(int(reqid), signal.SIGTERM)
        os.kill(int(reqid), signal.SIGKILL)    # remove this line or put inside try...except block if running under non-Unix
    
        # delete the temporary table
        tmpMaterialListUpdate.objects.all().delete()
    
    @login_required
    def fnUpdateMatlListfromSAP(req):
        client_phase = req.POST['phase'] if 'phase' in req.POST else None
        reqid = req.COOKIES['reqid'] if 'reqid' in req.COOKIES else None
    
        if req.method == 'POST':
            # check if the mandatory commits have been done and change the status code if so
            if reqid is not None:
                mandatory_commit_key = f'MatlX{reqid}'
                mandatory_commit_list = ['03', '04']
                if async_comm.objects.filter(pk=mandatory_commit_key).exists():
                    mandatory_commits_recorded = async_comm.objects.get(pk=mandatory_commit_key).statecode
                    if all((c in mandatory_commits_recorded) for c in mandatory_commit_list):
                        proc_MatlListSAPSprsheet_99_FinalProc(reqid)
                        async_comm.objects.filter(pk=mandatory_commit_key).delete()
    
            if client_phase=='init-upl':
                retinfo = HttpResponse()
    
                # start django_q broker
                reqid = subprocess.Popen(
                    ['python', f'{django_settings.BASE_DIR}/manage.py', 'qcluster']
                ).pid
                retinfo.set_cookie('reqid',str(reqid))
                proc_MatlListSAPSprsheet_00InitUMLasync_comm(reqid)
    
                fName = proc_MatlListSAPSprsheet_00CopyUMLSpreadsheet(req, reqid)
                task01 = async_task(proc_MatlListSAPSprsheet_01ReadSpreadsheet, reqid, fName, hook=done_MatlListSAPSprsheet_01ReadSpreadsheet)
    
                acomm_fake = {
                    'statecode': 'starting',
                    'statetext': 'SAP MM60 Update Starting',
                    }
                retinfo.write(json.dumps(acomm_fake))
                return retinfo
            elif client_phase=='waiting':
                retinfo = HttpResponse()
    
                acomm = async_comm.objects.values().get(pk=reqid)    # something's very wrong if this doesn't exist
                stcode = acomm['statecode']
                if stcode == 'fatalerr':
                    pass
                retinfo.write(json.dumps(acomm))
                return retinfo
            elif client_phase=='wantresults':
                ImpErrList = tmpMaterialListUpdate.objects.filter(recStatus__startswith='err')
                AddedMatlsList = tmpMaterialListUpdate.objects.filter(recStatus='ADD')
                RemvdMatlsList = tmpMaterialListUpdate.objects.filter(recStatus__startswith='DEL')
                cntext = {
                    'ImpErrList':ImpErrList,
                    'AddedMatls':AddedMatlsList,
                    'RemvdMatls':RemvdMatlsList,
                    }
                templt = 'frmUpdateMatlListfromSAP_done.html'
                return render(req, templt, cntext)
            elif client_phase=='resultspresented':
                proc_MatlListSAPSprsheet_99_Cleanup(reqid)
                retinfo = HttpResponse()
                retinfo.delete_cookie('reqid')
    
                return retinfo
            else:
                return
            #endif client_phase
        else:
            cntext = {
                }
            templt = 'frmUpdateMatlListfromSAP_phase0.html'
        #endif req.method = 'POST'
    
        return render(req, templt, cntext)
    
    #########################################################################
    #########################################################################
    #########################################################################


    {### frmUpdateMatlListfromSAP_phase0.html ###}
    
    {% extends "WICS_common.html" %}
    {% load widget_tweaks %}
    {% load static %}
    
    {% block tTitle %}Update Material List from SAP Spreadsheet{% endblock %}
    
    {% block boddy %}
    <div class="container text-center mx-auto">
        <div class="row">
            <div class="col-7 fs-3 text-end">
                Update Material List from SAP MM60 Spreadsheet
            </div>
            <div class="col-3 text-start">
                <img src={% static 'WICS-Logo.png' %} width="200" height="100">
            </div>
            <div class="col-2 text-end"> {{ user.get_full_name }} </div>
        </div>
        <div class="row"> <!-- status messages -->
            <div id="wait_spinner" class="container" style="display:none">
                <div class="spinner-border text-success"></div>
                Processing... 
                <br>
                <span id="retStatecode" style="display:none"></span> <span id="Upload-Status"></span>
            </div>
            <div id="fatalErrMsg"></div>
        </div>
    </div>
    <hr>
    
    <hr>
    <form id="getUpdSprsheet" method="post" enctype="multipart/form-data">
        {% csrf_token %}
        Where is the SAP Material List Spreadsheet? 
        <p><input id="SAPFile" type="file"
            name="SAPFile"
            accept=".xlsx,application/vnd.ms-excel">
           </input>
        </p>
        <input id="phase" name="phase" type="hidden" value='init-upl'></input>
    
        <!-- form footer -->
        <div class="container">
            <div class="row mx-auto max-width=100%">
                <div class="col-4">
                    <button id="save_btn" type="button" onclick="PollBackend();">
                        <img src="{% static 'upload-outbox-line-icon.svg' %}" width="20" height="20"></img>
                        Continue
                    </button>
                    <input type="hidden" name="NextPhase" value="02-Upl-Sprsht"></input>
                </div>
                <div class="col-6"></div>
                <div class="col">
                    <button id="close_btn" type="button">
                        <img src="{% static 'stop-road-sign-icon.svg' %}" width="20" height="20"></img>
                        Close Form
                    </button>
                </div>
            </div>
        </div>
      </form>
    
    <script>
    
        var intervalID;
        const POLLING_INTERVAL = 3000;
    
        function PollBackend(){
    
            var phase = $("#phase").val()
            var retStatecode;
            const fform = document.getElementById("getUpdSprsheet");
            const formdata = new FormData(fform);
    
            function SetRetData(data) {
                $( '#Upload-Status' ).text( data.statetext );
                $( "#retStatecode" ).text(data.statecode);
                };
    
            if (phase == 'init-upl') {
                $( '#Upload-Status' ).text( "" );
                $( '#fatalErrMsg' ).text( "" );
                document.getElementById("wait_spinner").style.display = "block";
    
                $.ajax({
                    method: 'POST', 
                    data: formdata, 
                    processData: false, 
                    contentType: false, 
                    });
                $("#phase").val('waiting')
                intervalID = setInterval(PollBackend,POLLING_INTERVAL);
                $( "#retStatecode" ).text('waiting');   // fake code to skip rest of this iteration
            } else if (phase == 'waiting') {
                $.ajax({
                    method: 'POST', 
                    data: formdata, 
                    dataType: "json",
                    processData: false, 
                    contentType: false, 
                    success: SetRetData,
                    });
            };
    
            retStatecode = $( "#retStatecode" ).text();
            if (retStatecode == "fatalerr") {
                // kill intervalID = setInterval(PollBackend,1500,'waiting');
                clearInterval(intervalID);
    
                $( '#fatalErrMsg' ).text( $("#Upload-Status").text() );
                $( '#Upload-Status' ).text( "" );
                document.getElementById("wait_spinner").style.display = "none";
                
                $("#phase").val('init-upl')
                
                $( '#SAPFile' ).val(null);
                $( '#SAPFile' ).trigger("focus");
            }
            if (retStatecode == "done") {
                // kill intervalID = setInterval(PollBackend,1500,'waiting');
                clearInterval(intervalID);
    
                // switch to results
                $("#phase").val('wantresults');
                // change this - normal post, not ajax - is this right?
                $("#getUpdSprsheet").trigger("submit");
                /***
                $.ajax({
                    type: 'POST', 
                    data: formdata, 
                    dataType: "html",
                    processData: false, 
                    contentType: false, 
                    success: function (data) {
                        document.open();
                        document.write(data);
                        document.close();
                        },
                    });
                ***/
            };
            }
        document.body.onbeforeunload = function() {
            document.getElementById("wait_spinner").style.display = "block";
            }
    
        document.getElementById("close_btn").addEventListener("click",
            function(){
                window.close();
            });
    
    </script>
    
    {% endblock %}
    
    /************************************************************************
    ************************************************************************/
    {### frmUpdateMatlListfromSAP_done.html ###}

    {% extends "WICS_common.html" %}
    {% load widget_tweaks %}
    {% load static %}
    
    {% block tTitle %}Update Material List from SAP MM60 Spreadsheet{% endblock %}
    
    {% block boddy %}
    <div class="container text-center mx-auto">
        <div class="row">
            <div class="col-5 fs-3 text-end">
                <br>
                Update Material List Finished
            </div>
            <div class="col-5 text-start">
                <img src={% static 'WICS-Logo.png' %} width="200" height="100">
            </div>
            <div class="col-2 text-end"> {{ user.get_full_name }} </div>
        </div>
        <div class="row"> <!-- status messages -->
            <div id="wait_spinner" class="spinner-border text-success" style="display:none"> Processing... </div>
        </div>
    </div>
    <hr>
    {% csrf_token %}
    {% if ImpErrList %}
    <hr>
    <b>Errors:</b>
    <ul>
        {% for err in ImpErrList %}
        <li>
            <b>{{ err.errmsg }}</b>
        </li>
        {% empty %}
            <li><b>None!</b></li>
        {% endfor %}
    </ul>
    {% endif %}
    <hr>
    Material Added:
    <ul>
        {% for rec in AddedMatls %}
            <li>
            id {{ rec.MaterialLink_id }} - 
            {{ rec.org }} -
            {{ rec.Material }} - 
            {{ rec.Description }} - 
            {{ rec.SAPMaterialType }} -
            {{ rec.SAPMaterialGroup }} -
            {{ rec.Price }} -
            {{ rec.PriceUnit }}
            </li>
        {% empty %}
            <li><b>None!</b></li>
        {% endfor %}
    </ul>
    <hr>
    Material Removed:
    <ul>
        {% for rec in RemvdMatls %}
            <li>
            {{ rec.org }} -
            {{ rec.Material }} - 
            {{ rec.Description }}
            </li>
        {% empty %}
            <li><b>None!</b></li>
        {% endfor %}
    </ul>
    
    <!-- form footer -->
    <div class="container">
        <div class="row mx-auto max-width=100%">
            <div class="col-4">
                <input type="hidden" name="NextPhase" value="99-DONE"></input>
            </div>
            <div class="col-6"></div>
            <div class="col">
                <button id="close_btn" type="button">
                    <img src="{% static 'stop-road-sign-icon.svg' %}" width="20" height="20"></img>
                    Close Form
                </button>
            </div>
        </div>
    </div>
    <script>
    
        $( document ).ready(function() {
            const formdata = new FormData();
            formdata.append('phase', 'resultspresented')
            csrftoken = document.querySelector('[name=csrfmiddlewaretoken]').value;
            $.ajax({
                type: 'POST', 
                data: formdata,
                headers: {'X-CSRFToken': csrftoken},
                processData: false, 
                contentType: false, 
                success: function(data) {}
                });
        });
    
        /****
         document.body.onbeforeunload = function() {
            document.getElementById("wait_spinner").style.display = "block";
            }
        ****/
    
        document.getElementById("close_btn").addEventListener("click",
            function(){
                window.close();
            });
    
    </script>
    
    {% endblock %}
