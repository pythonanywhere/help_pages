
<!--
.. title: The PythonAnywhere help pages
.. slug: index
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



Many of your questions about PythonAnywhere are likely to be answered below. If not, the best place to get support is in [our forums](https://www.pythonanywhere.com/forums/). We monitor them to make sure that every question gets answered, and you get the added benefit that other PythonAnywhere customers can help you out too. They're also a nice place for a chat ![:-\)](/help/smile.png)

If you want, you can access an even broader group of people by asking your questions on Stack Overflow; we check [all posts there tagged with pythonanywhere](//stackoverflow.com/questions/tagged/pythonanywhere) daily, and reply if no-one else has already solved the problem. 

But if you want to ask your questions in private and get responses over email, you can use the "Send feedback" link at the top of any page on PythonAnywhere. We'll be alerted and will get back to you ASAP. 

If you want help about Python programming generally (as opposed to PythonAnywhere), you can [buy 1:1 live Python help at Codementor](https://www.codementor.io/python-experts?utm_source=pythonanywhere&utm_medium=text-link&utm_content=forums&utm_campaign=pa-q1). 


#Contents


[TOC]


##Step-by-step guides for a some common tasks


[ ![](//www.pythonanywhere.com/static/glyphicons/glyphicons_268_keyboard_wireless@2x.png) I want to start learning Python ](//www.pythonanywhere.com/task_helpers/start/1-start_python/)

[ ![](//www.pythonanywhere.com/static/glyphicons/glyphicons_254_fishes@2x.png) I want to follow the Django Tutorial ](//www.pythonanywhere.com/task_helpers/start/2-following-the-django-tutorial/)

[ ![](//www.pythonanywhere.com/static/glyphicons/glyphicons_232_cloud@2x.png) I want to create a web application ](//www.pythonanywhere.com/task_helpers/start/3-web_app/)

[ ![](//www.pythonanywhere.com/static/glyphicons/glyphicons_137_computer_service@2x.png) I have built a web app on my local PC and want to deploy it on PythonAnywhere ](//www.pythonanywhere.com/task_helpers/start/4-deploy-local-web-app)

[ ![](//www.pythonanywhere.com/static/glyphicons/glyphicons_341_github@2x.png) I want to clone and hack on my GitHub project ](//www.pythonanywhere.com/task_helpers/start/5-github/)

[ ![](//www.pythonanywhere.com/static/glyphicons/glyphicons_074_cup@2x.png) I want to check out the Education Beta features ](//www.pythonanywhere.com/task_helpers/start/6-education/)

[ ![](//www.pythonanywhere.com/static/glyphicons/glyphicons_245_chat@2x.png) I want to suggest a new button to go here. ](){: .feedback_link}


##Popular services, common requests, FAQ


  * **Github** should work just fine. On free accounts, **git** to other sites will only work over https to [whitelisted](/help/pages/403ForbiddenError) sites. 
  * **Subversion/svn** will work fine, although, again, free accounts need to use `<https://>`, not `svn+<ssh://>`, and will be able to access [whitelisted](/help/pages/403ForbiddenError) sites only 
  * **Can I use MongoDB**? Only via an external service 
  * **Can I use an external MySQL service?** Probably not (on a free account), unless they have an HTTP api. 
  * [Why do I get a "403 Forbidden" error when accessing a website from PythonAnywhere?](/help/pages/403ForbiddenError)
  * [I get "permission denied" when trying to pip install a new module](/help/pages/InstallingNewModules)
  * [Can I use SMTP to send email on a Free account?](/help/pages/SMTPForFreeUsers)
  * [Can I edit my config files?](/help/pages/ConfigFiles)
  * [Can I use matplotlib to generate graphs from my data?](/help/pages/MatplotLibGraphs)
  * [How do I keep a console running forever? Or, how do I make a program that restarts automatically?](/help/pages/LongRunningTasks)
  * [Can I use PythonAnywhere for teaching? Are there any special features for education?](/help/pages/Education)


##Using PythonAnywhere consoles


  * [Types of PythonAnywhere consoles](/help/pages/TypesOfConsoles)
  * [Copying and pasting in PythonAnywhere consoles](/help/pages/CopyAndPaste)
  * [Changing the font size in a PythonAnywhere console](/help/pages/ChangingFontSize)
  * [Changing a console's name](/help/pages/ChangingConsolesName)
  * [SSH access to your account](/help/pages/SSHAccess)
  * [What are CPU-seconds?](/help/pages/WhatAreCPUSeconds)
  * [How can I use Python 2 with the "Save &amp; Run" button?](/help/pages/SaveAndRunPythonVersion)
  * [I want to embed a live python console on my website](/help/pages/EmbeddedConsoles)
  * Problems with consoles: 
    * [I can't see what I'm typing in the console](/help/pages/ICantSeeWhatIAmTyping)
    * [My console seems to be stuck on a single line](/help/pages/SingleLineConsoleProblem)
    * [The "Starting encrypted connection" message never disappears](/help/pages/StartingEncryptedConnection)
    * [I can't type certain keys into the console, like close-parenthesis (international keyboards)](/help/pages/TypingProblemsInternational)


##Working with PythonAnywhere web applications


  * [How to create a web application on PythonAnywhere](/help/pages/WebAppBasics)
  * [Creating a new Django project on PythonAnywhere](/help/pages/DjangoTutorial)
  * [Reloading the web application after you've made changes](/help/pages/ReloadWebApp)
  * [How to use your own domain for your web app (CNAME setup)](/help/pages/OwnDomains)
  * [Debugging import errors and sys.path issues](/help/pages/DebuggingImportError)
  * [How to use our static files service, and why you might want to](/help/pages/StaticFiles)
  * [How to use SSL for your own domain](/help/pages/SSLOwnDomains)
  * [How to force HTTPS on your web app](/help/pages/ForcingHTTPS)
  * [I'm getting a 502 Bad Gateway error. How can I debug?](/help/pages/502BadGateway)
  * [How to point a new domain at an existing web app](/help/pages/UsingANewDomainForExistingWebApp)
  * [A guide to setting up a virtualenv for PythonAnywhere webapps](/help/pages/VirtualEnvForNewerDjango) (so that you can use your own versions of different modules -- for example, Django 1.6 instead of the default 1.3.7) 
  * [Getting the IP address of clients connecting to your web app](/help/pages/WebAppClientIPAddresses)
  * [Using Flask](/help/pages/Flask)
  * [Using CherryPy](/help/pages/UsingCherryPy)
  * [Using Tornado](/help/pages/UsingTornado)
  * [How to use Mezzanine on PythonAnywhere](/help/pages/HowtouseMezzanineonPythonAnywhere)


###Common problems for specific web frameworks


  * All 
    * [Debugging import errors and sys.path issues](/help/pages/DebuggingImportError)
    * [How do I get streaming/buffering to work?](/help/pages/Buffering)
  * [Web2Py](/help/pages/Web2Py)
    * ["Admin is disabled because insecure channel (web2py error)"](/help/pages/AdminIsDisabledBecauseInsecureChannel)
    * [How do I set up different apps for different domains in Web2py?](/help/pages/MultipleDomainsWeb2py)
    * [How do I change my admin password in Web2py?](/help/pages/Web2pyAdminPassword)
    * [How do I run the web2py scheduler?](/help/pages/Web2pyScheduler)
  * Django 
    * [How to follow the Django Tutorial on PythonAnywhere](/help/pages/FollowingTheDjangoTutorial)
    * [How can I use Django 1.7](/help/pages/VirtualEnvForNewerDjango) under Python 2.7 (1.6 is the default under Python 3.3/4) 
    * [How to setup static files under Django](/help/pages/DjangoStaticFiles) -- STATIC_ROOT in settings.py, `collectstatic`, etc 
    * [The Django admin's CSS isn't working](/help/pages/DjangoAdminCSSNotWorking)
  * Flask 
    * [Dealing with a 504 error in Flask applications](/help/pages/Flask504Error)
    * [General flask tips, including avoiding app.run() and how to run database config with db.create_all()](/help/pages/Flask)
  * Web.py 
    * ["Web.py application WSGI configuration"](/help/pages/WebDotPyWSGIConfig)


##Useful Python modules


  * [Batteries included](https://www.pythonanywhere.com/batteries_included/): a list of all Python modules installed by default on PythonAnywhere
  * [Installing new Python modules for yourself](/help/pages/InstallingNewModules)
  * [Installing the Quant Software Toolkit on PythonAnywhere](/help/pages/InstallingQSTKonPythonAnywhere)
  * [Rebuilding a Virtualenv](/help/pages/RebuildingVirtualenvs)


##Doing stuff with files


  * [Using the file browser](/help/pages/FileBrowser)
  * [The file editor](/help/pages/FileEditor)
  * [Can I use FTP/Filezilla? How should I upload my code to PythonAnywhere?](/help/pages/FTP)
  * [Dropbox (deprecated, for now)](/help/pages/UsingDropbox)
  * [Using external version control systems](/help/pages/ExternalVCS) (eg. [GitHub](/help/pages/GitHub), [BitBucket](/help/pages/BitBucket)) 


##Databases


  * [Databases available on PythonAnywhere](/help/pages/KindsOfDatabases)
  * [Using MySQL (including using MySQL with Python 3)](/help/pages/UsingMySQL)
  * [Getting started with Postgres](/help/pages/Postgres)
  * [How do I find out how large my MySQL database is?](/help/pages/MySQLDatabaseSize)
  * [Migrating a web2py app from SQLite to MySQL](/help/pages/MigatingWeb2pyFromSQLiteToMySQL)
  * [Database character sets (UTF8/Unicode etc)](/help/pages/DatabaseCharacterSets)
  * [LOAD DATA INFILE doesn't work](/help/pages/LoadDataInfile)
  * [Importing a database you have stored on your own machine to PythonAnwyhere](/help/pages/ImportingYourLocalDatabaseToPythonAnywhere)
  * [Tunnelling SSH for MySQL GUIs](/help/pages/SSHTunnelling)
  * [Fixing "OperationalError: 2006 MySQL server has gone away"](/help/pages/ManagingDatabaseConnections)
  * [Fixing "OperationalError: 1226 User has exceeded the max_user_connections resource](/help/pages/ManagingDatabaseConnections)
  * [Using SQLAlchemy with MySQL](/help/pages/UsingSQLAlchemywithMySQL)


##Running tasks periodically


  * [Using the "Schedule" tab](/help/pages/ScheduledTasks)
  * [Can I pass command-line arguments and parameters to my scheduled tasks?](/help/pages/ScheduledTaskParameters)
  * [How do I run the web2py scheduler?](/help/pages/Web2pyScheduler)
  * [How do I keep a console running forever? Or, how do I make a program that restarts automatically?](/help/pages/LongRunningTasks)


##Other Languages


  * [Setting up Haskell and creating a new Cabal package](/help/pages/Haskell)
  * [Testing a simple Javascript project using Jasmine](/help/pages/Javascript)
