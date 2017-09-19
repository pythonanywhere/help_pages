
<!--
.. title: VirtualEnv for newer Django
.. slug: VirtualEnvForNewerDjango
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->





##Guide to setting up a virtualenv for PythonAnywhere Web apps


A virtualenv is a way to have your own private Python environment that has
different versions of packages to the system default. You can have many
virtualenvs, each with its own versions of installed packages. On
PythonAnywhere, this is a great way to use newer (or older) versions of
software than the ones we have installed.

One reason you might want to do this is to use a newer version of Django. For
example (at the time of writing) our system default is 1.10, but the Django
team had just released a point update to 1.10.2.  If you want to upgrade to 
that, or later to 1.11, a virtualenv makes it easy.

*(If you're on our old 
[system image](https://www.pythonanywhere.com/batteries_included/), you'll be on an
even earlier version of Django, so this guide is even more pertinent.)*



###Instructions


Log in to PythonAnywhere, and create a new Web app:

  * Go to the "Web" tab.
  * Select the "Add a new web app" option on the left-hand side.
  * If you have a Web Developer account, specify the domain you want your web app to appear on, then click "Next"
  * Select the "Manual configuration" option from the list.
  * Click "Next", and wait for the system to tell you that the web app has been created.

Now you can check that you have a web app -- go to *yourusername*.pythonanywhere.com in your browser to see the simple site we generate for you.

You may have noticed a *Virtualenv path* option. Let's go and create a virtualenv, so we have something to put in there.


###Creating the virtualenv and installing (eg) django


Go to the "Consoles" tab and start a *Bash console*

    14:50 ~ $ mkvirtualenv --python=/usr/bin/python3.6 myproject


***TIP: if you want to use Python 2 for your virtualenv, use `mkvirtualenv --python=/usr/bin/python2.7 myproject`***

***TIP: if you see an error saying `mkvirtualenv: command not found`, check out [InstallingVirtualenvWrapper](/pages/InstallingVirtualenvWrapper).***

You can check it works -- the prompt should gain the `(myproject)` prefix, and you can check `which pip` returns the virtualenv pip:

    (myproject)14:51 ~ $ which pip
    /home/myusername/.virtualenvs/myproject/bin/pip


If it hasn't, you'll need to activate the virtualenv, like this:

    workon myproject


You'll need to do this in any bash console when you're trying to install things to your virtualenv or run `manage.py`, otherwise you'll be trying to make changes to the system environment instead of your virtualenv.

Now install Django:

    (myproject)14:51 ~ $ pip install django


(apologies if this takes a long time. We're working on speeding up disk I/O)

Now you can check it worked:

    (myproject)15:02 ~ $ which django-admin.py
    /home/myusername/.virtualenvs/myproject/bin/django-admin.py
    (myproject)15:02 ~ $ django-admin.py --version
    1.10.2


Start a new django project:

    (myproject)15:02 ~ $ django-admin.py startproject mysite


Check it worked:

    (myproject)15:02 ~ $ tree mysite
    mysite
    ├── manage.py
    └── mysite
        ├── __init__.py
        ├── settings.py
        ├── urls.py
        └── wsgi.py


###Using the virtualenv in your web app


Now go back to the **Web** tab and edit the WSGI file for your web app (There's
a link on the web app tab) and delete everything except the Django section and
then uncomment the Django section. Your WSGI file should look something like
this:

    # +++++++++++ DJANGO +++++++++++
    # To use your own django app use code like this:
    import os
    import sys

    # assuming your django settings file is at '/home/myusername/mysite/mysite/settings.py'
    path = '/home/myusername/mysite'
    if path not in sys.path:
        sys.path.append(path)

    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'

    # serve django via WSGI
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()


Then, back on the web tab itself, edit the path to your virtualenv in the
Virtualenv section. You can specify the full path,
*/home/myusername/.virtualenvs/myproject*, or just the short name of the
virtualenv, *myproject*, and the system will automatically expand it to the
full path after you submit it.

Save it, then go and hit the **Reload** button for your domain.


###Checking it worked.


Go to site -- you should see the Django "it worked!" page.

You're all set up, and now you can use your virtualenv ![:\)](/smile.png)


###Extra packages


Don't forget, the virtualenv has its own set of installed packages -- so if you
want to use something you'll need to `pip install` it. A common example for
Django is the Python MySQL library.

For Python 2.7 you'll need to install `mysql-python`:

    (myproject)15:12 ~/mysite $ pip install mysql-python

For Python 3.x you need a different package, `mysqlclient`:

    (myproject)15:12 ~/mysite $ pip install mysqlclient



###Static files


See our [help page on setting up static files for django](https://help.pythonanywhere.com/pages/DjangoStaticFiles)



###Developing with your virtualenv


Remember: whenever you want to get back and work on your virtualenv, you need to make sure it's active -- if you're opening a new console, for example.

Look out for the little `(myproject)` prefix at the command-line.

It's also well worth checking `which pip` to make sure you're using the virtualenv pip when installing.

If in doubt, run:

    (myproject)17:02 ~ $ source virtualenvwrapper.sh


To switch on virtualenvwrapper (you can add this to your `.bashrc` if it's not there already)

And

    17:02 ~ $ workon myproject


to switch to working on your virtual environment.
