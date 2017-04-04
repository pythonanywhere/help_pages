
<!--
.. title: How to set environment variables for your web apps (for SECRET_KEY etc)
.. slug: environment-variables-for-web-apps
.. date: 2015-12-22 12:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


Many deployment guides suggest you store configuration information that's
likely to vary between platforms in Environment variables.  See [The 12-factor
app](http://12factor.net/config) for example.  While this advice isn't perfectly
adapted to a Platform-as-a-Service environment like PythonAnywhere, it can be made
to work.  Here's how.

We'll use the example of setting the Django `SECRET_KEY` setting, since it's a 
common one.

In brief, you need to set the environment variable in two different places:

* In a *postactivate* script for it to work in Bash consoles
* In your *WSGI file* for it to work in the web app itself.


## For your web app itself:  set the environment variable in your *WSGI file*

> This will ensure the environment variable is available to the worker
> processes that are actually serving your web application, live on the
> Internet.

Click over to the [Web tab](https://www.pythonanywhere.com/web_app_setup/) for your web app,
and click on the link to your **WSGI file**.  In here, you can set your environment variable
using Python syntax:

```python
import os
os.environ["SECRET_KEY"] = "mysekritvalue"
```

You can set as many environment variables as you like, this way.

Hit save, reload your web app, and it should now have access to the variable.


## For Bash consoles:  set the environment variable in your virtualenv *postactivate* script

> For when you're running database migrations, or doing any other command-line
> interactions with your web app

Assuming you're using a [Virtualenv](/pages/Virtualenvs) for your web app, the most
convenient place to set an environment variable to be available in your Bash
console sessions is in a special script called "postactivate" that gets run
automatically whenever you activate your virtualenv.

Navigate to your virtualenv itself, and find  the folder called *bin*, and inside
that you'll see a file called *postactivate*.  Open it up in the Editor.

* A typical location might be */home/yourusername/.virtualenvs/my-project-virtualenv/bin/postactivate*

Here you can set environment variables using Bash syntax:


```bash
export SECRET_KEY="mysekritvalue"
```

And, again, you can set several environment variables if you need to, one per line.

Test this out by activating your virtualenv, with, eg, `workon
my-project-virtualenv` and then trying to run `echo $SECRET_KEY`


### That's annoying!  Why do I have to set it in multiple places!

It *is* annoying.  We haven't found a good solution for de-duplicating the environment variables between these two files, but we're sure there is one out there -- if you know of one, do [get in touch!](mailto:support@pythonanywhere.com)

