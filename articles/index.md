
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



Many of your questions about PythonAnywhere are likely to be answered below. If not, the best place to get support is in [our forums](https://www.pythonanywhere.com/forums/). We monitor them to make sure that every question gets answered, and you get the added benefit that other PythonAnywhere customers can help you out too. They're also a nice place for a chat ![:-\)](/smile.png)

If you want, you can access an even broader group of people by asking your questions on Stack Overflow; we check [all posts there tagged with pythonanywhere](//stackoverflow.com/questions/tagged/pythonanywhere) daily, and reply if no-one else has already solved the problem.

But if you want to ask your questions in private and get responses over email, you can use the "Send feedback" link at the top of any page on PythonAnywhere. We'll be alerted and will get back to you ASAP.

If you want help about Python programming generally (as opposed to PythonAnywhere), you can [buy 1:1 live Python help at Codementor](https://www.codementor.io/python-experts?utm_source=pythonanywhere&utm_medium=text-link&utm_content=forums&utm_campaign=pa-q1).


[TOC]


##Step-by-step guides for some common tasks


[ ![](//www.pythonanywhere.com/static/glyphicons/glyphicons_268_keyboard_wireless@2x.png) I want to start learning Python ](//www.pythonanywhere.com/task_helpers/start/1-start_python/)

[ ![](//www.pythonanywhere.com/static/glyphicons/glyphicons_254_fishes@2x.png) I want to follow the Django Tutorial ](//www.pythonanywhere.com/task_helpers/start/2-following-the-django-tutorial/)

[ ![](//www.pythonanywhere.com/static/glyphicons/glyphicons_232_cloud@2x.png) I want to create a web application ](//www.pythonanywhere.com/task_helpers/start/3-web_app/)

[ ![](//www.pythonanywhere.com/static/glyphicons/glyphicons_137_computer_service@2x.png) I have built a web app on my local PC and want to deploy it on PythonAnywhere ](//www.pythonanywhere.com/task_helpers/start/4-deploy-local-web-app)

[ ![](//www.pythonanywhere.com/static/glyphicons/glyphicons_341_github@2x.png) I want to clone and hack on my GitHub project ](//www.pythonanywhere.com/task_helpers/start/5-github/)

[ ![](//www.pythonanywhere.com/static/glyphicons/glyphicons_074_cup@2x.png) I want to check out the Education Beta features ](//www.pythonanywhere.com/task_helpers/start/6-education/)



##Popular services, common requests, FAQ


  * **Github** should work just fine. On free accounts, **git** to other sites will only work over https to [whitelisted](/pages/403ForbiddenError) sites.
  * **Subversion/svn** will work fine, although, again, free accounts need to use `<https://>`, not `svn+<ssh://>`, and will be able to access [whitelisted](/pages/403ForbiddenError) sites only
  * **Can I use MongoDB**? Only via an external service
  * **Can I use an external MySQL service?** Probably not (on a free account), unless they have an HTTP api.
  * [Why do I get a "403 Forbidden" error when accessing a website from PythonAnywhere?](/pages/403ForbiddenError)
  * [I get "permission denied" when trying to pip install a new module](/pages/InstallingNewModules)
  * [Can I use SMTP to send email on a Free account?](/pages/SMTPForFreeUsers)
  * [Can I edit my config files?](/pages/ConfigFiles)
  * [Can I use matplotlib to generate graphs from my data?](/pages/MatplotLibGraphs)
  * [How do I keep a console running forever? Or, how do I make a program that restarts automatically?](/pages/LongRunningTasks)
  * [Can I use PythonAnywhere for teaching? Are there any special features for education?](/pages/Education)


##Using PythonAnywhere consoles


  * [Types of PythonAnywhere consoles](/pages/TypesOfConsoles)
  * [Copying and pasting in PythonAnywhere consoles](/pages/CopyAndPaste)
  * [Changing the font size in a PythonAnywhere console](/pages/ChangingFontSize)
  * [Changing a console's name](/pages/ChangingConsolesName)
  * [SSH access to your account](/pages/SSHAccess)
  * [What are CPU-seconds?](/pages/WhatAreCPUSeconds)
  * [How can I use Python 2 with the "Save &amp; Run" button?](/pages/SaveAndRunPythonVersion)
  * [I want to embed a live python console on my website](/pages/EmbeddedConsoles)
  * Problems with consoles:
    * [I can't see what I'm typing in the console](/pages/ICantSeeWhatIAmTyping)
    * [The "Starting encrypted connection" message never disappears](/pages/StartingEncryptedConnection)
    * [I can't type certain keys into the console, like close-parenthesis (international keyboards)](/pages/TypingProblemsInternational)


##Working with PythonAnywhere web applications


  * [How to create a web application on PythonAnywhere](/pages/WebAppBasics)
  * [Creating a new Django project on PythonAnywhere](/pages/DjangoTutorial)
  * [Reloading the web application after you've made changes](/pages/ReloadWebApp)
  * [How to use your own domain for your web app (CNAME setup)](/pages/OwnDomains)
  * [Debugging import errors and sys.path issues](/pages/DebuggingImportError)
  * [How to use our static files service, and why you might want to](/pages/StaticFiles)
  * [How to use SSL for your own domain](/pages/SSLOwnDomains)
  * [How to force HTTPS on your web app](/pages/ForcingHTTPS)
  * [I'm getting a 502 Bad Gateway error. How can I debug?](/pages/502BadGateway)
  * [How to point a new domain at an existing web app](/pages/UsingANewDomainForExistingWebApp)
  * [A guide to setting up a virtualenv for PythonAnywhere webapps](/pages/VirtualEnvForNewerDjango) (so that you can use your own versions of different modules -- for example, Django 1.6 instead of the default 1.3.7)
  * [Using a virtualenv for your web app](/pages/Virtualenvs)
  * [Switching to the new virtualenv system](/pages/UpgradingToTheNewVirtualenvSystem)
  * [Getting the IP address of clients connecting to your web app](/pages/WebAppClientIPAddresses)
  * [Python 3 web apps](/pages/Python3WebApps)
  * [Using Flask](/pages/Flask)
  * [Using CherryPy](/pages/UsingCherryPy)
  * [Using Tornado](/pages/UsingTornado)
  * [How to use Mezzanine on PythonAnywhere](/pages/HowtouseMezzanineonPythonAnywhere)


###Common problems for specific web frameworks


  * All
    * [Debugging import errors and sys.path issues](/pages/DebuggingImportError)
    * [How do I get streaming/buffering to work?](/pages/Buffering)
  * [Web2Py](//www.web2py.com/)
    * ["Admin is disabled because insecure channel (web2py error)"](/pages/AdminIsDisabledBecauseInsecureChannel)
    * [How do I set up different apps for different domains in Web2py?](/pages/MultipleDomainsWeb2py)
    * [How do I change my admin password in Web2py?](/pages/Web2pyAdminPassword)
    * [How do I run the web2py scheduler?](/pages/Web2pyScheduler)
  * Django
    * [How to follow the Django Tutorial on PythonAnywhere](/pages/FollowingTheDjangoTutorial)
    * [How can I use Django 1.7](/pages/VirtualEnvForNewerDjango) under Python 2.7 (1.6 is the default under Python 3.3/4)
    * [How to setup static files under Django](/pages/DjangoStaticFiles) -- STATIC_ROOT in settings.py, `collectstatic`, etc
    * [The Django admin's CSS isn't working](/pages/DjangoAdminCSSNotWorking)
  * Flask
    * [Dealing with a 504 error in Flask applications](/pages/Flask504Error)
    * [General flask tips, including avoiding app.run() and how to run database config with db.create_all()](/pages/Flask)
  * Web.py
    * ["Web.py application WSGI configuration"](/pages/WebDotPyWSGIConfig)


##Useful Python modules


  * [Batteries included](https://www.pythonanywhere.com/batteries_included/): a list of all Python modules installed by default on PythonAnywhere
  * [Installing new Python modules for yourself](/pages/InstallingNewModules)
  * [Installing the Quant Software Toolkit on PythonAnywhere](/pages/InstallingQSTKonPythonAnywhere)
  * [Rebuilding a Virtualenv](/pages/RebuildingVirtualenvs)


##Doing stuff with files


  * [Using the file browser](/pages/FileBrowser)
  * [The file editor](/pages/FileEditor)
  * [Can I use FTP/Filezilla? How should I upload my code to PythonAnywhere?](/pages/FTP)
  * [Dropbox (deprecated, for now)](/pages/UsingDropbox)
  * [Using external version control systems](/pages/ExternalVCS) (eg. [GitHub](//www.github.com/), [BitBucket](//www.bitbucket.org/))


##Databases


  * [Databases available on PythonAnywhere](/pages/KindsOfDatabases)
  * [Using MySQL (including using MySQL with Python 3)](/pages/UsingMySQL)
  * [Getting started with Postgres](/pages/Postgres)
  * [Creating Postgres backups](/pages/RegularPostgresBackups)
  * [How do I find out how large my MySQL database is?](/pages/MySQLDatabaseSize)
  * [Migrating a web2py app from SQLite to MySQL](/pages/MigatingWeb2pyFromSQLiteToMySQL)
  * [Database character sets (UTF8/Unicode etc)](/pages/DatabaseCharacterSets)
  * [LOAD DATA INFILE doesn't work](/pages/LoadDataInfile)
  * [Importing a database you have stored on your own machine to PythonAnwyhere](/pages/ImportingYourLocalDatabaseToPythonAnywhere)
  * [Tunnelling SSH for MySQL GUIs](/pages/SSHTunnelling)
  * [Fixing "OperationalError: 2006 MySQL server has gone away"](/pages/ManagingDatabaseConnections)
  * [Fixing "OperationalError: 1226 User has exceeded the max_user_connections resource](/pages/ManagingDatabaseConnections)
  * [Using SQLAlchemy with MySQL](/pages/UsingSQLAlchemywithMySQL)


##Running tasks periodically


  * [Using the "Schedule" tab](/pages/ScheduledTasks)
  * [Can I pass command-line arguments and parameters to my scheduled tasks?](/pages/ScheduledTaskParameters)
  * [How do I run the web2py scheduler?](/pages/Web2pyScheduler)
  * [How do I keep a console running forever? Or, how do I make a program that restarts automatically?](/pages/LongRunningTasks)


##Other Languages


  * [Setting up Haskell and creating a new Cabal package](/pages/Haskell)
  * [Testing a simple Javascript project using Jasmine](/pages/Javascript)
