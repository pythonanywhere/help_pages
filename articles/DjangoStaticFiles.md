
<!--
.. title: How to setup static files in Django
.. slug: DjangoStaticFiles
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



There are 3 main things to do:

  * set `STATIC_ROOT` in settings.py
  * run `python2.7 manage.py collectstatic` (or `python3.5` or `python3.6` as appropriate)
  * set up a Static Files entry on the PythonAnywhere Web tab.

Optionally, you can also customise `STATIC_URL`, if you want to use a static URL prefix other than */static/*


##Set STATIC_ROOT in settings.py


The `STATIC_ROOT` variable in *settings.py* defines the single folder you want
to collect all your static files into. Typically, this would be a top-level
folder inside your project, eg:

    :::python
    STATIC_ROOT = "/home/myusername/myproject/static"
    # or, eg,
    STATIC_ROOT = os.path.join(BASE_DIR, "static")


The important thing is this needs to be the full, absolute path to your static files folder.


##Run pythonX.Y manage.py collectstatic


This command (don't forget to replace "X.Y" with the version of Python your
website uses) collects up all your static files from each of your app folders
(including the static files for the admin app) and from any other folders you
specify in settings.py, and copies them into `STATIC_ROOT`.

You need to re-run this command whenever you want to publish new versions of
your static files.


##(Optionally) change STATIC_URL


If you really must, you can change the default STATIC_URL, which is `/static/`,
to being a different prefix, like `/assets/`, or whatever it may be. You'll
probably want to use the `{% static %}` template tag with this. There's more
info in the [django
docs](https://docs.djangoproject.com/en/dev/howto/static-files/).


##Set up a static files mapping


Finally, set up a static files mapping to get our web servers to serve out your static files for you.

  * Go to the **Web** tab on the PythonAnywhere dashboard
  * Go to the **Static Files** section
  * Enter the same URL as `STATIC_URL` in the **url** section (typically, `/static/`)
  * Enter the path from `STATIC_ROOT` into the **path** section (the full path, including `/home/username/etc`)

Then hit **Reload** and test your static file mapping by going to retrieve a known static file.

Eg, if you have a file at `/home/myusername/myproject/static/css/base.css`, go visit *<http://www.your-domain.com/static/css/base.css>*


##Serving static files in development


Django does have an alternative for serving static files during development,
which can avoid the need for you to run `collectstatic` whenever you make
changes to your files, but it comes at the cost of putting an extra processing
burden on the Python parts of your app. If you really want to use this, you'll
find more info in the [django
docs.](https://docs.djangoproject.com/en/dev/howto/static-files/)


##Media files


If you're using Django's [default uploaded files
handling](https://docs.djangoproject.com/en/dev/topics/files/), then you'll
need to set up a similar static files mapping from `MEDIA_URL` to
`MEDIA_ROOT`...

