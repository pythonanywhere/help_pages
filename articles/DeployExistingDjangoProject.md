
<!--
.. title: Deploying an existing Django project on PythonAnywhere
.. slug: DeployingExistingDjangoProject
.. date: 2016-02-10 12:35:28 UTC
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->




# How to deploy an existing Django Project on PythonAnywhere.

Here's the overview:

1. Upload your code to PythonAnywhere
2. Set up a virtualenv and install django and any other requirements
3. Set up your web app using manual config and your WSGI file.
4. Add any other setup (static files, environment variables etc)


## Uploading your code to PythonAnywhere

Assuming your code is already on a code sharing site like GitHub or Bitbucket, you
can just clone it from a **Bash Console**:

```bash
# for example
$ git clone https://github.com/myusername/myproject.git
```

That's the solution we recommend, but there are a few different methods documented on the [Uploading code](/pages/FTP) page,



## Create a virtualenv and install Django and any other requirements

In your Bash console, create a virtualenv, naming it after your project, and choosing the version of Python you want to use:

```bash
$ mkvirtualenv --python=/usr/bin/python3.4 mysite-virtualenv
(mysite-virtualenv)$ pip install django
# or, if you have a requirements.txt:
(mysite-virtualenv)$ pip install -r requirements.txt
```

**Warning**: *django may take a long time to install.  PythonAnywhere has very fast internet, but the filesystem access can be slow, and django creates a lot of small files during its installation.  Thankfully you only have to do it once!*

*TIP**: *if you see an error saying `mkvirtualenv: command not found`, check out [InstallingVirtualenvWrapper](/pages/InstallingVirtualenvWrapper).*


## Setting up your Web app and WSGI file

At this point, you need to be armed with 3 pieces of information:

1. The path to your django project's top folder -- the folder that contains "manage.py", eg */home/myusername/mysite*
2. The name of your project (that's the name of the folder that contains your settings.py), eg "mysite"
3. The name of your virtualenv, eg "mysite-virtualenv"

#### Create a Web app with Manual Config

Head over to the **Web tab** and create a new web app, choosing the "Manual Configuration" option and the right version of Python (the same one you used to create your virtualenv).


#### Enter your virtualenv name

Once that's done, **enter the name of your virtualenv** in the Virtualenv section on the web tab and click OK.  You can just use its short name "mysite-virtualenv", and it will automatically complete to its full path in /home/username/.virtualenvs.

#### Edit your WSGI file

Next, click through to the WSGI file from the link on the web tab.

Delete everything except the Django section and then uncomment that section. Your WSGI file should look something like this: 

```python
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/myusername/mysite/mysite/settings.py'
path = '/home/myusername/mysite'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

## Uncomment the lines below depending on your Django version
###### then, for django >=1.5:
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
###### or, for older django <=1.4
#import django.core.handlers.wsgi
#application = django.core.handlers.wsgi.WSGIHandler()
```


* Be sure to substitute the correct path to your project, the folder that contains manage.py, which you noted above.
* And also make sure you put the correct value for `DJANGO_SETTINGS_MODULE`.
* This guide assumes you're using a recent version of django, so leave the old `wsgi.WSGIHandler()` code commented out, or better still, delete it.

Save it, then go and hit the **Reload** button for your domain. 


## Checking it worked.

Go visit your site, it should be live!


## What to do if you see any errors.

First, check your **error log**.  You'll find a link to it on your web tab.  

Then check out [the "debugging web app errors" section](/pages/#im-looking-at-an-error-message-in-my-web-app) from our help topics, particularly [this article on sys.path and import errors](/pages/DebuggingImportError)


## Additional configuration:

Check out [the "existing web app"
section](/pages/#ive-got-an-existing-web-app-that-im-trying-to-deploy) in our
help pages, particularly

* [Configuring static files with django](/pages/DjangoStaticFiles)
* [Setting environment variables](/pages/DjangoStaticFiles) if you need them for things like `SECRET_KEY`

