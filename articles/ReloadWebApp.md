
<!--
.. title: Reload web app
.. slug: ReloadWebApp
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->





##Reloading web apps


Unfortunately you do have to reload your web app when you change code (templates are usually automatically reloaded). Just go to the "Web" tab, make sure that the tab at the left for your web app is selected, then hit the button at the top. 

When you hit reload, we finish serving the requests that your workers are currently processing, and then we stop the workers, drop any requests that are in the queue, and spin up workers with the new code. While this is happening, any new requests will get a 302 redirect back to itself that keeps looping until your workers are done spinning up.

You can also setup your web app to reload based on git actions:
1. If you are developing on PythonAnywhere, you can setup a git hook (eg: post-commit, post-push etc) to automatically reload your web app by touching `/var/www/www_mydomain_com_wsgi.py`.
2. Alternatively, if you are developing on your local machine and would like the changes to be automatically made on PythonAnywhere, we have written a blogpost [here](https://blog.pythonanywhere.com/87/) about how to set that up.
