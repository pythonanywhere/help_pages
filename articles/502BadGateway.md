
<!--
.. title: I'm getting a "502 Bad Gateway / Backend" or a "504-loadbalancer" error. What to do next?
.. slug: 502BadGateway
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->




## Try hitting "Reload" again


It may just be a glitch! Reloading often clears things up. 


## Wait for the web app to be fully reloaded


Sometimes, if you go and visit your site immediately after hitting the "Reload"
button, you end up trying to access the site while it's still reloading, and
that can cause a bad gateway error. Make sure the spinner has stopped before
viewing the site. 


## Look for import errors or syntax errors in your WSGI file


If your WSGI file is totally broken, that can cause a 502 bad gateway error,
and it wouldn't end up in the error logs. 

In almost all other cases, we should be able to catch exceptions and send them
to your error logs (you have checked your error logs haven't you?) 


## Don't use app.run() (for Flask) or try to run your own web server


Flask's app.run() call tries to create its own web server, which is typically
what you would use on your own machine. 

On our servers, we run web server processes for you (using uWSGI), so there's
no need to use app.run(). Just provide the wsgi application as a variable
called "application", and we'll do the rest. 

But if you try and call app.run(), it conflicts with our web worker and breaks
stuff.   Similarly if you try and manually bind to a local port.


## Don't call django.setup in your web app code
`django.setup` is a function that is used to initialise Django in a script so
that you can use Django features in it. It re-initialises the logging
system. When you call it in a web app, it breaks the logging and you will see a
large number of log lines like this in your server log:


    :::text
    --- Logging error ---
    Traceback (most recent call last):
      File "/usr/lib/python3.10/logging/handlers.py", line 940, in emit#012    self.socket.sendto(msg, self.address)
    OSError: [Errno 9] Bad file descriptor


## Look for any slow code that might be timing out

We set a 5-minute timeout on web requests.  Look through your **server log**
(linked from the web tab) for any messages saying "Harakiri" -- they indicate
a worker was killed taking too long to process a request.

If you need to do some heavy processing or number crunching in your web app,
check out the tips [here](/pages/AsyncInWebApps)
