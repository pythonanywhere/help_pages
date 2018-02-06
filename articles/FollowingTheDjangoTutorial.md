
<!--
.. title: Following the official Django Tutorial on PythonAnywhere
.. slug: FollowingTheDjangoTutorial
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



We &lt;3 Django at PythonAnywhere, we use it ourselves. Their tutorial is excellent, but there's a couple of small things that are different about the PythonAnywhere environment, compared to a regular PC.

This guides pertains to the tutorial for Django 1.7: <https://docs.djangoproject.com/en/1.7/intro/tutorial01/> (but there should only be minor differences for 1.8)

This document is not a replacement for the official django tutorial, instead, it's meant to be a companion guide -- the django tutorial is meant to be your primary guide, but when you read each section of the django tutorial, you should also take a look at the corresponding section notes in this guide, for additional instructions.

So we recommend you keep both the django tutorial and this page open side-by-side as you go through them.


##Part 1 (project setup and the models API)



###Creating a virtualenv and Installing Django into it


The preinstalled versions of Django on PythonAnywhere are a little out of date, but you can use a *virtualenv* to install your own versions. We'll use a nifty helper tool called virtualenvwrapper. Open up a **Bash Console** and:

    mkvirtualenv django17 --python=/usr/bin/python3.6
    pip install django ## this may take a couple of minutes


  * TIP: *if you see an error saying mkvirtualenv: command not found, check out [InstallingVirtualenvWrapper](/pages/InstallingVirtualenvWrapper)*.

Once you've created your virtualenv, you'll be able to see that it's active because your command prompt, which normally says something like `17:18 ~ $` will get prefixed with a little `(django17)`, like this:

    (django17)17:18 ~ $


***--&gt; Always make sure your virtualenv is active when working on the django tutorial***

If you need to reactivate it later, maybe if you close your bash console and open a new one, the command is:

    workon django17


It's probably a good idea to keep a bash console open at all times in one browser tab, with the virtualenv activated, so you can flick back and forth.


####Checking the django installation


The first command the tutorial asks you to run is to check the installed version:

    python -c "import django; print(django.get_version())"
    # This should show something like 1.7.1.
    # If it shows anything else, you've probably forgotten to activate your virtualenv!



###Creating a project, and viewing files


After you run the `startproject` command, you can take a look around the files in your project using our file browser and built-in browser-based editor. Open a new browser tab and go to the **Files** tab, then navigate to your new "mysite" folder.



###(not) the Development server: setting up your web app on the Web tab


Don't try and run the Django development server on [PythonAnywere](https://www.pythonanywhere.com/). It won't work, because our console servers aren't the same as our web servers.

Instead, open up a third browser tab and go to our **Web** tab. Click **Add a
new web app**, choose **Manual configuration** and then **Python 3.6**. When
you hit next, you'll be on your web app configuration page, and it's probably a
good idea to keep this tab open in your browser at all times too, so that you
can easily jump back to it, and hit reload on your web app, or find your log
files, or whatever it may be.

Go to the *Virtualenv* section and enter the path to your virtualenv, something like this: */home/myusername/.virtualenvs/django17*

Then, find the link to **edit your wsgi file**, scroll through it, and uncomment the parts that pertain to django -- something like this:


    :::python
    import os
    import sys

    path = '/home/yourusername/mysite'
    if path not in sys.path:
        sys.path.append(path)
    os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()



Save the file, then go back to the **Web** tab and hit the **Reload** button. You'll then be able to click on the link to your site, to see the Django "Welcome" site -- it's live and on the Internet!


####Reloading to see changes


From this point on, whenever you make changes to files in your django project, you'll need to hit "Reload" on the web tab to publish them and make them live on the actual site.


##Part 2 (database setup & the admin site)


###Database setup and settings.py


For example, the next thing the tutorial wants you to do is edit `settings.py`. Navigate to it in the files browser, and click on it to open up our editor.

You will need to tell Django what site it's working for by finding `ALLOWED_HOSTS` in `settings.py` and editing it like this:

    :::python
    ALLOWED_HOSTS = ['<your_username>.pythonanywhere.com']



If you are using your own domain name, put that in the list instead.

We support different databases, but using SQlite, the default, is probably simplest at this stage. You can change your `TIME_ZONE` setting as they suggest if you like though.

  * TIP: *the links to the documentation in the comments in settings.py should point to the same django version as your virtualenv, 1.7. If they don't, then you probably accidentally ran the `startproject` command without activating the virtualenv. Probably best to delete the whole `mysite` directory, make sure your virtualenv is active, and run `startproject again`.*.

Then, run the `python manage.py migrate` command back in your Bash console.

    (django17)$ cd mysite  #  cd into the directory that contains manage.py if you haven't already
    (django17)$ python manage.py migrate



###(do not) Start the development server


Remember, don't use `runserver` and *localhost:8000* on PythonAnywhere. Instead, go back to your **Web** tab, and hit reload on your web app. You will then be able to go to *your-username.pythonanywhere.com/admin* and see the admin site up and running...


###Creating models


When you start the polls app, check out the `tree` command to see the directory tree...

    python manage.py startapp polls
    tree


Then, when you want to edit *polls/models.py*, click through to it using the **Files** tab...


###Playing with the API


All of this should work fine in your Bash console. If you want a better interactive interpreter for `manage.py shell`, do a

    pip install ipython



###Editing admin.py


Just remember to hit "Reload" back on the web tab after you've saved your changes to the file.


###Fixing the admin CSS


When you first load the admin site, it will look all ugly because, since we're not using the dev server, the admin CSS isn't served automatically. We can hack in a quick fix for it now. Go to the [Web Tab](https://www.pythonanywhere.com/web_app_setup) and find the **Static Files** section. Add a new entry:

  * url `/static/admin/`
  * path: `/home/yourusername/.virtualenvs/myvirtualenv/lib/python3.6/site-packages/django/contrib/admin/static/admin`

Substitute *yourusername* with your actual username and *myvirtualenv* with the name of your virtualenv ("django17" in this guide). Hit reload, and visit the admin site again, and it should look pretty.

Go through the rest of the tutorial, and then, when you get to part 6, static files, below, you'll be able to delete this "hack" just replace it with a "proper" static mapping.


##Part 3 (views and templates)


This part should all work smoothly. When we use PythonAnywhere, we often find ourselves with several tabs open -- one for a Bash console, several tabs for the different files we're editing, and maybe a tab for the web app config. See what workflow suits you!


##Part 4 (forms, generic views)


No particular instructions here


##Part 5 (testing)


If you ignored our suggestion earlier to just use SQLite, and you chose a different database, you will need to explicitly create a test database for django to use to run the tests...


##Part 6 (static files)


Because we're not using `runserver`, Django won't automatically serve static files. Follow the links to Django's documentation on how to serve static files in production.

Essentially, here's what you'll have to do:

  * In settings.py, set `STATIC_URL` and `STATIC_ROOT` to sensible values, eg `/static/` for the URL, and `/home/my-username/my-django-project/static` for the root folder.
  * Run `python manage.py collectstatic` to collect all the static files into the STATIC_ROOT folder
  * On the PythonAnywhere **Web** tab, set up a **Static Files** entry which points the URL from `STATIC_URL` to the folder specified at `STATIC_ROOT`.
  * Hit reload, and go see if it worked.
