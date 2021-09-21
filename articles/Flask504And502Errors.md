<!--
.. title: Dealing with 504 and 502 errors in Flask applications
.. slug: Flask504And502Errors
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

The most common problem we see with Flask sites is that people try and call

    :::python
    app.run()
    # don't do this!

This tries to launch Flask's own development server, which is not
necessary on PythonAnywhere, because we do the server part for you.  Starting a
development server will just block your code, meaning that it can never receive
requests from our web-hosting system.

All you need is to import your Flask app object into your WSGI file -- something like
this:

    :::python
    from my_flask_app import app as application


The app object has to be renamed application, like that.

**Do not call `app.run()` anywhere in your code** as it will conflict with the
PythonAnywhere workers and cause errors (normally with error code 504, but
sometimes with code 502).

If you want to be able to run your code on your own machine in test mode, then
you can guard the `app.run()` like this:

```python
if __name__ == '__main__':`
    app.run()
```

That means that you can run the development server with something like
`python mysite.py` on your own machine, but the `app.run()` is prevented from
running on PythonAnywhere because on our system, `__name__` will not be equal
to `'__main__'`.

Other than that, be sure to check out our guide to
[debugging import errors](/pages/DebuggingImportError) for general tips on
dealing with problems in your WSGI config.
