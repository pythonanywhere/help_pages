
<!--
.. title: Dealing with 504 errors in flask applications (or, getting wsgi config right)
.. slug: Flask504Error
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



The most common problem we see with flask apps is that people try and call

    :::python
    app.run()
    # don't do this!


This actually tries to launch Flask's own development server. That's not necessary on PythonAnywhere, because we do the server part for you. All you need is to import your flask app into your wsgi file, something like this:

    :::python
    from my_flask_app import app as application


The app has to be renamed application, like that.

**Do not call app.run() anywhere in your code** as it will conflict with the PythonAnywhere workers and cause 504 errors. Or, if you must call app.run() (eg to be able to run a test server on your own pc), then make sure it's inside an `if __name__ == '__main__':` block

Other than that, be sure to check out our guide to [Debugging import errors](/pages/DebuggingImportError) for general tips on dealing with problems in your wsgi config.
