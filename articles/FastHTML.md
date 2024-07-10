<!--
.. title: Deploying FastHTML on PythonAnywhere (beta)
.. slug: FastHTML
.. date: 2024-06-10 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

# Disclaimer

Deployment of FastHTML-based (and other async) websites on PythonAnywhere is an
experimental feature that is possible to use, but not guaranteed to work yet.

Some important limitations to know about:

 * HTTPS is only available on default PythonAnywhere subdomains (e.g. `username.eu.pythonanywhere.com`)
 * There is no support for static file mappings
 * There is no support for HTTP password
 * There is no web UI for creating and managing ASGI websites -- it's API and command-line only
 * We do not guarantee that the command line syntax and the API interface will remain the same.

If you are brave enough to try it, here is a quick guide how to do it :-)

# Prerequisites

## API token

The first step when using the API is to get an API token -- this is what you use
to authenticate yourself with our servers when using it.  To do that, log in to
PythonAnywhere, and go to the "Account" page using the link at the top right.
Click on the "API token" tab; if you don't already have a token, it will look
like this:

<img alt="API token not set up" src="/api-token-needs-generation.png" class="bordered-image">

Click the "Create a new API token" button to get your token, and you'll see
this:

<img alt="API token set up" src="/api-token-set-up.png" class="bordered-image">

That string of letters and numbers (`d870f0cac74964b27db563aeda9e418565a0d60d`
in the screenshot) is the API token, and anyone who has it can access your
PythonAnywhere account and do stuff -- so keep it secret. If someone does
somehow get hold of it, you can revoke it on this page by clicking the red
button -- that stops it from working in the future, and creates a new one for
you to use.

Now you can use our command-line tools or our experimental API to deploy your
FastHTML website.  This help page will show you how to use the command-line
tools.

## First step: install the command-line tools

We'll be managing the website from a Bash console on PythonAnywhere, so the
first step is to install the command-line tools.  In a fresh Bash console, run

```bash
pip install --upgrade pythonanywhere
```

(As of this writing, it will print out an error about `typing-extensions`, but
you can ignore that.)

Running that install will make a new command, `pa` available, which we'll be
using later.


## Creating a simple test website

Now we'll create a simple site that we can deploy.


### Virtual environment

We suggest that you create a virtual environment with `python-fasthtml`
installed (it's assumed in the following guide).  To create an environment
called `fasthtml_venv`, run these commands in a Bash console:

```bash
mkvirtualenv fasthtml_venv --python=python3.10
pip install python-fasthtml
```


### The code of your website

Create a directory `~/my_fasthtml/` with a `main.py` file in it containing the following code:

```python
from fasthtml.common import FastHTML, H1, Title, P

app = FastHTML()
rt = app.route

@rt("/")
def get():
    return Title("Hello from FastHTML on PythonAnywhere"), H1("Hello world!"), P("I'm FastHTML on PythonAnywhere!")
```


## Managing your website

### Creating it

In Bash, to deploy your website to your subdomain -- that is, to
*yourusername*`.pythonanywhere.com` if you're on our US system, or
*yourusername*`.eu.pythonanywhere.com` if you're on the EU system -- just run this
command.  You'll need to replace the domain argument as appropriate, and put your own
username in place of `YOURUSERNAME` in the command:

```bash
pa website create --domain YOURUSERNAME.pythonanywhere.com --command '/home/YOURUSERNAME/.virtualenvs/fasthtml_venv/bin/uvicorn --uds $DOMAIN_SOCKET my_fasthtml.main:app'
```

If everything was successful, you should see something like:

```text
< All done! Your site is now live at YOURUSERNAME.pythonanywhere.com. >
   \
    ~<:>>>>>>>>>
```

Now, if you go to the website URL defined in `domain` you should get

```text
Hello world!
I'm FastHTML on PythonAnywhere!
```

You have a working FastHTML website hosted on PythonAnywhere!  However, this site
will not currently appear on the "Web" page inside your PythonAnywhere account;
we have a user interface that is a work-in-progress, though, and if you'd like
to try that out, [drop us a line](mailto:support@pythonanywhere.com).


### Getting and listing websites

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

...which will display something like this:

```text
STUFF
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

#### The server log

For example, `/var/log/YOURUSERNAME.pythonanywhere.com.server.log`.

By default, uvicorn logs incoming requests to the standard output stream, so
you'll see something like this:

```text
INFO:      - "GET / HTTP/1.1" 200 OK
```

#### The access log

For example, `/var/log/YOURUSERNAME.pythonanywhere.com.access.log`.

This will also show incoming requests, but will be formatted similarly to other
PythonAnywhere websites -- for example:

```text
1.2.3.4 - - [17/Oct/2023:13:14:00 +0000] "GET / HTTP/1.1" 200 32 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" "1.2.3.4" response-time=0.286
```


## Technical details

If you just want to get FastHTML up and running, all you need to do is follow
the recipe above.  However, if you'd like to understand a bit more about what is
going on, or to build on these instructions to do more than just FastHTML, read on!

The command that we are providing for our FastHTML site in the instructions above is this:

```text
/home/YOURUSERNAME/.virtualenvs/fasthtml_venv/bin/uvicorn my_fasthtml.main:app --uds $DOMAIN_SOCKET
```

Breaking that down:

* `/home/YOURUSERNAME/.virtualenvs/fasthtml_venv/bin/uvicorn` is the path to uvicorn in your virtualenv.  Uvicorn is an ASGI container program -- it can run any ASGI-based Python web framework, like FastHTML, FastAPI, or recent versions of Django.
* `my_fasthtml.main:app` is telling uvicorn, which is running in your home directory `~`, to load up the ASGI app called `app` from the file `my_fasthtml/main.py`
* `--uds $DOMAIN_SOCKET` is telling uvicorn to listen for incoming requests on a unix domain socket -- the location of that socket is provided by our system in the environment variable `DOMAIN_SOCKET`

As we mentioned above, that domain socket (which will be something like
`/var/sockets/YOURUSERNAME.pythonanywhere.com/app.sock`) is internal to the
part of our system that serves websites; you won't be able to see
it in a console or on the "Files" page inside PythonAnywhere.

If you want to use an ASGI framework that is not FastHTML, you should be able to
get it up an running just by changing the first argument to point to the ASGI
object that your framework exports.

But in addition, you can even use our new website hosting system to host non-ASGI
servers!  It supports any server that is able to listen for incoming requests on a unix domain socket.
You'll just need to work out the appropriate incantation to tell it how to
listen on the socket provided in `$DOMAIN_SOCKET`.

### Optional `uvicorn` command arguments

* `--app-dir <path>`: add this argument to the command if your app's code uses multiple files that are not currently on the Python path.

For example if you have file structure like this:

```
foo/
└── bar
    ├── main.py
    └── baz
        ├── module_a.py
        └── module_b.py
```

where `foo` is a directory in your home directory, and `main.py` relies on imports from `baz/module_*` files, then your command should look like this:

```python
command = (
    f"/home/{username}/.virtualenvs/fasthtml_venv/bin/uvicorn "
    f"--app-dir /home/{username}/foo/bar "
    "--uds $DOMAIN_SOCKET "
    "main:app "
)
```

### The API

If you want to control your ASGI site programatically, using Python code rather
than the `pa` command-line tool, check out [this help page](/pages/ASGIAPI).


