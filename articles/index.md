
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



Many of your questions about PythonAnywhere are likely to be answered below. If
not, the best place to get support is in
our [**Forums**](https://www.pythonanywhere.com/forums/). We monitor them to make
sure that every question gets answered, and you get the added benefit that
other PythonAnywhere customers can help you out too. They're also a nice place
for a chat ![:-\)](/smile.png)

If you want, you can access an even broader group of people by asking your
questions on *StackOverflow*; we check
[all posts there tagged with pythonanywhere](//stackoverflow.com/questions/tagged/pythonanywhere)
 daily, and reply if no-one else has already solved the problem.

But if you want to ask your questions in private and get responses over **email**,
you can use the "Send feedback" link at the top of any page on PythonAnywhere.
We'll be alerted and will get back to you ASAP.  You can also email us directly
via [support@pythonanywhere.com](mailto:support@pythonanywhere.com)

If you want help about Python programming generally (as opposed to
PythonAnywhere), you can
[buy 1:1 live Python help at Codementor](https://www.codementor.io/python-experts?utm_source=pythonanywhere&utm_medium=text-link&utm_content=forums&utm_campaign=pa-q1).


The help pages have the following sections -- hopefully you can jump straight to one that describes what you're looking for help with!

[TOC]

# I'm a beginner learning Python

We have lots of beginners on PythonAnywhere! Here's a very quick step-by-step tutorial you might want to start with:

<a href="//www.pythonanywhere.com/task_helpers/start/1-start_python/" class="btn">
    <img alt="keyboard icon" src="//www.pythonanywhere.com/static/glyphicons/glyphicons_268_keyboard_wireless@2x.png">
    &nbsp;
     I want to start learning Python
</a>

And here are some common questions and guides for beginners:

  * [How can I use Python 2 with the "Save &amp; Run" button?](/pages/SaveAndRunPythonVersion)
  * [Installing new Python modules for yourself](/pages/InstallingNewModules)
  * [Using the file browser](/pages/FileBrowser)
  * [The file editor](/pages/FileEditor)
  * [Changing the font size in a PythonAnywhere console](/pages/ChangingFontSize)

<!-- TODO: how do I edit a file?  How do I run a script? -->


# I've got an existing web app that I'm trying to deploy

This section assumes you have started building a web app on your local PC, and you're now looking to deploy it to PythonAnywhere.

Here is a step-by-step tutorial that walks you through the general outline of how to set up an existing web app on PythonAnywhehre

<a href="//www.pythonanywhere.com/task_helpers/start/4-deploy-local-web-app/" class="btn">
    <img alt="computer icon" src="//www.pythonanywhere.com/static/glyphicons/glyphicons_137_computer_service@2x.png">
    &nbsp;
     I have built a web app on my local PC and want to deploy it on PythonAnywhere
</a>

And here are some popular how-to guides and help pages for common webapp issues:

  * [Can I use FTP/Filezilla? How should I upload my code to PythonAnywhere?](/pages/FTP)
  * [Debugging import errors and sys.path issues in your WSGI file](/pages/DebuggingImportError)
  * [Using a virtualenv for your web app](/pages/Virtualenvs)
  * [How to use your own domain for your web app (CNAME setup)](/pages/OwnDomains)
  * [How to use our static files service, and why you might want to](/pages/StaticFiles)
  * [How to use SSL for your own domain](/pages/SSLOwnDomains)
  * [How to get a Let's Encrypt certificate for your own domain](/pages/LetsEncrypt)
  * [How to use ZeroSSL](/pages/ZeroSSL), an alternative interface to LetsEncrypt
  * [How to set environment variables in web apps](/pages/environment-variables-for-web-apps)
  * [How to handle slow/async work in a web app](/pages/AsyncInWebApps)
  * [How to point a new domain at an existing web app in the Web tab](/pages/UsingANewDomainForExistingWebApp)
  * [Using MySQL (including using MySQL with Python 3)](/pages/UsingMySQL)
  * [I'm getting a 502 Bad Gateway error. How can I debug?](/pages/502BadGateway)
  * [How to host a static site on PythonAnywhere](/pages/hosting-a-static-site)
  * [Using International Domain Names](/pages/InternationalDomainNames) -- that is, ones with non-ASCII/Unicode characters in them


And some tips for specific web frameworks:


  * Django
    * [Deploying an existing Django project on PythonAnywhere](/pages/DeployExistingDjangoProject)
    * [How can I use a more recent version of Django for a new project](/pages/VirtualEnvForNewerDjango)
    * [How to setup static files under Django](/pages/DjangoStaticFiles) -- STATIC_ROOT in settings.py, `collectstatic`, etc
    * [The Django admin's CSS isn't working](/pages/DjangoAdminCSSNotWorking)
    * [How to set SECRET_KEY via an environment variable](/pages/environment-variables-for-web-apps)
<!--TODO: Django 400 bad request ALLOWED_HOSTS page -->

  * Flask
    * [A beginner's guide to building a simple database-backed Flask website on PythonAnywhere](http://blog.pythonanywhere.com/121/)
    * [General flask tips, including avoiding app.run() and how to run database config with db.create_all()](/pages/Flask)
    * [Dealing with a 504 error in Flask applications](/pages/Flask504Error)
    * [Using SQLAlchemy with MySQL](/pages/UsingSQLAlchemywithMySQL)

  * Web2Py
    * ["Admin is disabled because insecure channel (web2py error)"](/pages/AdminIsDisabledBecauseInsecureChannel)
    * [How do I set up different apps for different domains in Web2py?](/pages/MultipleDomainsWeb2py)
    * [How do I change my admin password in Web2py?](/pages/Web2pyAdminPassword)
    * [How do I run the web2py scheduler?](/pages/Web2pyScheduler)

  * Others
    * [How to use Mezzanine on PythonAnywhere](/pages/HowtouseMezzanineonPythonAnywhere)
    * [Using CherryPy](/pages/UsingCherryPy)
    * [Using Tornado (WSGI-only mode)](/pages/UsingTornado)
    * [Using Web.py](/pages/WebDotPyWSGIConfig)
    * [How to host a static site on PythonAnywhere](/pages/hosting-a-static-site)




# I'm looking at an error message in a console

Oh no!  Here's our most common explanations and solutions to console problems:

  * [I get "permission denied" when trying to pip install a new module](/pages/InstallingNewModules)
  * [Why do I get a "403 Forbidden" error when accessing a website from PythonAnywhere?](/pages/403ForbiddenError)
  * [I'm getting "no such file or directory"](/pages/NoSuchFileOrDirectory)
  * [LOAD DATA INFILE doesn't work](/pages/LoadDataInfile)
  * ["Disk Quota Exceeded" (running out of storage space / maxing out your quota)](/pages/DiskQuotaExceeded)


Some technical problems with consoles that sometimes come up:

  * [I can't see what I'm typing in the console](/pages/ICantSeeWhatIAmTyping)
  * [The "Starting encrypted connection" message never disappears](/pages/StartingEncryptedConnection)
  * [I can't see what I'm typing in the console](/pages/ICantSeeWhatIAmTyping)



# I'm looking at an error message in my web app


Oh no!  But fear not -- the likelihood is that we've seen someone else with this error before, and we know how to fix it.

If you haven't already, the first step is to look in your **error log** -- you'll find a link to it on the [Web tab](https://www.pythonanywhere.com/web_app_setup/).

Once you've done that, here are some solutions to common problems

  * [Debugging import errors and sys.path issues](/pages/DebuggingImportError)  <--  if you've just started setting up your app, chances are the answer is in here.
  * [Dealing with "there was an error reloading your web app" messages](/pages/ErrorReloadingWebApp)
  * [I'm getting a 502 Bad Gateway error. How can I debug?](/pages/502BadGateway)
  * [I'm getting a 400 Bad Request error from my Django app](/pages/Django400BadRequest)
  * [Debugging problems with static files (js, css) not loading](/pages/DebuggingStaticFiles)
  * [Fixing "OperationalError: 2006 MySQL server has gone away"](/pages/ManagingDatabaseConnections)
  * [Fixing "OperationalError: 1226 User has exceeded the max_user_connections resource](/pages/ManagingDatabaseConnections)
  * [I'm seeing lots of GeneratorExit errors in my error log](/pages/GeneratorExit)



# I'm trying to figure out how to get a particular tool or feature to work

Here are some guides for some of the common things people want to do:

  * [Installing new Python modules for yourself](/pages/InstallingNewModules)
  * [How do I keep a console running forever? Or, how do I make a program that restarts automatically?](/pages/LongRunningTasks)
  * [How to I run an async task queue like celery?](/pages/AsyncInWebApps)
  * [Can I use matplotlib to generate graphs from my data?](/pages/MatplotLibGraphs)
  * [Can I use SMTP to send email on a Free account?](/pages/SMTPForFreeUsers)
  * [How to force HTTPS on your web app](/pages/ForcingHTTPS)
  * [Using MySQL (including using MySQL with Python 3)](/pages/UsingMySQL)
  * [Backing up (and restoring) MySQL databases using mysqldump](/pages/MySQLBackupRestore)
  * [Working with PDFs and converting document formats](/pages/PDF)
  * [Can I use IPv6?](/pages/IPv6)
  * [Using Selenium](/pages/selenium)
  * [Does PythonAnywhere have an API?](/pages/API)
  * [What do I do if a server I want to connect to has a whitelist that only allows incoming connections from particular (static) IPs?](/pages/StaticIPForExternalWhitelists)


And here's some very brief FAQ answers about common requests:

  * **Can I use MongoDB**? Only via an external service like mongolabs
  * **Can I use an external MySQL service?** Probably not (on a free account), unless they have an HTTP api.
  * Can I use Redis?  Again, only via an external service like redislabs.  Although you can use redislite
  * Can I use websockets, or run my own socket server?  I'm afraid not --  we only support Python apps that implement the WSGI protocol
  * How do I reload my webapp automatically?  You can now use our [API](/pages/API) for this :)



# I'm a teacher looking to use PythonAnywhere for education

Welcome!  We have lots of teachers and students on board.  Check out this page for an overview of our education-specific features:

  * [General info on our educational features](/pages/Education)


Or you can run through this step-by-step tutorial if you prefer:

<a href="//www.pythonanywhere.com/task_helpers/start/6-education/" class="btn">
    <img alt="trophy icon" src="//www.pythonanywhere.com/static/glyphicons/glyphicons_074_cup@2x.png">
    &nbsp;
    I want to check out the Education Beta features
</a>



# A few other topics

  * [how to get SSH access to your account](/pages/SSHAccess)
  * [How to follow the Django Tutorial on PythonAnywhere](/pages/FollowingTheDjangoTutorial)
  * [I want to embed a live python console on my website](/pages/EmbeddedConsoles)
  * [Getting the IP address of clients connecting to your web app](/pages/WebAppClientIPAddresses)
  * [How do I get streaming/buffering to work?](/pages/Buffering)
  * [How to use a virtualenv in an IPython Notebook](/pages/IPythonNotebookVirtualenvs)
  * [What are these virtualenv things, anyway?](/pages/VirtualenvsExplained)



# Some older/miscellaneous guides


Files:

  * [Can I edit my config files?](/pages/ConfigFiles)
  * [Dropbox (deprecated, for now)](/pages/UsingDropbox)

Consoles:

  * [Types of PythonAnywhere consoles](/pages/TypesOfConsoles)
  * [Copying and pasting in PythonAnywhere consoles](/pages/CopyAndPaste)
  * [Changing a console's name](/pages/ChangingConsolesName)
  * [What are CPU-seconds?](/pages/WhatAreCPUSeconds)
  * [Using external version control systems](/pages/ExternalVCS) (eg. [GitHub](//www.github.com/), [BitBucket](//www.bitbucket.org/))

Web apps:

  * [How to create a web application on PythonAnywhere](/pages/WebAppBasics)
  * [Reloading the web application after you've made changes](/pages/ReloadWebApp)
  * [Switching to the new virtualenv system](/pages/UpgradingToTheNewVirtualenvSystem)
  * [Python 3 web apps](/pages/Python3WebApps)

  * [Batteries included](https://www.pythonanywhere.com/batteries_included/): a list of all Python modules installed by default on PythonAnywhere
  * [Installing the Quant Software Toolkit on PythonAnywhere](/pages/InstallingQSTKonPythonAnywhere)
  * [Rebuilding a Virtualenv](/pages/RebuildingVirtualenvs)


Databases:

  * [Databases available on PythonAnywhere](/pages/KindsOfDatabases)
  * [Activating a Postgres server](/pages/Postgres)
  * [Congiguring postgres for your app (eg Django)](/pages/PostgresGettingStarted)
  * [Creating Postgres backups](/pages/RegularPostgresBackups)
  * [Increasing the number of connections for your Postgres server](/pages/PostgresConnections)
  * [Connecting to Microsoft SQL Server](/pages/MSSQLServer)
  * [How do I find out how large my MySQL database is?](/pages/MySQLDatabaseSize)
  * [Migrating a web2py app from SQLite to MySQL](/pages/MigatingWeb2pyFromSQLiteToMySQL)
  * [Database character sets (UTF8/Unicode etc)](/pages/DatabaseCharacterSets)
  * [Importing a database you have stored on your own machine to PythonAnwyhere](/pages/ImportingYourLocalDatabaseToPythonAnywhere)
  * [Accessing your MySQL database from outside PythonAnywhere](/pages/AccessingMySQLFromOutsidePythonAnywhere)

Scheduled tasks:

  * [Using the "Schedule" tab](/pages/ScheduledTasks)
  * [Can I pass command-line arguments and parameters to my scheduled tasks?](/pages/ScheduledTaskParameters)
  * [How do I run a scheduled task inside a virtualenv](/pages/VirtualEnvInScheduledTasks)

Other Languages:

  * [Setting up Haskell and creating a new Cabal package](/pages/Haskell)
  * [Setting up a Node project](/pages/Node)
  * [Testing a simple Javascript project using Jasmine](/pages/Javascript)



# A few other step-by-step guides

<a href="//www.pythonanywhere.com/task_helpers/start/2-following-the-django-tutorial/" class="btn">
    <img alt="fishies icon" src="//www.pythonanywhere.com/static/glyphicons/glyphicons_254_fishes@2x.png">
    &nbsp;
    I want to follow the Django Tutorial
</a>

<a href="//www.pythonanywhere.com/task_helpers/start/3-web_app/" class="btn">
    <img alt="cloud icon" src="//www.pythonanywhere.com/static/glyphicons/glyphicons_232_cloud@2x.png">
    &nbsp;
    I want to create a web application
</a>

<a href="//www.pythonanywhere.com/task_helpers/start/5-github/" class="btn">
    <img alt="github icon" src="//www.pythonanywhere.com/static/glyphicons/glyphicons_341_github@2x.png">
    &nbsp;
    I want to clone and hack on my GitHub project
</a>

# Security

* [Securing your PythonAnywhere account](/pages/SecuringYourAccount)
* [Details on the PythonAnywhere Bug Bounty](/pages/BugBounty)
