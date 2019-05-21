
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

This guides pertains to the tutorial for Django 2.2: <https://docs.djangoproject.com/en/2.2/intro/tutorial01/>

This document is not a replacement for the official django tutorial, instead, it's meant to be a companion guide -- the django tutorial is meant to be your primary guide, but when you read each section of the django tutorial, you should also take a look at the corresponding section notes in this guide, for additional instructions.

So we recommend you keep both the django tutorial and this page open side-by-side as you go through them.


## Writing your first Django app, Part 1



### Creating a virtualenv and Installing Django into it


The preinstalled versions of Django on PythonAnywhere are a little out of date, but you can use a *virtualenv* to install your own versions. We'll use a nifty helper tool called virtualenvwrapper. Open up a **Bash Console** and:

    mkvirtualenv django2 --python=/usr/bin/python3.6
    pip install django ## this may take a couple of minutes


  * TIP: *if you see an error saying mkvirtualenv: command not found, check out [InstallingVirtualenvWrapper](/pages/InstallingVirtualenvWrapper)*.

Once you've created your virtualenv, you'll be able to see that it's active because your command prompt, which normally says something like `17:18 ~ $` will get prefixed with a little `(django2)`, like this:

    (django2)17:18 ~ $


***--&gt; Always make sure your virtualenv is active when working on the django tutorial***

If you need to reactivate it later, maybe if you close your bash console and open a new one, the command is:

    workon django2


It's probably a good idea to keep a bash console open at all times in one browser tab, with the virtualenv activated, so you can flick back and forth.


#### Checking the django installation


The first command the tutorial asks you to run is to check the installed version:

    python -m django --version
    # This should show something like 2.0.2.
    # If it shows anything else, you've probably forgotten to activate your virtualenv!



### Creating a project, and viewing files


After you run the `startproject` command, you can take a look around the files in your project using our file browser and built-in browser-based editor. Open a new browser tab and go to the **Files** tab, then navigate to your new "mysite" folder.

Apart from the **Files** tab, you can also use the `tree` command from the bash console to see the directory tree...



### (not) the development server: setting up your web app on the Web tab

You will probably quickly realize that the Django development server on
[PythonAnywere](https://www.pythonanywhere.com/) (ie. the `manage.py runserver`
command) doesn't work.  If you try and run it, you're likely to see an error saying
*That port is already in use*. And in any case, it won't be able to create a dev server
you can access, because our console servers aren't publicly accessible over the
Internet (they're actually different machines from our web servers).

Instead, you need to do 3 things:

1. Create a web app via our interface- this lets us know that you want to create
   a website with at `myusername.pythonanywhere.com` and
   that we should listen and try to respond to any web traffic that comes to us
   for that domain.

2. Configure the web app to be run inside the virtualenv that you just set up -
   this lets us know which versions of python and django we should be using.

3. Configure the web app so that we know what actual code to run.


Let's take this step by step.

First, to create a web app on PythonAnywhere, open up a new browser tab and go
to our **Web** tab. Click **Add a new web app**, choose **Manual
configuration** and then **Python 3.6**.

* *TIP: Make sure you choose "Manual configuration", not "Django" when creating your webapp. We need the manual option to make sure we get Django 2 from our virtualenv*

When you hit next, you'll be on your web app configuration page, and it's probably a good idea to keep this tab open
in your browser at all times too, so that you can easily jump back to it.  It
will allow you to easily hit reload on your web app, or find your error log, and
things like that.

Second, go to the **Virtualenv section** of your web app and enter the name of our virtualenv,
**django2**.  When you click confirm, you should find completes to a full path like this:
*/home/myusername/.virtualenvs/django2*.

Finally, your wsgi.py file is how we know what code to run for you. Find the
link to **edit your wsgi file**, delete everything and replace it with this:

```python
import os
import sys

path = os.path.expanduser('~/mysite')
if path not in sys.path:
    sys.path.insert(0, path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'mysite.settings'
from django.core.wsgi import get_wsgi_application
from django.contrib.staticfiles.handlers import StaticFilesHandler
application = StaticFilesHandler(get_wsgi_application())
```


Save the file, then go back to the **Web** tab and hit the **Reload** button. Now instead of the django dev server running on your own machine, you have a django site live and on the Internet, at *yourusername.pythonanywhere.com*.  Try clicking the link to see it now.

***--&gt; Whenever you make changes to files in your django project, you'll need to hit "Reload" on the web tab to publish them and make them live on the actual site.***

#### fixing the DisallowedHost error

If you try and click through to yoru site now, you will see an error page (`Invalid HTTP_HOST header`) instead of the Django welcome page. This is because your page is on the internet, and is access via the url/domain that you just setup (eg. `myusername.pythonanywhere.com`) is different from running a server locally and accessing it locally.

You will need to tell Django what site it's processing requests for by going to
the **Files** tab, and editing `mysite/settings.py`. Find `ALLOWED_HOSTS` in
`settings.py` and editing it like this:


```python
ALLOWED_HOSTS = ['*']
# once you finish the tutorial, you might want to change this to a more secure setting, 'yourusername.pythonanywhere.com'.
```

Reload your webapp, and now when you visit your site, you should see the expected startup page, with its little rocket and message saying "The install worked successfully! Congratulations!".

You can now follow along with the rest of Part 1 of the official tutorial, more or less from the **Creating the Polls app** section onwards, using the tab with your Bash console, and another tab for editing files perhaps.

* *TIP: when you've finished editing views.py and the various urls.py files, don't forget to reload your webapp before going to check out your new /polls/ url on your live site*


## Writing your first Django app, Part 2

### Database setup and settings.py



We support different databases, but using SQlite, the default, is probably simplest at this stage. You can change your `TIME_ZONE` setting as they suggest if you like though.

  * TIP: *the links to the documentation in the comments in settings.py should point to the same django version as your virtualenv, 2.0. If they don't, then you probably accidentally ran the `startproject` command without activating the virtualenv. Probably best to delete the whole `mysite` directory, make sure your virtualenv is active, and run `startproject` again.*.



### Playing with the API

Everything in this section should work fine in your Bash console.

(A minor thing: if you want a better interactive interpreter for `manage.py shell`, do a

    pip install ipython

and you'll get nice tab-completion and syntax highlighting).


### *Do not* start the development server to access the Django Admin


Remember, don't use `runserver` and *localhost:8000* on PythonAnywhere.
Instead, go back to your **Web** tab, hit reload if you have made any changes
following the Django tutorial, and then you will then be able to go to
*myusername.pythonanywhere.com/admin* and see the admin site up and running.



## Writing your first Django app, Part 3 & 4


This part should all work smoothly.

You'll probably find yourself using our "Files" tab quite a lot here, to create new files and directories, and edit them, as well as occasionlly flicking back to the Bash console to run commands, or the Web tab to reload your web app, and maybe to yet another tab to check your live site.

When we use PythonAnywhere, we often find ourselves with lots of different browser tabs open at the same time  -- one for a Bash console, several tabs for the different files we're editing, and maybe a tab for the web app config. See what workflow suits you!


## Part 5 (testing)


If you ignored our suggestion earlier to just use SQLite, and you chose a different database, you will need to explicitly create a test database for django to use to run the tests...


## Part 6 (static files)

We used a little hack in our wsgi file that means static files are served by `django.contrib.static.StaticFilesHandler`.  Everything will work fine, but for a production app, you should read our [guide to static files in django](https://help.pythonanywhere.com/pages/DjangoStaticFiles)

## Part 7 (customising the admin)

All of this will work fine, just remember to reload your web app every time you want to see changes to the admin.

If you haven't found it already, you might see a little "reload" icon in the editor, which will save you a trip to the web tab...


Happy Django-ing!
