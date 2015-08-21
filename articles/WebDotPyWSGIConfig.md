
<!--
.. title: How to configure a web.py app as a pythonanywhere wsgi application
.. slug: WebDotPyWSGIConfig
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



Web.py applications usually have an `"app"` variable to represent the application. You can turn this into a wsgi-compatible application by calling `.wsgifunc()` on it. So, in your wsgi file, you'll need something like this: 

       1 sys.path.append('/home/myusername/path-to/my-webdotpy-files')
       2 from myapp import app
       3 application = app.wsgifunc()



Other than that, be sure to check out our guide to [Debugging import errors](/pages/DebuggingImportError) for general tips on dealing with problems in your wsgi config. 
