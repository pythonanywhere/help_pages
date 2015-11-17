
<!--
.. title: How to use Mezzanine on PythonAnywhere
.. slug: HowtouseMezzanineonPythonAnywhere
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->




##Install mezzanine into a virtualenv


The default version of mezzanine available on PythonAnywhere is a little old. To get the latest version, you need to use a virtualenv. Also, take a look at this PythonAnywhere [forum thread]((www.pythonanywhere.com/forums/topic/2693/)) if you are using Mezzanine 4 or higher and running into problems.


###Creating a virtualenv


Start by creating a virtualenv -- a "virtual environment" which has only the python packages you want, rather than the system default ones. This allows you to use the latest version of mezzanine.

    :::bash
    source virtualenvwrapper.sh
    mkvirtualenv mezzanine
    # or optionally, mkvirtualenv mezzanine --python=python3  to use Python 3
    # you can also use --system-site-packages, see below


  * ASIDE: If you use *--system-site-packages*, you'll get all of the pythonanywhere [batteries included system pacakges](//www.pythonanywhere.com/batteries_included/) like numpy, scipy etc, available in your virtualenv. the difference will be that you will then be able to install your own, upgraded version over the top, which is what we're doing with the mezzanine package.

You will now be "in" the virtualenv. You can tell whenever your virtualenv is active, because its name appears in the bash prompt:

    :::
    (mezzanine)15:18 ~ $


From this point on, you can use

    :::bash
    deactivate # to switch off the virtualenv
    workon mezzanine # to go back into the virtualenv


    pip install mezzanine
    # will show "downloading mezzanine... downloading django.. downloading requests etc
    # it may take several minutes for the install to complete.

    # check mezzanine has installed correctly
    pip freeze | grep -i mezzanine
    # this should show a recent version.


If anything goes wrong, make sure you were "in" the virtualenv when you started. Did the prompt have the little `(mezzanine)`? If not, use `workon mezzanine`.


##Starting a mezzanine project


Next is building your actual mezzanine site.


###Creating the project


I'm using *project_name* as the project name, but you can substitute in whatever you want - as long as you do it everywhere!

    :::bash
    workon mezzanine
    mezzanine-project project_name
    cd project_name



###Setting a timezone


Next you'll need to edit the *settings.py* for your project. Use the **Files** menu to navigate to *project_name/settings.py*, and then find the line that defines `TIME_ZONE`, and set it to something appropriate, eg:

    :::python
    TIME_ZONE = 'Europe/London'



###Creating the database

    :::python
    python manage.py createdb --noinput



##Creating a web app


Go to the **Web tab** on PythonAnywhere, and click **Start a new Web App**. Choose **Manual Configuration**.


###virtualenv


In the **virtualenv** section of the web tab, enter the path to your virtualenv: */home/yourusername/.virtualenvs/mezzanine* in our example.


###WSGI configuration: sys.path + django settings module


Once it's loaded, click on the link to your **WSGI file**, and edit it so that it looks a little like this:

    :::python
    import os
    import sys

    # add project folder to path
    path = '/home/yourusername/project_name':
    if path not in sys.path:
        sys.path.append(path)

    # Remove any references to your home folder (this can break Mezzanine)
    while "." in sys.path:
        sys.path.remove(".")
    while "" in sys.path:
        sys.path.remove("")

    # specify django settings
    os.environ['DJANGO_SETTINGS_MODULE'] = 'project_name.settings'

    # load default django wsgi app
    import django.core.handlers.wsgi
    application = django.core.handlers.wsgi.WSGIHandler()



####Reload Web App


Hit the big **Reload Web App** button, and click on the link to your site. You should now see a live site saying things like "Home" and "Congratulations", but the layout will look all broken, because the CSS isn't loading yet.


##Configuring static files



###Add a Static files entry on the Web tab


Back on the **Web tab**, go to the **Static Files** section, and enter a static file with

  * URL: `/static/`
  * path: `/home/yourusername/project_name/static`


###Run manage.py collectstatic


Open, or re-open your **Bash console**, and run

    :::bash
    workon mezzanine
    python manage.py collectstatic



####Reload web app


Back on the **Web tab**, hit the big **Reload** button,

Now your site should be live, and looking good!


##Things to think about next


  * The default database for Mezzanine is SQLite. It's fine for testing, but you probably want to switch to MySQL for production use. Check out the [UsingMySQL](/pages/UsingMySQL) page.
  * You'll want to switch `DEBUG` to False, and that will need you need to fill in `ALLOWED_HOSTS` in *settings.py*


###Customising templates


There's a few notes in this forum thread: <https://www.pythonanywhere.com/forums/topic/1195/>
