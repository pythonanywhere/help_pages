<!--
.. title: Deploying Flask-SocketIO sites on PythonAnywhere (beta)
.. slug: FlaskSocketIO
.. date: 2024-08-20 14:30:00 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

# Disclaimer

This help page explains how to set up an Flask-SocketIO site on PythonAnywhere.

**Note:** deployment of async websites on PythonAnywhere is an
experimental feature.  Some important limitations to know about:

 * HTTPS is only available on default PythonAnywhere subdomains (e.g. `YOURUSERNAME.pythonanywhere.com`).
 * There is no support for static file mappings.
 * There is no web UI for creating and managing async websites -- it's API and command-line only.
 * We do not guarantee that the command line syntax and the API interface will remain the same.
 * We have not worked out the long-term pricing for async sites, which will probably
   differ from the way we charge for traditional WSGI ones.  We're 99.9% certain that
   there will be a way to host them in a free plan, though!

If you are brave enough to try it, here is a quick guide on how to do it :-)

## Prerequisites

### API token

This help page explains how to manage your websites using our `pa` command-line
tool rather than the API, but you'll need to generate an API token so that
that tool knows how to connect to PythonAnywhere.

To do that, log in to
PythonAnywhere, and go to the "Account" page using the link at the top right.
Click on the "API token" tab; if you don't already have a token, it will look
like this:

<img alt="API token not set up" src="/api-token-needs-generation.png" class="bordered-image">

Click the "Create a new API token" button to get your token, and you'll see
this:

<img alt="API token set up" src="/api-token-set-up.png" class="bordered-image">

That string of letters and numbers (masked out
in the screenshot) is the API token, and anyone who has it can access your
PythonAnywhere account and do stuff -- so keep it secret. If someone does
somehow get hold of it, you can revoke it on this page by clicking the red
button -- that stops it from working in the future, and creates a new one for
you to use.

Now you can use our command-line tool or our experimental API to deploy your
ASGI website.  This help page will show you how to use the command-line
tool, so you don't need to note down the API token -- now that it has been
generated, it's available to any code running inside Bash consoles on
PythonAnywhere.

### Installing the command-line tools

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

In this example, we'll use the example website that is part of Flask-SocketIO
itself, so you should start off by cloning it.

```bash
git clone https://github.com/miguelgrinberg/Flask-SocketIO.git
```

This will put all of the code for Flask-SocketIO into a directory called
`Flask-SocketIO` in your home directory.  We'll need to make one small change to
it; use the "Files" page inside PythonAnywhere to navigate to that directory, then
to the `example` subdirectory.  There, you should edit the file `app.py`, and
look for this line near the top:

```python
socketio = SocketIO(app, async_mode=async_mode)
```

Change it to look like this:

```
socketio = SocketIO(app, async_mode=async_mode, cors_allowed_origins="*")
```

Then save the file.

Next, you should create a virtual environment with `flask-socketio`, `gunicorn`
and `eventlet` installed.  Got back to your Bash console, and run this:

```bash
mkvirtualenv my_venv --python=python3.10
```

...and then:

```
pip install flask-socketio gunicorn eventlet
```

Now you have some sample Flask-SocketIO code and a virtualenv with everything
installed to use it.  Time to get it online!


## Managing your website

### Creating your website

In Bash, to deploy your website to your subdomain -- that is, to
*yourusername*`.pythonanywhere.com` if you're on our US system, or
*yourusername*`.eu.pythonanywhere.com` if you're on the EU system -- just run
the following.  You'll need to replace the domain argument and your username
as appropriate.


```bash
pa website create --domain YOURUSERNAME.pythonanywhere.com --command '/home/YOURUSERNAME/.virtualenvs/my_venv/bin/gunicorn --worker-class eventlet -w 1 --chdir /home/YOURUSERNAME/Flask-SocketIO/example --bind unix:${DOMAIN_SOCKET} app:app'
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

You have a working Flask-SocketIO website hosted on PythonAnywhere!  However, this site
will not currently appear on the "Web" page inside your PythonAnywhere account;
we have a user interface that is a work-in-progress, though, and if you'd like
to try that out, [drop us a line](mailto:support@pythonanywhere.com).


### Getting and listing websites

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
command      /home/YOURUSERNAME/.virtualenvs/my_venv/bin/gunicorn --worker-class eventlet -w 1 --chdir /home/YOURUSERNAME/Flask-SocketIO/example --bind unix:${DOMAIN_SOCKET} app:app
-----------  -------------------------------------------------------------------------------------------------------------------------
```

### Reloading

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

### Delete

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


## Supported UI features

### Logs

You can access the logs -- the ones that were printed out by the detailed
version of the `pa website get` command -- from the **Files** page or from a
console; they're located in `/var/log`.

#### The error log

For example, `/var/log/YOURUSERNAME.pythonanywhere.com.error.log`.

By default, gunicorn logs its status messages to the standard error stream, so
if all is well you'll see something like this:

```text
[2024-08-20 15:28:23 +0000] [1] [INFO] Starting gunicorn 23.0.0
[2024-08-20 15:28:23 +0000] [1] [INFO] Listening at: unix:/var/sockets/YOURUSERNAME.pythonanywhere.com/app.sock (1)
[2024-08-20 15:28:23 +0000] [1] [INFO] Using worker: eventlet
[2024-08-20 15:28:23 +0000] [2] [INFO] Booting worker with pid: 2
```

The second line is uvicorn saying that it has successfully started, and is listening
for incoming requests on an internal [unix domain socket](https://en.wikipedia.org/wiki/Unix_domain_socket).
That socket is internal to our web-hosting system -- you won't be able to see
it in a console or on the "Files" page inside PythonAnywhere.

#### The server log

For example, `/var/log/YOURUSERNAME.pythonanywhere.com.server.log`.

By default, gunicorn logs client disconnects there, so you'll see
something like this:

```text
Client disconnected
Client disconnected
```

#### The access log

For example, `/var/log/YOURUSERNAME.pythonanywhere.com.access.log`.

This will also show incoming requests, but will be formatted similarly to other
PythonAnywhere websites -- for example:

```text
1.2.3.4 - - [17/Oct/2023:13:14:00 +0000] "GET / HTTP/1.1" 200 32 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" "1.2.3.4" response-time=0.286
```


## Technical details

If you just want to get an async site up and running, all you need to do is follow
the recipe above.  However, if you'd like to understand a bit more about what is
going on, or to build on these instructions to do more than just Flask-SocketIO, read on!

Let's take a look at the command we specified when we created the site:

```text
/home/YOURUSERNAME/.virtualenvs/my_venv/bin/gunicorn --worker-class eventlet -w 1 --chdir /home/YOURUSERNAME/Flask-SocketIO/example --bind unix:${DOMAIN_SOCKET} app:app
```

Breaking that down:

* `/home/YOURUSERNAME/.virtualenvs/my_venv/bin/gunicorn` is the path to gunicorn in your virtualenv.  Gunicorn is an WSGI container program -- it can run any WSGI-based Python web framework, but in particular it can handle sites that work asynchronously.
* `--worker-class eventlet -w 1` is telling gunicorn to use an eventlet inner loop with one worker
* `--chdir /home/YOURUSERNAME/Flask-SocketIO/example` is making it change the working directory to the one containing your website's code -- in this example, the Flask-SocketIO example.
* `--bind unix:${DOMAIN_SOCKET}` is telling gunicorn to listen for incoming requests on a unix domain socket -- the location of that socket is provided by our system in the environment variable `DOMAIN_SOCKET`
* `app:app` is telling gunicorn, which is looking for code in the working directory it switched to with the `--chdir`, to load up the ASGI app called `app` from the file `app.py`.

As we mentioned above, that domain socket (which will be something like
`/var/sockets/YOURUSERNAME.pythonanywhere.com/app.sock`) is internal to the
part of our system that serves websites; you won't be able to see
it in a console or on the "Files" page inside PythonAnywhere.


## ASGI sites

Flask-SocketIO is kind of a half-way house towards async websites.  That's not to
say it doesn't work well -- it does!  But since it was created, a new protocol
for supporting async more natively in Python has been defined, called ASGI.  There
are a number of great new frameworks using ASGI, like FastAPI, FastHTML and the
newest version of Django.  You can find out how to use those on [our ASGI help page](/pages/ASGICommandLine).


## The API

If you want to control your ASGI site programatically, using Python code rather
than the `pa` command-line tool, check out [this help page](/pages/ASGIAPI).


