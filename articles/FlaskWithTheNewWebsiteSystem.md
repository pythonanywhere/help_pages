<!--
.. title: Deploying Flask sites on PythonAnywhere with our experimental website system
.. slug: FlaskWithTheNewWebsiteSystem
.. date: 2025-05-15 14:30:00 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

# Disclaimer

This help page explains how to set up an Flask site on PythonAnywhere using our
new experimental website-hosting system.  If you want to set up a Flask site
normally, then you should follow [these instructions instead](/pages/Flask).  These
instructions will only be useful if you want to try out things like threading
in your site.

Some important limitations to know about:

 * There is no support for static file mappings.
 * There is a very limited web UI for creating and managing these new-style websites.
   Contact [support@pythonanywhere.com](mailto:support@pythonanywhere.com) if
   you would like us to enable it for your account.
 * We do not guarantee that the command line syntax and the API interface will remain the same.
 * We have not worked out the long-term pricing for sites hosted this way, which will probably
   differ from the way we charge for traditional ones.  We're 99.9% certain that
   there will be a way to host them in a free plan, though!

If you are brave enough to try it, here is a quick guide on how to do it :-)

# Prerequisites

## API token

This help page explains how to manage your websites using our `pa` command-line
tool rather than the API, but you'll need to generate an API token so that
that tool knows how to connect to PythonAnywhere.

[This page](/pages/GettingYourAPIToken) will show you how to do that.

Now you can use our command-line tool or our experimental API to deploy your
Flask website.  This help page will show you how to use the command-line
tool, so you don't need to note down the API token -- now that it has been
generated, it's available to any code running inside Bash consoles on
PythonAnywhere.

## Installing the command-line tools

As a first step, start a fresh Bash console, and in there, install the latest
version of our command-line tool.

```bash
pip install --upgrade pythonanywhere
```

(As of this writing, it will print out an error about `typing-extensions`, but
you can ignore that.)

Running that install will make a new command, `pa` available, which we'll be
using later.


## Creating a simple test website

Create a directory called `mysite` in your home directory, and create a file called
`flask_app.py` in there.  Use this code:

```python
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello from Flask on the experimental website platform!'
```

Next, you should create a [virtualenv](/pages/VirtualenvsExplained) with `flask`, `gunicorn`
and `eventlet` installed.  Go back to your Bash console, and run this:

```bash
mkvirtualenv my_venv --python=python3.10
```

...and then:

```
pip install flask gunicorn eventlet
```

Now you have some sample Flask code and a virtualenv with everything
installed to use it.  Time to get it online!


# Managing your website

## Creating your website

In Bash, to deploy your website to your subdomain -- that is, to
*yourusername*`.pythonanywhere.com` if you're on our US system, or
*yourusername*`.eu.pythonanywhere.com` if you're on the EU system -- just run
the following.  You'll need to replace the domain argument and your username
as appropriate.

```bash
pa website create --domain YOURUSERNAME.pythonanywhere.com --command '/home/YOURUSERNAME/.virtualenvs/my_venv/bin/gunicorn --worker-class eventlet -w 1 --chdir /home/YOURUSERNAME/mysite --bind unix:${DOMAIN_SOCKET} flask_app:app'
```

If everything was successful, you should see something like:

```text
< All done! Your site is now live at YOURUSERNAME.pythonanywhere.com. >
   \
    ~<:>>>>>>>>>
```

Now, if you go to the website URL defined in `domain` you should get the sample
website!

*Note:* as of this writing, there is a bug that means that you might get a 404
not found page for a few seconds before the site comes up.  If you get that,
just refresh the page in your browser.  We're on the case :-)

You have a working Flask website hosted on PythonAnywhere using our experimental website system.  However, this site
will not currently appear on the "Web" page inside your PythonAnywhere account;
we have a user interface that is a work-in-progress, though, and if you'd like
to try that out, [drop us a line](mailto:support@pythonanywhere.com).


## Getting and listing websites

You can get a list of async websites from PythonAnywhere with this command:

```bash
pa website get
```

You'll get something like this:

```text
domain name                      enabled
-------------------------------  ---------
YOURUSERNAME.pythonanywhere.com  True
```

And you can get the details for one website like this:

```bash
pa website get --domain YOURUSERNAME.pythonanywhere.com
```

...which will display something like this:

```text
-----------  -------------------------------------------------------------------------------------------------------------------------
domain name  YOURUSERNAME.pythonanywhere.com
enabled      True
command      /home/YOURUSERNAME/.virtualenvs/my_venv/bin/gunicorn --worker-class eventlet -w 1 --chdir /home/YOURUSERNAME/mysite --bind unix:${DOMAIN_SOCKET} flask_app:app
access log   /var/log/YOURUSERNAME.pythonanywhere.com.access.log
error log    /var/log/YOURUSERNAME.pythonanywhere.com.error.log
server log   /var/log/YOURUSERNAME.pythonanywhere.com.server.log
-----------  -------------------------------------------------------------------------------------------------------------------------
```

## Using a custom domain for your web app

If you are using a custom domain, there will be an extra field called `cname`
in the output above. This is the CNAME that you can use in your DNS settings
for your web app. For more details on setting up DNS for a custom domain, see:

- [How DNS works: a beginner's guide](https://help.pythonanywhere.com/pages/DNSPrimer/),
- [Setting up a custom domain on PythonAnywhere](https://help.pythonanywhere.com/pages/CustomDomains/),
- [Naked domains](https://help.pythonanywhere.com/pages/NakedDomains/),
- [Troubleshooting DNS](https://help.pythonanywhere.com/pages/TroubleshootingDNS/).


## Enabling HTTPS for your custom domain webapp

You can get a Let's Encrypt certificate for your custom domain using the API too:

```bash
pa website create-autorenew-cert --domain YOURCUSTOMDOMAIN
```

## Reloading

If you change the code of your website, you'll need to reload it to activate
those changes:

```bash
pa website reload --domain YOURUSERNAME.pythonanywhere.com
```

If all goes well, you'll see this:

```text
< Website YOURUSERNAME.pythonanywhere.com has been reloaded! >
   \
    ~<:>>>>>>>>>
```

...and if you visit the site, you'll see that it's been updated to run your new
code.

## Delete

To delete your website, use this:

```bash
pa website delete --domain YOURUSERNAME.pythonanywhere.com
```

If all goes well, you'll see this:

```text
< Website YOURUSERNAME.pythonanywhere.com has been deleted! >
   \
    ~<:>>>>>>>>>
```

...and the website will be gone, and replaced with our default "Coming Soon!"
page.


# Supported UI features

## Logs

You can access the logs -- the ones that were printed out by the detailed
version of the `pa website get` command -- from the **Files** page or from a
console; they're located in `/var/log`.

### The error log

For example, `/var/log/YOURUSERNAME.pythonanywhere.com.error.log`.

By default, gunicorn logs its status messages to the standard error stream, so
if all is well you'll see something like this:

```text
[2024-08-20 15:28:23 +0000] [1] [INFO] Starting gunicorn 23.0.0
[2024-08-20 15:28:23 +0000] [1] [INFO] Listening at: unix:/var/sockets/YOURUSERNAME.pythonanywhere.com/app.sock (1)
[2024-08-20 15:28:23 +0000] [1] [INFO] Using worker: eventlet
[2024-08-20 15:28:23 +0000] [2] [INFO] Booting worker with pid: 2
```

The second line is gunicorn saying that it has successfully started, and is listening
for incoming requests on an internal [unix domain socket](https://en.wikipedia.org/wiki/Unix_domain_socket).
That socket is internal to our web-hosting system -- you won't be able to see
it in a console or on the "Files" page inside PythonAnywhere.

### The server log

For example, `/var/log/YOURUSERNAME.pythonanywhere.com.server.log`.

By default, gunicorn logs client disconnects there, so you'll see
something like this:

```text
Client disconnected
Client disconnected
```

### The access log

For example, `/var/log/YOURUSERNAME.pythonanywhere.com.access.log`.

This will also show incoming requests, but will be formatted similarly to other
PythonAnywhere websites -- for example:

```text
1.2.3.4 - - [17/Oct/2023:13:14:00 +0000] "GET / HTTP/1.1" 200 32 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" "1.2.3.4" response-time=0.286
```


# Technical details

If you just want to get an async site up and running, all you need to do is follow
the recipe above.  However, if you'd like to understand a bit more about what is
going on, or to build on these instructions to do more than just Flask-SocketIO, read on!

Let's take a look at the command we specified when we created the site:

```text
/home/YOURUSERNAME/.virtualenvs/my_venv/bin/gunicorn --worker-class eventlet -w 1 --chdir /home/YOURUSERNAME/mysite --bind unix:${DOMAIN_SOCKET} flask_app:app
```

Breaking that down:

* `/home/YOURUSERNAME/.virtualenvs/my_venv/bin/gunicorn` is the path to gunicorn in your virtualenv.  Gunicorn is an WSGI container program -- it can run any WSGI-based Python web framework, but in particular it can handle sites that work asynchronously.
* `--worker-class eventlet -w 1` is telling gunicorn to use an eventlet inner loop with one worker
* `--chdir /home/YOURUSERNAME/mysite` is making it change the working directory to the one containing your website's code.
* `--bind unix:${DOMAIN_SOCKET}` is telling gunicorn to listen for incoming requests on a unix domain socket -- the location of that socket is provided by our system in the environment variable `DOMAIN_SOCKET`
* `flask_app:app` is telling gunicorn, which is looking for code in the working directory it switched to with the `--chdir`, to load up the async app called `app` from the file `flask_app.py`.

As we mentioned above, that domain socket (which will be something like
`/var/sockets/YOURUSERNAME.pythonanywhere.com/app.sock`) is internal to the
part of our system that serves websites; you won't be able to see
it in a console or on the "Files" page inside PythonAnywhere.


# The API

If you want to control your async site programatically, using Python code rather
than the `pa` command-line tool, check out [this help page](/pages/ASGIAPI).


