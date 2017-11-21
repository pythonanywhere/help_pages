
<!--
.. title: How to configure a Dash web app as a pythonanywhere wsgi application
.. slug: DashWSGIConfig
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



Dash apps have a app.server that you need to pass to WSGI. Your wsgi.py will have something like this:

    :::python
    from myapp import app
    application = app.server

We followed [this Dash tutorial](https://plot.ly/dash/getting-started)
and created [this website](http://dashingdemo.pythonanywhere.com/) using the code from the first example. You can take a look at the git repo [here](https://github.com/conradho/dashingdemo).

Other than that, be sure to check out our guide to [Debugging import errors](/pages/DebuggingImportError) for general tips on dealing with problems in your wsgi config.
