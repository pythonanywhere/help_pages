
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

To avoid duplication, we recommend using a **.env file** and a tool called
[python-dotenv](https://github.com/theskumar/python-dotenv) to load it.

## Start by saving your environment variables into a .env file in your project folder

You can run something like this in a Bash console, or edit the .env file directly
using our "Files" tab:
```bash
cd ~/my-project-dir
echo "export SECRET_KEY=sekritvalue" >> .env
echo "export OTHER_SECRET=somethingelse" >> .env
# etc
```

# Install python-dotenv into your virtualenv

```bash
workon my-virtualenv-name
pip install python-dotenv
# or, if you're not using a virtualenv:
pip3.6 install --user python-dotenv

# and, optionally, add it to your requirements.txt, if you're using one:
echo python-dotenv >> requirements.txt
```

## For your web app itself:  loading your .env file in your *WSGI file*

> This will ensure the environment variables is available to the worker
> processes that are actually serving your web application, live on the
> Internet.

Click over to the [Web tab](https://www.pythonanywhere.com/web_app_setup/) for your web app,
and click on the link to your **WSGI file**.  In here, you can set your environment variable
using Python syntax:

```python
import os
from dotenv import load_dotenv
project_folder = os.path.expanduser('~/my-project-dir')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))
```

Save this change, and your code will now have access to the variable from `os.getenv`,
so with the Django `SECRET_KEY` setting, you can just add this to your `settings.py`:

    import os
    SECRET_KEY = os.getenv("SECRET_KEY")

Hit save, reload your web app, and it should now have access to the variable.


## For Bash consoles:  load your .env file in your virtualenv *postactivate* script

> For when you're running database migrations, or doing any other command-line
> interactions with your web app

Here's how to load up the environnment variables from your .env file in a Bash console:
```bash
set -a; source ~/my-project-dir/.env; set +a
```

Assuming you're using a [Virtualenv](/pages/Virtualenvs) for your web app, and also
assuming you're using virtualenvwrapper/workon, a
convenient place to set an environment variable to be available in your Bash
console sessions is in a special script called "postactivate" that gets run
automatically whenever you activate your virtualenv.

* A typical location might be */home/yourusername/.virtualenvs/my-project-virtualenv/bin/postactivate*

Here's how you might add the `source` command above to your postactivate script:

```bash
echo 'set -a; source ~/my-project-dir/.env; set +a' >> ~/.virtualenvs/my-project-virtualenv/bin/postactivate
```

Test this out by activating your virtualenv, with, eg, `workon
my-project-virtualenv` and then trying to run eg `echo $SECRET_KEY`


### All done!

Your environment variables should now load automatically, both in your webapp,
and in your virtualenv.
