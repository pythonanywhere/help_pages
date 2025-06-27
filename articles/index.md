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

See details of our education features: [PythonAnywhere Education beta](/pages/Education)


The help pages below have the following sections -- hopefully you can jump straight to
one that describes what you're looking for help with!


[TOC]


## I'm a beginner learning Python

New to Python? Start here for guides on learning Python programming and getting familiar with the PythonAnywhere platform.

<img alt="keyboard icon" src="https://www.pythonanywhere.com/static/glyphicons/glyphicons_268_keyboard_wireless@2x.png">
&nbsp; I want to start learning Python
<a href="https://www.pythonanywhere.com/task_helpers/start/1-start_python/">[account in US servers]</a>
<a href="https://eu.pythonanywhere.com/task_helpers/start/1-start_python/">[account in EU servers]</a>

* [Courses and other learning materials](/pages/Learning)
* [Installing new Python modules for yourself](/pages/InstallingNewModules)
* [How can I use a specific version of Python with the "Save & Run" button?](/pages/SaveAndRunPythonVersion)
* [Using the file browser](/pages/FileBrowser)
* [The file editor](/pages/FileEditor)
* [Changing the font size in a PythonAnywhere console](/pages/ChangingFontSize)
* [How do I share my code online?](/pages/ShareMyCodeOnline)

## Web Applications and Hosting

Everything you need to know about creating, configuring, and managing web applications on PythonAnywhere. This covers all major Python web frameworks and deployment options.

<img alt="computer icon" src="https://www.pythonanywhere.com/static/glyphicons/glyphicons_137_computer_service@2x.png">
&nbsp;
I have a web app on my local PC and want to deploy it on PythonAnywhere
<a href="https://www.pythonanywhere.com/task_helpers/start/4-deploy-local-web-app/">[account in US servers]</a>
<a href="https://eu.pythonanywhere.com/task_helpers/start/4-deploy-local-web-app/">[account in EU servers]</a>

### Basic Web App Setup

* [How to create a web application on PythonAnywhere](/pages/WebAppBasics)
* [Deploying an existing Django project on PythonAnywhere](/pages/DeployExistingDjangoProject)
* [How to host a static site on PythonAnywhere](/pages/HostingAStaticSite)

### Web App Configuration and  Management

* [Reloading the web application after you've made changes](/pages/ReloadWebApp)
* [Dealing with "there was an error reloading your web app" messages](/pages/ErrorReloadingWebApp)
* [How do I create a web app that redirects from one domain to another?](/pages/RedirectWebApp)
* [How to point a new domain at an existing web app in the Web tab](/pages/UsingANewDomainForExistingWebApp)
* [Global State and Web Apps](/pages/GlobalStateAndWebApps)

### Django

* [How to follow the Django Tutorial on PythonAnywhere](/pages/FollowingTheDjangoTutorial)
* [How to setup static files under Django](/pages/DjangoStaticFiles)
* [The Django admin's CSS isn't working](/pages/DjangoAdminCSSNotWorking)
* [Running Django code in consoles, scheduled and always-on tasks with custom management commands](/pages/DjangoManagementCommands)
* [I'm getting a 400 Bad Request error from my Django app](/pages/Django400BadRequest)
* [How can I use a more recent version of Django for a new project](/pages/VirtualEnvForNewerDjango)

### Flask
* [General Flask tips, including avoiding app.run() and how to run database config with db.create_all()](/pages/Flask)
* [Dealing with 504 and 502 errors in Flask applications](/pages/Flask504And502Errors)
* [Using Flask's send_file function with BytesIO](/pages/FlaskSendFileAndBytesIO)

### Web2py

* [How do I change my admin password in Web2py?](/pages/Web2pyAdminPassword)
* [Admin is disabled because insecure channel](/pages/AdminIsDisabledBecauseInsecureChannel)
* [Web2py: how to do a fake migration to change database hostname](/pages/Web2pyFakeMigration)
* [How do I run the web2py scheduler?](/pages/Web2pyScheduler)
* [Migating Web2py from SQLite to MySQL](/pages/MigatingWeb2pyFromSQLiteToMySQL)
* [How do I set up different apps for different domains in Web2py?](/pages/MultipleDomainsWeb2py)

### Other Frameworks

* [Using Dash](/pages/DashWSGIConfig)
* [Using CherryPy](/pages/UsingCherryPy)
* [Using Tornado (WSGI-only mode)](/pages/UsingTornado)
* [Using Jam.py](/pages/Jampy)
* [Using Web.py](/pages/WebDotPyWSGIConfig)
* [How to use Mezzanine on PythonAnywhere](/pages/HowtouseMezzanineonPythonAnywhere)
* [How to connect production React frontend with a Python backend](/pages/React)
* [How to connect production Vue frontend with a Python backend](/pages/Vue)

### ASGI (async) sites (beta)
* [Using the API to run ASGI sites on PythonAnywhere (beta)](/pages/ASGIAPI)
* [Deploying ASGI sites on PythonAnywhere (beta)](/pages/ASGICommandLine)
* [Deploying Flask sites on PythonAnywhere with our experimental website system](/pages/FlaskWithTheNewWebsiteSystem)
* [Deploying Flask-SocketIO sites on PythonAnywhere (beta)](/pages/FlaskSocketIO)
* [Deploying Streamlit apps on PythonAnywhere (beta)](/pages/Streamlit)

## Static Files and Content Delivery

How to serve static files (CSS, JavaScript, images) efficiently and troubleshoot common static file issues.

* [How to use our static files service, and why you might want to](/pages/StaticFiles)
* [Debugging problems with static files (js, css) not loading](/pages/DebuggingStaticFiles)
* [Using Cloudflare with PythonAnywhere](/pages/Cloudflare)

## Domains and HTTPS

Setting up custom domains, SSL certificates, and HTTPS for your web applications.

* [How DNS works: a beginner's guide](/pages/DNSPrimer)
* [Troubleshooting DNS problems](/pages/TroubleshootingDNS)
* [How to use a custom domain for your web app](/pages/CustomDomains)
* [Using Custom PythonAnywhere Subdomains](/pages/CustomPythonAnywhereSubdomains)
* [Naked domains](/pages/NakedDomains)
* [How to move a domain from one PythonAnywhere user account to another](/pages/MovingDomainToAnotherPythonAnywhereAccount)
* [Using International Domain Names](/pages/InternationalDomainNames)
* [How to set up an autorenewing HTTPS/SSL certificate for a custom domain](/pages/HTTPSSetup)
* [How to set up and install a custom HTTPS/SSL certificate for your custom domain](/pages/HTTPSCustomCerts)
* [How to force HTTPS on your web app](/pages/ForcingHTTPS)
* [TLS version support](/pages/TLSVersionSupport)

## Web-Related Errors and Troubleshooting

Common web application errors and how to debug them, including HTTP status codes and framework-specific issues.

* [Why do I get a "403 Forbidden" or "[Errno 111] Connection refused" error when accessing a website from PythonAnywhere?](/pages/403ForbiddenError)
* [I'm getting a 502 Bad Gateway error. How can I debug?](/pages/502BadGateway)
* [I'm getting an Internal Server Error on my website](/pages/InternalServerError)
* [How to handle slow/async work in a web app](/pages/AsyncInWebApps)
* [Getting the IP address of clients connecting to your web app](/pages/WebAppClientIPAddresses)

## Databases

Setting up and managing MySQL, PostgreSQL, and other databases on PythonAnywhere, including connections, backups, and external access.

* [Fixing "OperationalError: 2006 MySQL server has gone away" and "Too many connections"](/pages/ManagingDatabaseConnections)

### MySQL

* [Using MySQL](/pages/UsingMySQL)
* [Accessing your MySQL database from outside PythonAnywhere](/pages/AccessingMySQLFromOutsidePythonAnywhere)
* [Backing up (and restoring) MySQL databases using mysqldump](/pages/MySQLBackupRestore)
* [How do I find out how large my MySQL database is?](/pages/MySQLDatabaseSize)
* [Using SQLAlchemy with MySQL](/pages/UsingSQLAlchemywithMySQL)
* [LOAD DATA INFILE doesn't work](/pages/LoadDataInfile)
* [Importing a database you have stored on your own machine to PythonAnwyhere](/pages/ImportingYourLocalDatabaseToPythonAnywhere)

### PostgreSQL

* [Activating a Postgres server](/pages/Postgres)
* [Accessing your PostgreSQL database from outside PythonAnywhere](/pages/AccessingPostgresFromOutsidePythonAnywhere)
* [Creating Postgres backups](/pages/RegularPostgresBackups)
* [Configuring postgres for your app (eg Django)](/pages/PostgresGettingStarted)
* [Increasing the number of connections for your Postgres server](/pages/PostgresConnections)
* [Postgres Shared Memory Error](/pages/PostgresSharedMemory)

### Other Databases

* [Databases available on PythonAnywhere](/pages/KindsOfDatabases)
* [Database character sets (UTF8/Unicode etc)](/pages/DatabaseCharacterSets)
* [Using MongoDB on PythonAnywhere](/pages/MongoDB)
* [Connecting to Microsoft SQL Server](/pages/MSSQLServer)


## Virtualenvs and Package Management

Managing Python versions, virtual environments, and packages to isolate your project dependencies.

* [What are these virtualenv things, anyway?](/pages/VirtualenvsExplained)
* [Which Python versions does PythonAnywhere support?](/pages/PythonVersions)
* [Using a virtualenv for your web app](/pages/VirtualEnvForWebsites)
* [Rebuilding a Virtualenv](/pages/RebuildingVirtualenvs)
* [How to use a virtualenv in an Jupyter Notebook](/pages/IPythonNotebookVirtualenvs)
* [Python 3.7 virtualenvs on the "innit" system image](/pages/Python37VirtualenvOnInnit)
* [Using conda](/pages/Conda)

## Consoles

Using PythonAnywhere's browser-based consoles and SSH access for command-line development.

* [Changing a console's name](/pages/ChangingConsolesName)
* [Types of PythonAnywhere consoles](/pages/TypesOfConsoles)
* [I want to embed a live python console on my website](/pages/EmbeddedConsoles)
* [The "Starting encrypted connection" message never disappears](/pages/StartingEncryptedConnection)

## File Management and Development Tools

Uploading, downloading, and managing your code files and development workflow on PythonAnywhere.

* [Can I use FTP/Filezilla? How should I upload my code to PythonAnywhere?](/pages/UploadingAndDownloadingFiles)
* [Copying and pasting in PythonAnywhere consoles](/pages/CopyAndPaste)
* [Using external version control systems](/pages/ExternalVCS)

## Scheduled Tasks and Always-On Tasks

Running Python scripts on a schedule or keeping processes running continuously in the background.

* [Setting up scheduled tasks](/pages/ScheduledTasks)
* [Always-on tasks: how do I keep a console running forever? Or, how do I make a program that restarts automatically?](/pages/AlwaysOnTasks)

## API and Integration

Using PythonAnywhere's API to programmatically manage your account and integrate with external development tools.

* [Does PythonAnywhere have an API?](/pages/API)
* [Getting your API token](/pages/GettingYourAPIToken)
* [Integrating a development environment with PythonAnywhere](/pages/IntegratingWithPythonAnywhere)

## System Configuration and Settings

Configuring your PythonAnywhere environment, including system images, timezones, and environment variables.

* [Can I edit my config files?](/pages/ConfigFiles)
* [Changing your system image](/pages/ChangingSystemImage)
* [How to set environment variables in web apps](/pages/EnvironmentVariables)
* [Setting the timezone for your code](/pages/SettingTheTimezone)
* [Fonts](/pages/Fonts)

## Resource Management and Performance

Understanding and managing your account's resource limits, including disk space, CPU, and RAM usage.

* ["Disk Quota Exceeded" (running out of storage space / maxing out your quota)](/pages/DiskQuota)
* [RAM limits](/pages/RAMLimit)
* [What are CPU-seconds?](/pages/WhatAreCPUSeconds)
* [My site is slow!](/pages/MySiteIsSlow)
* [How many hits can my site handle?](/pages/HowManyHitsCanMySiteHandle)
* [How do I get streaming/buffering to work?](/pages/Buffering)

## Account Management and Security

Managing your PythonAnywhere account, security settings, and account deletion.

* [Securing your PythonAnywhere account](/pages/SecuringYourAccount)
* [How do I completely delete my account?](/pages/DeleteAccount)
* [How do I solve authentication errors from Gmail when sending emails from my code?](/pages/GmailAppSpecificPasswords)
* [Details on the PythonAnywhere Bug Bounty](/pages/BugBounty)

## Networking and External Access

Configuring network access, static IPs, SSH, and external connections for your applications.

* [How to get SSH access to your account](/pages/SSHAccess)
* [Can I use SMTP to send email on a Free account?](/pages/SMTPForFreeUsers)
* [Requesting Allowlist additions](/pages/RequestingAllowlistAdditions)
* [What do I do if a server I want to connect to has an allowlist that only allows incoming connections from particular (static) IPs?](/pages/StaticIPForExternalAllowlists)
* [IPv6](/pages/IPv6)

## Third-Party Services, Libraries and Languages

Using external services and specialized Python libraries with your PythonAnywhere applications.

### Web Scraping and Automation

* [Using Selenium](/pages/Selenium)
* [Using Playwright](/pages/Playwright)
* [Can I use matplotlib to generate graphs from my data?](/pages/MatplotLibGraphs)
* [Machine learning in website code](/pages/MachineLearningInWebsiteCode)
* [Installing TA-Lib on PythonAnywhere](/pages/TaLib)
* [How to I get Twilio to work?](/pages/TwilioBehindTheProxy)
* [Working with PDFs and converting document formats](/pages/PDF)
* [Using NVM to get the most up-to-date version of node](/pages/Node)
* [Testing a simple Javascript project using Jasmine](/pages/JasmineTestsForJavaScript)
* [Haskell](/pages/Haskell)
* [Can I use Pygame / Tkinter / turtle / GUI packages?](/pages/TkinterPygameEtc)
* [Compiling C Programs](/pages/CompilingCPrograms)

## General Error Handling and Troubleshooting

Common errors and troubleshooting guides for issues that can occur across different parts of the PythonAnywhere platform.

* [Debugging import errors and sys.path issues in your WSGI file](/pages/DebuggingImportError)
* [I'm getting "no such file or directory"](/pages/NoSuchFileOrDirectory)
* [I can't see what I'm typing in the console](/pages/ICantSeeWhatIAmTyping)
* [Typing problems international](/pages/TypingProblemsInternational)
* [Notebook authentication error](/pages/NotebookAuthenticationError)
* [I'm seeing lots of `GeneratorExit` or `OSError: write error` messages in my error log](/pages/GeneratorExit)
* [Browser extensions that are known to cause problems with PythonAnywhere consoles](/pages/ProblematicExtensions)
