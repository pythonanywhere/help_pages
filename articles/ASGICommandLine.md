<!--
.. title: Deploying ASGI sites on PythonAnywhere (beta)
.. slug: ASGICommandLine
.. date: 2024-06-10 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

# Disclaimer

This help page explains how to set up an ASGI site on PythonAnywhere -- for
example, one based on the FastHTML or FastAPI frameworks, or using the latest
Django async features.  We have a separate help page for [Flask-SocketIO](/pages/FlaskSocketIO),
which uses a non-ASGI system.

**Note:** deployment of ASGI (and other async) websites on PythonAnywhere is an
experimental feature.  Some important limitations to know about:

 * There is no support for static file mappings.
 * There is a very limited web UI for creating and managing async websites.
   Contact [support@pythonanywhere.com](mailto:support@pythonanywhere.com) if
   you would like us to enable it for your account.
 * We do not guarantee that the command line syntax and the API interface will remain the same.
 * We have not worked out the long-term pricing for ASGI sites, which will probably
   differ from the way we charge for traditional WSGI ones.  We're 99.9% certain that
   there will be a way to host them in a free plan, though!

If you are brave enough to try it, here is a quick guide on how to do it :-)

# Prerequisites

## API token

This help page explains how to manage your websites using our `pa` command-line
tool rather than the API, but you'll need to generate an API token so that
that tool knows how to connect to PythonAnywhere.

First, you will need an API token. [This page](/pages/GettingYourAPIToken) will
show you how to get that.

Now you can use our command-line tool or our experimental API to deploy your
ASGI website.  This help page will show you how to use the command-line
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


# Creating a simple test website

Now we'll create a simple site that we can deploy.  Exactly how you do that
depends on the web framework you want to use:

* [FastHTML](#fasthtml)
* [FastAPI](#fastapi)
* [Django](#django)


## FastHTML

Firstly, create a virtual environment with `python-fasthtml`
installed.  In your Bash console:

```bash
mkvirtualenv my_venv --python=python3.10
```

...and then:

```
pip install python-fasthtml
```

Next, we'll create a minimal FastHTML site.  Create a directory `~/my_fasthtml/`
and inside it create a file called `main.py`, containing the following code:

```python
from fasthtml.common import FastHTML, H1, Title, P

app = FastHTML()
rt = app.route

@rt("/")
def get():
    return Title("Hello from FastHTML on PythonAnywhere"), H1("Hello world!"), P("I'm FastHTML on PythonAnywhere!")
```

That's enough setup!  The only other thing you'll need to know to run your site
is the *command* that you will later on provide when creating it; we'll explain
the details of this later on, but for now, just note down that it should be this:

```bash
/home/YOURUSERNAME/.virtualenvs/my_venv/bin/uvicorn --app-dir /home/YOURUSERNAME/my_fasthtml --uds ${DOMAIN_SOCKET} main:app
```

...with `YOURUSERNAME` replaced by your actual username, but with everything else
exactly as it is.

Now you can move on to [creating your website](#creating-your-website)

## FastAPI

Firstly, create a virtual environment with `fastapi` and `uvicorn`
installed.  In your Bash console:

```bash
mkvirtualenv my_venv --python=python3.10
```

...and then:

```
pip install "uvicorn[standard]" fastapi
```

Next, we'll create a minimal FastAPI site.  Create a directory `~/my_fastapi/`
and inside it create a file called `main.py`, containing the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello from FastAPI"}
```

That's enough setup!  The only other thing you'll need to know to run your site
is the *command* that you will later on provide when creating it; we'll explain
the details of this later on, but for now, just note down that it should be this:

```bash
/home/YOURUSERNAME/.virtualenvs/my_venv/bin/uvicorn --app-dir /home/YOURUSERNAME/my_fastapi --uds ${DOMAIN_SOCKET} main:app
```

...with `YOURUSERNAME` replaced by your actual username, but with everything else
exactly as it is.

Now you can move on to [creating your website](#creating-your-website)

## Django

Firstly, create a virtual environment with `django` and `uvicorn`
installed.  In your Bash console:

```bash
mkvirtualenv my_venv --python=python3.10
```

...and then:

```
pip install "uvicorn[standard]" django
```

Next, we'll create a minimal Django site.  Firstly, in your Bash console,
run this:

```bash
django-admin startproject asyncdjango
```

Modify `~/asyncdjango/asyncdjango/urls.py` to look like this:

```python
from django.urls import path
from django.http import JsonResponse


async def async_view(request):
    return JsonResponse({'message': 'Hello from async Django!'})

urlpatterns = [
    path("", async_view),
]
```

That's enough setup!  The only other thing you'll need to know to run your site
is the *command* that you will later on provide when creating it; we'll explain
the details of this later on, but for now, just note down that it should be this:

```bash
/home/YOURUSERNAME/.virtualenvs/my_venv/bin/uvicorn --app-dir /home/YOURUSERNAME/asyncdjango --uds $DOMAIN_SOCKET asyncdjango.asgi:application
```

...with `YOURUSERNAME` replaced by your actual username, but with everything else
exactly as it is.

Now you can move on to [creating your website](#creating-your-website)


# Managing your website

## Creating your website

In Bash, to deploy your website to your subdomain -- that is, to
*yourusername*`.pythonanywhere.com` if you're on our US system, or
*yourusername*`.eu.pythonanywhere.com` if you're on the EU system -- just run
the following.  You'll need to replace the domain argument as appropriate, and
put the framework-specific command that you noted down earlier inside the single
quotes in place of `COMMAND`.


```bash
pa website create --domain YOURUSERNAME.pythonanywhere.com --command 'COMMAND'
```

If everything was successful, you should see something like:

```text
< All done! Your site is now live at YOURUSERNAME.pythonanywhere.com. >
   \
    ~<:>>>>>>>>>
```

Now, if you go to the website URL defined in `domain` you should get something
back from your website -- exactly what, of course, depends on which of the
frameworks you chose agove.

*Note:* as of this writing, there is a bug that means that you might get a 404
not found page for a few seconds before the site comes up.  If you get that,
just refresh the page in your browser.  We're on the case :-)

You have a working ASGI website hosted on PythonAnywhere!  However, this site
will not currently appear on the "Web" page inside your PythonAnywhere account;
we have a user interface that is a work-in-progress, though, and if you'd like
to try that out, [drop us a line](mailto:support@pythonanywhere.com).


## Getting and listing websites

You can get a list of ASGI websites from PythonAnywhere with this command:

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

...which will display something like this (the command will of course vary based
on the framework you're using):

```text
-----------  -------------------------------------------------------------------------------------------------------------------------
domain name  YOURUSERNAME.pythonanywhere.com
enabled      True
command      /home/YOURUSERNAME/.virtualenvs/my_venv/bin/uvicorn --app-dir /home/YOURUSERNAME/my_fastapi --uds ${DOMAIN_SOCKET} main:app
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

By default, uvicorn logs its status messages to the standard error stream, so
if all is well you'll see something like this:

```text
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on unix socket /var/sockets/YOURUSERNAME.pythonanywhere.com/app.sock (Press CTRL+C to quit)
```

The last line is uvicorn saying that it has successfully started, and is listening
for incoming requests on an internal [unix domain socket](https://en.wikipedia.org/wiki/Unix_domain_socket).
That socket is internal to our web-hosting system -- you won't be able to see
it in a console or on the "Files" page inside PythonAnywhere.

### The server log

For example, `/var/log/YOURUSERNAME.pythonanywhere.com.server.log`.

By default, uvicorn logs incoming requests to the standard output stream, so
you'll see something like this:

```text
INFO:      - "GET / HTTP/1.1" 200 OK
```

### The access log

For example, `/var/log/YOURUSERNAME.pythonanywhere.com.access.log`.

This will also show incoming requests, but will be formatted similarly to other
PythonAnywhere websites -- for example:

```text
1.2.3.4 - - [17/Oct/2023:13:14:00 +0000] "GET / HTTP/1.1" 200 32 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" "1.2.3.4" response-time=0.286
```


# Technical details

If you just want to get an ASGI site up and running, all you need to do is follow
the recipe above.  However, if you'd like to understand a bit more about what is
going on, or to build on these instructions to do more than just ASGI, read on!

As an example, let's use the command that we specified for FastAPI

```text
/home/YOURUSERNAME/.virtualenvs/my_venv/bin/uvicorn --app-dir /home/YOURUSERNAME/my_fastapi --uds ${DOMAIN_SOCKET} main:app
```

Breaking that down:

* `/home/YOURUSERNAME/.virtualenvs/my_venv/bin/uvicorn` is the path to uvicorn in your virtualenv.  Uvicorn is an ASGI container program -- it can run any ASGI-based Python web framework, like FastHTML, FastAPI, or recent versions of Django.
* `--app-dir /home/YOURUSERNAME/my_fastapi` is the directory containing your website's code -- in this example, the FastAPI example.
* `--uds ${DOMAIN_SOCKET}` is telling uvicorn to listen for incoming requests on a unix domain socket -- the location of that socket is provided by our system in the environment variable `DOMAIN_SOCKET`
* `main:app` is telling uvicorn, which is looking for code in the specified `app-dir`, to load up the ASGI app called `app` from the file `main.py`.  If you're using Django, it will be a little more complicated because of the way Django nests directories.

As we mentioned above, that domain socket (which will be something like
`/var/sockets/YOURUSERNAME.pythonanywhere.com/app.sock`) is internal to the
part of our system that serves websites; you won't be able to see
it in a console or on the "Files" page inside PythonAnywhere.

If you want to use an ASGI framework that is not one of the ones we have examples
for above, you should be able to
get it up and running by:

* Installing the framework into your virtualenv.
* Adjusting the `app-dir` to point to the location of your code.
* Changing the last argument to point to the ASGI object that your framework exports.

But in addition, you can even use our new website hosting system to host non-ASGI
servers!  It supports any server that is able to listen for incoming requests on a unix domain socket.
You'll just need to work out the appropriate incantation to tell it how to
listen on the socket provided in `$DOMAIN_SOCKET`.

# The API

If you want to control your ASGI site programatically, using Python code rather
than the `pa` command-line tool, check out [this help page](/pages/ASGIAPI).


