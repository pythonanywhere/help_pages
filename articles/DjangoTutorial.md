
<!--
.. title: Django tutorial
.. slug: DjangoTutorial
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->





##Creating a new Django project on PythonAnywhere


So you want to create a web application, but you don't really want to do all the faffing around that is involved in setting up and configuring web servers? 

**Note:** This tutorial is for **Django 1.3 on PythonAnywhere**. If you use a different version of Django, you will get weird and unhelpful errors. 

*If you just want to follow the official django tutorial on PythonAnywhere, check out [FollowingTheDjangoTutorial](/help/pages/FollowingTheDjangoTutorial) instead*

Well, that's one of the reasons we created PythonAnywhere. This tutorial will take you through the process of creating a working Django site with an admin interface and a front page that tells you the time. At the end of the tutorial, there's also an overview of options you can use if you already know Django, and you have already coded up a web app which you want to use on PythonAnywhere. 

To follow along with this tutorial you will need a PythonAnywhere account. Go and sign up if you don't already have one then come back here. 


#Contents


[TOC]


###Quickstarting a new project


Log into PythonAnywhere, go to the **Web** tab, and click on **Add a new web app** link. 

This will pop up a dialog, whose first page asks you to enter your own domain or gives you the option of using `<username>.pythonanywhere.com`. Just select that for now and click next. 

Now you will be presented with a list of the various Web frameworks you can choose from. Select **Django**. 

This will bring up some options - feel free to change the *Project Name* to something more descriptive. The default directory is fine, or if you prefer you can put the app into your Dropbox - but you'll need to have set up a shared Dropbox folder already. There's more info on that in the **Files** tab on your dashboard 

Click the **Next** button, and after a few seconds, the wizard dialog will disappear and a very basic app will be up and running! Just click the URL at the top of the screen to go see it - you should see the default "Welcome to Django" page. 


###Creating an app inside the Django project


Django suggest that you structure your sites as *projects* which contain one or more *apps* - the idea is that you can re-use an app in different projects. 

Let's create our first app inside your project. In order to do this you start a **Bash Console** -- you can do this from the **Consoles** tab on the dashboard. 

In the console, enter the following commands: 

        cd mysite
        python ./manage.py startapp myapp


Replace `mysite` with the name of your project, if you chose a different one. 

If you do an `ls`, you'll see that Django has created a new folder called myapp inside your project. 

We'll need this console again later, so why not keep it open for now, and proceed with the rest of the tutorial in a different tab. 


###Configuring the database and enabling the admin interface


Django needs a database connection to do pretty much anything. PythonAnywhere provides support for MySQL databases but for now we will just use `sqlite3`, a file based database that does not require setting up a database account and password. 

The file that contains all the settings information for Django is called, naturally enough, `settings.py`. By default it lives in your Django project directory. 

Go to the **Files** tab on your dashboard, find your project folder, and then find `settings.py` inside it. 

We will need to change the `DATABASE` and `INSTALLED_APP` sections so that it looks like the code below. With your username and project name replaced on the line beginning with `NAME`. Do not change any other bits of it at this time. 

       1     DATABASES = {
       2         'default': {
       3             'ENGINE': 'django.db.backends.sqlite3',
       4             'NAME': '/home/<my name>/<my_test_project>/db.sqlite',
       5             'USER': '',
       6             'PASSWORD': '',
       7             'HOST': '',
       8             'PORT': ''
       9         }
      10     }



... 

       1     INSTALLED_APPS = (
       2         'django.contrib.auth',
       3         'django.contrib.contenttypes',
       4         'django.contrib.sessions',
       5         'django.contrib.sites',
       6         'django.contrib.messages',
       7         'django.contrib.staticfiles',
       8         # Uncomment the next line to enable the admin:
       9         'django.contrib.admin',
      10         # Uncomment the next line to enable admin documentation:
      11         # 'django.contrib.admindocs',
      12         'mysite.myapp',
      13     )



Again, replace `mysite.myapp` with `your-project-name.your-app-name` if necessary. 

Now that you have told Django what database to use you have to run a management command in order for it to create the initial tables and the first admin user. Go back to your Bash console and enter the following commands: 

        python ./manage.py syncdb


You will be asked a series of questions. You should enter a username, email address, and password for the first admin user. You will need this information to log in to Django's admin interface so make sure that you remember the details somehow. 

The last message that Django will print out is `No fixtures found` -- once it's printed that and returned to the Bash prompt, you're ready to continue. 


###Defining your urls


The next step is defining the urls for your application. This means you are starting to tell Django what to do when a user visits a certain location in your web site. The file to edit is called `urls.py` and it should be in the same directory as your `settings.py` file. 

Open it up and make it look like the file below - you'll need to uncomment 3 lines to do with admin and fix the first url line. Remember that you have to delete the leading spaces as well as the `#` marks to uncomment. 

Remember, as always, that each time you see `mysite` or `myapp`, you should replace them with your project name or app name, if necessary. 

       1     from django.conf.urls.defaults import patterns, include, url
       2 
       3     # Uncomment the next two lines to enable the admin:
       4     from django.contrib import admin
       5     admin.autodiscover()
       6 
       7     urlpatterns = patterns('',
       8         # This is going to be our home view.
       9         # We'll uncomment it later
      10         # url(r'^$', 'mysite.myapp.views.home', name='home'),
      11 
      12         # Uncomment the admin/doc line below to enable admin documentation:
      13         # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
      14 
      15         # Uncomment the next line to enable the admin:
      16         url(r'^admin/', include(admin.site.urls)),
      17     )



In this file you are defining two url patterns. The first one matches a blank string which is what happens when a user visits `http://<your username>.pythonanywhere.com`

The second one matches "admin/" which is Django's default admin interface, which should now be working. You can check that now if you like. First go to the **Web** tab and click the reload button to activate your changes. Then, visit: 

`http://your-username.pythonanywhere.com/admin/`

(don't forget the `/admin/` at the end of the URL!) 

You should be able to log in with the username and password that you provided earlier. When you are done come back here to continue. 

If you get an error rather than the admin interface then go back through each of these steps and check that everything is exactly like the examples. You also might want to check the error logs, available from the **Web** tab, and see if they can give you additional clues about where the the mistake might be. 


###Creating a template


![http://tutorial.pythonanywhere.com/static/django/new_folder_for_templates.png](http://tutorial.pythonanywhere.com/static/django/new_folder_for_templates.png)

Now that you have a working admin interface it is time to create a template. 

First you need to create a directory for your template inside your app folder: 

  * Go to the **Files** tab. 
  * Go to your `mysite` directory 
  * Then go down to `myapp`
  * Enter **templates** into the "Enter a new directory name" field at the top of 
    * the page and click the "New" button next to it. 

Now create a new file inside the templates folder called `home.html`, and make it look like this. 

       1     <html>
       2     <head>
       3         <title>My Python Anywhere hosted Django app</title>
       4     </head>
       5     <body>
       6         <h1>My Python Anywhere hosted Django app</h1>
       7         <p>Well, since it's already {{ right_now.minute }} past {{ right_now.hour }} UTC,
       8         that is as far as we are going to take you in this tutorial.</p>
       9         <p>What you do next is up to you...</p>
      10     </body>
      11     </html>



The values inside the `{{ }}` are going to be replaced by dynamic content when we complete our final task. Which is writing a view. 


###Writing the first view


Views are Django functions which take a request and return a response. We are going to write a very simple view called `home` which uses the `home.html` template and uses the datetime module to tell us what the time is whenever the page is refreshed. The file we need to edit is called `views.py` and it will be inside `mysite/myapp/`

Copy the code below into it and save the file. 

       1     from datetime import datetime
       2 
       3     from django.shortcuts import render
       4 
       5     def home(request):
       6         return render(request, 'home.html', {'right_now':datetime.utcnow()})



Now that we've defined the view, we can uncomment this line in `urls.py`

       1         # url(r'^$', 'mysite.myapp.views.home', name='home'),



The last step is reloading your web app so that the changes are noticed by the web server. Go and do that now, back in the **Web** tab with the big reload button. 

If you have followed along with this tutorial you should now have a working, dynamic page at `http://<your username>.pythonanywhere.com/`

You can continue to experiment with this by changing the view and the template as well as progress through the full Django tutorial [starting here](https://docs.djangoproject.com/en/dev/intro/tutorial01/#creating-models) to see what else is possible. 

But for now, that's the end of the tutorial. Happy coding! 


##Serving static files (css, images etc)


Static files are an important part of what makes a web page look right. When you quickstart a Django app on PythonAnywhere two locations are automatically created for static files Any files placed in the static or media folders inside your project will be available at `http://your-domain.com/static/` and `http://your-domain.com/media/` respectively. You can change this by editing the static file entries on the tab for your web app. 


##Existing apps / manual config


If you already have a web app, the idea is that it should be just as easy to host your project on PythonAnywhere, as it is to host in on your own PC using the Django dev server. 

There's just a couple of subtleties: 

  1. adding the right path to `sys.path` in `wsgi.py`
  1. setting up your database in `settings.py` - you'll need the full path for sqlite 
  1. setting up your static files 


###Note down the path to your project's parent folder and the project name


There are several ways you might have got a Django project into PythonAnywhere - maybe you started one from scratch using `django-admin.py startproject`. Maybe you pulled it in from [GitHub](/help/pages/GitHub) or another code sharing site using `git` or a similar VCS tool. Maybe it's in your Dropbox! 

Either way, the thing to do is make a note of the path to **parent folder of the project root**. The project root is the folder which contains `settings.py`; for example, let's say it's `/home/my_username/projects/my_project/`

In this case, you want to make a note of the path to the project's parent folder 

  * `/home/my_username/projects`

You also need to make a note of the **name of the project root folder** in this case: 

  * `my_project`

Those two together should add up to the full path to the project root. Crystal-clear? 

If you have problems with import errors, check out our [Guide to sys.path and import errors](/help/pages/DebuggingImportError)


###Edit the wsgi file


Go to your PythonAnywhere **Dashboard** and click on the **Web** tab, then click the **Add a new web app** button. In the first step, just enter the domain where you want to host your site, then in the second, instead of selecting "Django", select **Manual configuration**. This will set up a web app but won't try to create a new Django project for you. 

Once you've clicked next on the next page, you near the top of the page some text saying something like *It is configured via a WSGI file stored at: /var/www/something_com_wsgi.py"* The filename is a link, and if you click there you'll be taken to an editor displaying a *WSGI configuration file* that tells PythonAnywhere how to manage your site. If you're a WSGI wizard then you can probably work out what to do from here. But if not, just follow the steps below: 

Delete the contents and replace them with the below, replacing `/home/my_username/projects` with the path to the parent folder of your project, which you noted down earlier, and `my_project` with your project name. 

       1     # +++++++++++ DJANGO +++++++++++
       2     import os
       3     import sys
       4 
       5     ## assuming your Django settings file is at '/home/my_username/projects/my_project/settings.py'
       6     path = '/home/my_username/projects'
       7     if path not in sys.path:
       8         sys.path.append(path)
       9 
      10     os.environ['DJANGO_SETTINGS_MODULE'] = 'my_project.settings'
      11 
      12     import django.core.handlers.wsgi
      13     application = django.core.handlers.wsgi.WSGIHandler()



If you're using a version of Django &gt; 1.6 (which you really shouldn't with this guide, which is for 1.3), you'll need to replace the last two lines with this: 

    from django.core.wsgi import get_wsgi_application
    application = get_wsgi_application()

Your Django app should now work, and you can visit at `http://my_username.pythonanywhere.com`

Again, if you have any problems, check out the [guide to sys.path and import errors](/help/pages/DebuggingImportError)


###Setup the database in settings.py, and syncdb


You need to make sure of three things: 

  * if using *sqlite*, you must have the full path to your database 
  * if using *MySQL*, you'll need the database name, password, and host 
    * (`mysql.server` if you're using our MySQL service) 
  * finally, make sure all your apps are in `INSTALLED_APPS`

       1     DATABASES = {
       2         'default': {
       3             'ENGINE': 'django.db.backends.sqlite3',
       4             'NAME': '/home/my_username/my_test_project/db.sqlite', # absolute location is required
       5             'USER': '',
       6             'PASSWORD': '',
       7             'HOST': '',
       8             'PORT': ''
       9         }
      10     }
      11 
      12     INSTALLED_APPS = (
      13         #[...]
      14         'django.contrib.admin',
      15         'my_test_project.my_app',
      16     )



Now open up a **Bash console** to perform the initial database creation 

        cd <your project name>
        ./manage.py syncdb


Follow the usual prompts to create an admin user and password. 


###Static files


Checkout out our [guide to static files in Django](/help/pages/DjangoStaticFiles)


###Reload the web server and enjoy!


Now you just need to reload the web server so that it notices the changes you have made. Visit the Web tab on the Python Anywhere dashboard and click the "Reload web app" button. That's it. At this stage you have a working admin interface and can visit it at <http://my_username.pythonanywhere.com/admin>. 
