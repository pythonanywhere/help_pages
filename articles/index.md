
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
our [**Forums**](https://www.pythonanywhere.com/forums/) and
[**EU Forums**](https://eu.pythonanywhere.com/forums/). We monitor them to make
sure that every question gets answered, and you get the added benefit that
other PythonAnywhere customers can help you out too. They're also a nice place
for a chat ![:-\)](/smile.png)

If you want, you can access an even broader group of people by asking your
questions on **StackOverflow**; we check
[all posts there tagged with pythonanywhere](//stackoverflow.com/questions/tagged/pythonanywhere)
 daily, and reply if no-one else has already solved the problem.

But if you want to ask your questions in private and get responses over **email**,
you can use the "Send feedback" link at the top of any page on PythonAnywhere.
We'll be alerted and will get back to you ASAP.  You can also email us directly
via [support@pythonanywhere.com](mailto:support@pythonanywhere.com)

If you want help about Python programming generally (as opposed to
PythonAnywhere), you can
[buy 1:1 live Python help at Codementor](https://www.codementor.io/python-experts?utm_source=pythonanywhere&utm_medium=text-link&utm_content=forums&utm_campaign=pa-q1).

We also have a page that lists books and courses the people have recommended to us [here](/pages/Learning).



The help pages have the following sections -- hopefully you can jump straight to
one that describes what you're looking for help with!

[TOC]

# I'm a beginner learning Python

We have lots of beginners on PythonAnywhere! Here's a very quick step-by-step tutorial you might want to start with:

<img alt="keyboard icon" src="https://www.pythonanywhere.com/static/glyphicons/glyphicons_268_keyboard_wireless@2x.png">
&nbsp; I want to start learning Python
<a href="https://www.pythonanywhere.com/task_helpers/start/1-start_python/">[account in US servers]</a>
<a href="https://eu.pythonanywhere.com/task_helpers/start/1-start_python/">[account in EU servers]</a>

And here are some common questions and guides for beginners:

  * [How can I use a specific version of Python with the "Save &amp; Run" button?](/pages/SaveAndRunPythonVersion)
  * [Installing new Python modules for yourself](/pages/InstallingNewModules)
  * [Using the file browser](/pages/FileBrowser)
  * [The file editor](/pages/FileEditor)
  * [Changing the font size in a PythonAnywhere console](/pages/ChangingFontSize)
  * [How do I share my code online?](/pages/ShareMyCodeOnline)
  * [What is a good tutorial for learning Python?](/pages/Learning)

<!-- TODO: how do I edit a file?  How do I run a script? -->


# I've got an existing web app that I'm trying to deploy

This section assumes you have started building a web app on your local PC, and you're now looking to deploy it to PythonAnywhere.

Here is a step-by-step tutorial that walks you through the general outline of how to set up an existing web app on PythonAnywhehre

<img alt="computer icon" src="https://www.pythonanywhere.com/static/glyphicons/glyphicons_137_computer_service@2x.png">
&nbsp;
I have built a web app on my local PC and want to deploy it on PythonAnywhere
<a href="https://www.pythonanywhere.com/task_helpers/start/4-deploy-local-web-app/">[account in US servers]</a>
<a href="https://eu.pythonanywhere.com/task_helpers/start/4-deploy-local-web-app/">[account in EU servers]</a>

And here are some popular how-to guides and help pages for common webapp issues:

  * [Can I use FTP/Filezilla? How should I upload my code to PythonAnywhere?](/pages/UploadingAndDownloadingFiles)
  * [Debugging import errors and sys.path issues in your WSGI file](/pages/DebuggingImportError)
  * [Using a virtualenv for your web app](/pages/Virtualenvs)
  * [How to use a custom domain for your web app](/pages/CustomDomains) (including CNAME setup)
  * [How to set up an HTTPS/SSL certificate for a custom domain](/pages/HTTPSSetup)
  * [How to force HTTPS on your web app](/pages/ForcingHTTPS)
  * [Troubleshooting DNS problems](/pages/TroubleshootingDNS)
  * [How to use our static files service, and why you might want to](/pages/StaticFiles)
  * [How to set environment variables in web apps](/pages/environment-variables-for-web-apps)
  * [How to handle slow/async work in a web app](/pages/AsyncInWebApps)
  * [How to point a new domain at an existing web app in the Web tab](/pages/UsingANewDomainForExistingWebApp)
  * [How to move a domain from one PythonAnywhere user account to another](/pages/MovingDomainToAnotherPythonAnywhereAccount)
  * [Using MySQL](/pages/UsingMySQL)
  * [I'm getting a 502 Bad Gateway error. How can I debug?](/pages/502BadGateway)
  * [My site is slow!](/pages/MySiteIsSlow)
  * [How to host a static site on PythonAnywhere](/pages/hosting-a-static-site)
  * [Using International Domain Names](/pages/InternationalDomainNames) -- that is, ones with non-ASCII/Unicode characters in them
  * [How do I create a web app that redirects from one domain to another?](/pages/RedirectWebApp)
  * [How many hits can my site handle?](/pages/HowManyHitsCanMySiteHandle) -- a guide to making sure that you have the right number of worker processes


And some tips for specific web frameworks:

  * Django
    * [Deploying an existing Django project on PythonAnywhere](/pages/DeployExistingDjangoProject)
    * [How can I use a more recent version of Django for a new project](/pages/VirtualEnvForNewerDjango)
    * [How to setup static files under Django](/pages/DjangoStaticFiles) -- STATIC_ROOT in settings.py, `collectstatic`, etc
    * [The Django admin's CSS isn't working](/pages/DjangoAdminCSSNotWorking)
    * [How to set SECRET_KEY via an environment variable](/pages/environment-variables-for-web-apps)
    * [Running Django code in consoles, scheduled and always-on tasks with custom management commands](/pages/DjangoManagementCommands)
    * [How to scale a Django Application on PythonAnywhere with Memcache](https://blog.memcachier.com/2018/10/15/django-on-pythonanywhere-tutorial/) (external link to Memcachier)

  * Flask
    * [A beginner's guide to building a simple database-backed Flask website on PythonAnywhere](http://blog.pythonanywhere.com/121/)
    * [General Flask tips, including avoiding app.run() and how to run database config with db.create_all()](/pages/Flask)
    * [Dealing with 504 or 502 errors in Flask applications](/pages/Flask504And502Errors)
    * [Using SQLAlchemy with MySQL](/pages/UsingSQLAlchemywithMySQL)
    * [How to scale a Flask Application on PythonAnywhere with Memcache](https://blog.memcachier.com/2018/10/01/flask-on-pythonanywhere-tutorial/) (external link to Memcachier)

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
    * [Using Dash](/pages/DashWSGIConfig)
    * [Using Jam.py](/pages/jampy)
    * [How to host a static site on PythonAnywhere](/pages/hosting-a-static-site)



# I'm looking at an error message in a console

Oh no!  Here's our most common explanations and solutions to console problems:

  * [I get "permission denied" when trying to pip install a new module](/pages/InstallingNewModules)
  * [Why do I get a "403 Forbidden" error when accessing a website from PythonAnywhere?](/pages/403ForbiddenError)
  * [I'm getting "no such file or directory"](/pages/NoSuchFileOrDirectory)
  * [LOAD DATA INFILE doesn't work](/pages/LoadDataInfile)
  * ["Disk Quota Exceeded" (running out of storage space / maxing out your quota)](/pages/DiskQuota)


Some technical problems with consoles that sometimes come up:

  * [I can't see what I'm typing in the console](/pages/ICantSeeWhatIAmTyping)
  * [The "Starting encrypted connection" message never disappears](/pages/StartingEncryptedConnection)


# I'm looking at an error message in my web app

If you haven't already, the first step is to look in your **error
log** -- you'll find a link to it on the **Web tab** ([account in US servers](https://www.pythonanywhere.com/web_app_setup/); [account in EU servers](https://eu.pythonanywhere.com/web_app_setup/)).
There's [more information about the error log here](/pages/InternalServerError).

Once you've done that, here are some solutions to common problems

  * [Debugging import errors and sys.path issues](/pages/DebuggingImportError)  <--  if you've just started setting up your app, chances are the answer is in here.
  * [Dealing with "there was an error reloading your web app" messages](/pages/ErrorReloadingWebApp)
  * [I'm getting a 502 Bad Gateway error. How can I debug?](/pages/502BadGateway)
  * [I'm getting a 400 Bad Request error from my Django app](/pages/Django400BadRequest)
  * [Debugging problems with static files (js, css) not loading](/pages/DebuggingStaticFiles)
  * [Fixing "OperationalError: 2006 MySQL server has gone away"](/pages/ManagingDatabaseConnections)
  * [Fixing "OperationalError: 1226 User has exceeded the max_user_connections resource](/pages/ManagingDatabaseConnections)
  * [I'm seeing lots of `GeneratorExit` or `OSError: write error` messages in my error log](/pages/GeneratorExit)



# I'm trying to figure out how to get a particular tool or feature to work

PythonAnywhere already has many of the Python modules that you might want to
use installed. There is a complete list of them available on our [Batteries
included page](https://www.pythonanywhere.com/batteries_included/)

Here are some guides for some of the common things people want to do:

  * [Installing new Python modules for yourself](/pages/InstallingNewModules)
  * [Changing your system image](/pages/ChangingSystemImage)
  * [Always-on tasks: how do I keep a console running forever? Or, how do I make a program that restarts automatically?](/pages/AlwaysOnTasks)
  * [How to I run an async task queue like celery?](/pages/AsyncInWebApps)
  * [Can I use matplotlib to generate graphs from my data?](/pages/MatplotLibGraphs)
  * [Can I use SMTP to send email on a Free account?](/pages/SMTPForFreeUsers)
  * [How do I solve authentication errors from Gmail when sending emails from my code?](/pages/GmailAppSpecificPasswords)
  * [How to force HTTPS on your web app](/pages/ForcingHTTPS)
  * [Using MySQL (including using MySQL with Python 3)](/pages/UsingMySQL)
  * [Backing up (and restoring) MySQL databases using mysqldump](/pages/MySQLBackupRestore)
  * [Setting the timezone for your code](/pages/SettingTheTimezone)
  * [Working with PDFs and converting document formats](/pages/PDF)
  * [Can I use IPv6?](/pages/IPv6)
  * [Can I use Pygame / Tkinter / turtle / GUI packages?](/pages/TkinterPygameEtc)
  * [Using Selenium](/pages/selenium)
  * [Using Playwright](/pages/Playwright)
  * [Does PythonAnywhere have an API?](/pages/API)
  * [What do I do if a server I want to connect to has an allowlist that only allows incoming connections from particular (static) IPs?](/pages/StaticIPForExternalAllowlists)
  * [How to I get Twilio to work?](/pages/TwilioBehindTheProxy)
  * Machine learning: [what to do if your website using Keras, TensorFlow or PyTorch doesn't work](/pages/MachineLearningInWebsiteCode)
  * [Fonts](/pages/Fonts)
  * [Using Cloudflare with PythonAnywhere](/pages/Cloudflare)
  * [Installing TA-Lib on PythonAnywhere](/pages/TaLib)


And here's some very brief FAQ answers about common requests:

  * **Can I use MongoDB**? It's not built in, but from a paid account you can use an external service like [mLab](https://mlab.com/).  Some [extra hints and tips on using Mongo here](/pages/MongoDB).
  * **Can I use an external MySQL service?** Probably not (on a free account), unless they have an HTTP api.
  * Can I use Redis?  Again, only via an external service like redislabs.  Although you can use redislite
  * Can I use websockets, or run my own socket server?  I'm afraid not --  we only support Python apps that implement the WSGI protocol
  * How do I reload my webapp automatically?  You can now use our [API](/pages/API) for this :)
  * [Which Python versions does PythonAnywhere support?](/pages/PythonVersions)



# I'm a teacher looking to use PythonAnywhere for education

Welcome!  We have lots of teachers and students on board.  Check out this page for an overview of our education-specific features:

  * [General info on our educational features](/pages/Education)


Or you can run through this step-by-step tutorial if you prefer:

<img alt="trophy icon" src="https://www.pythonanywhere.com/static/glyphicons/glyphicons_074_cup@2x.png">
&nbsp; I want to check out the Education Beta features
<a href="https://www.pythonanywhere.com/task_helpers/start/6-education/">[account in US servers]</a>
<a href="https://eu.pythonanywhere.com/task_helpers/start/6-education/">[account in EU servers]</a>

# A few other topics

  * [how to get SSH access to your account](/pages/SSHAccess)
  * [How to follow the Django Tutorial on PythonAnywhere](/pages/FollowingTheDjangoTutorial)
  * [I want to embed a live python console on my website](/pages/EmbeddedConsoles)
  * [How do I share my code online?](/pages/ShareMyCodeOnline)
  * [Getting the IP address of clients connecting to your web app](/pages/WebAppClientIPAddresses)
  * [How do I get streaming/buffering to work?](/pages/Buffering)
  * [How to use a virtualenv in an IPython Notebook](/pages/IPythonNotebookVirtualenvs)
  * [What are these virtualenv things, anyway?](/pages/VirtualenvsExplained)
  * [How do I completely delete my account?](/pages/DeleteAccount)



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
  * [Browser extensions that are known to cause problems with PythonAnywhere consoles](/pages/ProblematicExtensions)

Web apps:

  * [How to create a web application on PythonAnywhere](/pages/WebAppBasics)
  * [Reloading the web application after you've made changes](/pages/ReloadWebApp)
  * [Rebuilding a Virtualenv](/pages/RebuildingVirtualenvs)


Databases:

  * [Databases available on PythonAnywhere](/pages/KindsOfDatabases)
  * [Activating a Postgres server](/pages/Postgres)
  * [Configuring postgres for your app (eg Django)](/pages/PostgresGettingStarted)
  * [Creating Postgres backups](/pages/RegularPostgresBackups)
  * [Increasing the number of connections for your Postgres server](/pages/PostgresConnections)
  * [Connecting to Microsoft SQL Server](/pages/MSSQLServer)
  * [How do I find out how large my MySQL database is?](/pages/MySQLDatabaseSize)
  * [Migrating a web2py app from SQLite to MySQL](/pages/MigatingWeb2pyFromSQLiteToMySQL)
  * [Database character sets (UTF8/Unicode etc)](/pages/DatabaseCharacterSets)
  * [Importing a database you have stored on your own machine to PythonAnwyhere](/pages/ImportingYourLocalDatabaseToPythonAnywhere)
  * [Accessing your MySQL database from outside PythonAnywhere](/pages/AccessingMySQLFromOutsidePythonAnywhere)
  * [Accessing your PostgreSQL database from outside PythonAnywhere](/pages/AccessingPostgresFromOutsidePythonAnywhere)


Scheduled tasks (similar to cron):

  * [Setting up scheduled tasks](/pages/ScheduledTasks)


Other Languages:

  * [Setting up Haskell and creating a new Cabal package](/pages/Haskell)
  * [Setting up a Node project](/pages/Node)
  * [Testing a simple Javascript project using Jasmine](/pages/jasmine-tests-for-js-projects)



# A few other step-by-step guides

<img alt="fishies icon" src="https://www.pythonanywhere.com/static/glyphicons/glyphicons_254_fishes@2x.png">
&nbsp; I want to follow the Django Tutorial
<a href="https://www.pythonanywhere.com/task_helpers/start/2-following-the-django-tutorial/">[account in US servers]</a>
<a href="https://eu.pythonanywhere.com/task_helpers/start/2-following-the-django-tutorial/">[account in EU servers]</a>

<img alt="cloud icon" src="https://www.pythonanywhere.com/static/glyphicons/glyphicons_232_cloud@2x.png">
&nbsp; I want to create a web application
<a href="https://www.pythonanywhere.com/task_helpers/start/3-web_app/">[account in US servers]</a>
<a href="https://eu.pythonanywhere.com/task_helpers/start/3-web_app/">[account in EU servers]</a>

<img alt="github icon" src="https://www.pythonanywhere.com/static/glyphicons/glyphicons_341_github@2x.png">
&nbsp; I want to clone and hack on my GitHub project
<a href="https://www.pythonanywhere.com/task_helpers/start/5-github/">[account in US servers]</a>
<a href="https://eu.pythonanywhere.com/task_helpers/start/5-github/">[account in EU servers]</a>

# Security

* [Securing your PythonAnywhere account](/pages/SecuringYourAccount)
* [Details on the PythonAnywhere Bug Bounty](/pages/BugBounty)
