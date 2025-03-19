<!--
.. title: Virtualenvs for newer Django
.. slug: VirtualEnvForNewerDjango
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

## Guide to setting up a virtualenv for PythonAnywhere Web apps

A [virtualenv](/pages/VirtualenvsExplained) is a way to have your own private Python environment that has
different versions of packages to the system default. You can have many
virtualenvs, each with its own versions of installed packages. On
PythonAnywhere, this is a great way to use newer (or older) versions of
software than the ones we have installed.

One reason you might want to do this is to use a newer version of Django. For
example, in our "innit" system image, our
[system default is 5.1.3](https://www.pythonanywhere.com/batteries_included/),
but the latest version released by Django Team (as of March 2025) is 5.1.7. If you want to upgrade to
that, a virtualenv makes it easy.

> If you're on an older system image, you'll be on an even earlier version of
> Django, so this guide is even more pertinent.  You can also
> [update your system image to a more recent one](/pages/ChangingSystemImage),
> though.


### Instructions

Log in to PythonAnywhere, and create a new Web app:

* Go to the "Web" page.
* Select the "Add a new web app" option on the left-hand side.
* If you have a Web Developer account, specify the domain you want your web app to appear on, then click "Next"
* Select the "Manual configuration" option from the list.
* Click "Next", and wait for the system to tell you that the web app has been created.

Now you can check that you have a web app -- go to *yourusername*`.pythonanywhere.com` in your browser to see the simple
site we generate for you.

You may have noticed a *Virtualenv path* option on the "Web" page. Let's go and create a virtualenv, so we have something to put in there.


### Creating the virtualenv and installing Django

Go to the "Consoles" tab and start a *Bash console*

```bash
14:50 ~ $ mkvirtualenv --python=python3.13 myproject
```

You can check it works -- the prompt should gain the `(myproject)` prefix, and you can check `which pip` returns the
virtualenv pip:

```bash
(myproject) 14:51 ~ $ which pip
/home/myusername/.virtualenvs/myproject/bin/pip
```

If it hasn't, you'll need to activate the virtualenv, like this:

```bash
workon myproject
```

You'll need to do this in any bash console when you're trying to install things to your virtualenv or run `manage.py`,
otherwise you'll be trying to make changes to the system environment instead of your virtualenv.

Now install Django:

```bash
(myproject) 14:51 ~ $ pip install django
```

Now you can check it worked:

```bash
(myproject) 15:02 ~ $ which django-admin
/home/myusername/.virtualenvs/myproject/bin/django-admin
(myproject) 15:02 ~ $ django-admin --version
5.1.7
```

Start a new django project:

```bash
(myproject) 15:02 ~ $ django-admin.py startproject mysite
```

Check it worked:

```bash
(myproject) 15:02 ~ $ tree mysite
mysite
── manage.py
└── mysite
    ├── __init__.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```


### Using the virtualenv in your web app

Now go back to the "Web" page and edit the WSGI file for your web app (there's
a link on the page) and delete everything except the Django section, and
then uncomment the Django section. Your WSGI file should look something like
this:

```python
# +++++++++++ DJANGO +++++++++++
# To use your own django app use code like this:
import os
import sys

# assuming your django settings file is at '/home/myusername/mysite/mysite/settings.py'
path = '/home/myusername/mysite'
if path not in sys.path:
    sys.path.insert(0, path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

# serve django via WSGI
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
```

Then, back on the "Web" page, edit the path to your virtualenv in the
Virtualenv section. You can specify the full path,
`/home/myusername/.virtualenvs/myproject`, or just the short name of the
virtualenv, `myproject`, and the system will automatically expand it to the
full path after you submit it.

Save it, then go and hit the **Reload** button for your site.


### Checking it worked.

Go to site -- you should see the Django "it worked!" page.

You're all set up, and now you can use your virtualenv ![:\)](/smile.png)


### Extra packages

Don't forget, the virtualenv has its own set of installed packages -- so if you
want to use something you'll need to `pip install` it. A common example for
Django is the Python MySQL library, which requires the package `mysqlclient`:

```bash
(myproject) 15:12 ~/mysite $ pip install mysqlclient
```

### Static files

See our [help page on setting up static files for Django](https://help.pythonanywhere.com/pages/DjangoStaticFiles)


### Developing with your virtualenv

Remember: whenever you want to get back and work on your virtualenv, you need to make sure it's active -- if you're
opening a new console, for example.

Look out for the `(myproject)` prefix at the command-line.

It's also well worth checking `which pip` to make sure you're using the virtualenv pip when installing.

If in doubt, run:

```bash
(myproject) 17:02 ~ $ source virtualenvwrapper.sh
```

To switch on virtualenvwrapper (you can add this to your `.bashrc` if it's not there already)

And

```bash
17:02 ~ $ workon myproject
```

to switch to working on your virtual environment.
