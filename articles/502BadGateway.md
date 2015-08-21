
<!--
.. title: I'm getting a "502 Bad Gateway / Backend" error. What to do next?
.. slug: 502BadGateway
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->




###Try hitting "Reload" again


It may just be a glitch! Reloading often clears things up. 


###Wait for the web app to be fully reloaded


Sometimes, if you go and visit your site immediately after hitting the "Reload" button, you end up trying to access the site while it's still reloading, and that can cause a bad gateway error. Make sure the spinner has stopped before viewing the site. 


###Look for import errors or syntax errors in your WSGI file


If your WSGI file is totally broken, that can cause a 502 bad gateway error, and it wouldn't end up in the error logs. 

In almost all other cases, we should be able to catch exceptions and send them to your error logs (you have checked your error logs haven't you?) 


###Don't use app.run() (for Flask) or try to run your own web server


Flask's app.run() call tries to create its own web server, which is typically what you would use on your own machine. 

On our servers, we run web server processes for you (using uWSGI), so there's no need to use app.run(). Just provide the wsgi application as a variable called "application", and we'll do the rest. 

But if you try and call app.run(), it conflicts with our web worker and breaks stuff. 


###Contact support if nothing else works


We're always happy to help. Use the "send feedback" button, or post in the forums, or email us at [support@pythonanywhere.com](mailto:support@pythonanywhere.com). 
