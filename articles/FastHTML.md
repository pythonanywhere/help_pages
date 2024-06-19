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

Deployment of FastHTML-based (and other async) web apps on PythonAnywhere is an experimental feature that is possible to use, but not guaranteed to work yet.

Some important limitations to know about:

 * HTTPS is only available on default PythonAnywhere subdomains (e.g. `username.eu.pythonanywhere.com`)
 * There is no support for static file mappings
 * There is no support for HTTP password
 * There is no web UI for creating and managing ASGI websites -- it's API-only
 * We do not guarantee that the API interface will remain the same.

If you are brave enough to try it, here is a quick guide how to do it.

# Prerequisites

## API token

The first step when using the API is to get an API token -- this is what you use to authenticate yourself with our servers when using it.  To do that, log in to PythonAnywhere, and go to the "Account" page using the link at the top right.  Click on the "API token" tab; if you don't already have a token, it will look like this:

<img alt="API token not set up" src="/api-token-needs-generation.png" class="bordered-image">

Click the "Create a new API token" button to get your token, and you'll see this:

<img alt="API token set up" src="/api-token-set-up.png" class="bordered-image">

That string of letters and numbers (`d870f0cac74964b27db563aeda9e418565a0d60d` in the screenshot) is the API token, and anyone who has it can access your PythonAnywhere account and do stuff -- so keep it secret. If someone does somehow get hold of it, you can revoke it on this page by clicking the red button -- that stops it from working in the future, and creates a new one for you to use.

Now you can use our experimental API to deploy your FastHTML web app.

## Virtual environment

We suggest that you create a virtual environment with `requests`, `python-fasthtml`, `sqlite-utils` and `uvicorn` installed (it's assumed in the following guide).

To create an environment called `fasthtml_venv` run this code in a Bash console:

```bash
mkvirtualenv fasthtml_venv --python=python3.10
# and then
pip install requests "uvicorn[standard]" python-fasthtml sqlite-utils
```


## The code of your web app

Create a directory `~/my_fasthtml/` with a `main.py` file in it containing the following code:

```python
from fasthtml.common import FastHTML, H1, Title, P

app = FastHTML()
rt = app.route

@rt("/")
def get():
    return Title("Hello from FastHTML on PythonAnywhere"), H1("Hello world!"), P("I'm FastHTML on PythonAnywhere!")
```

**Caveat**: If your app's code consists of multiple files which are not located in your home
directory, you'd need to add extra argument (`--app-dir`) to the `uvicorn` command,
see
[Optional `uvicorn` command arguments](#optional-uvicorn-command-arguments)
section below.

# Manage your web app via API

## Create

Now you can run run `python` in your virtualenv, and run this code to create your app (for simplicity, we assume the
PythonAnywhere username is `xanthippe`) -- we will use `uvicorn` to serve it. Don't
worry about the details of the uvicorn command for now,
[we'll explain it later](#technical-details).

```python
from pprint import pprint
from urllib.parse import urljoin

import requests


api_token = "YOUR TOKEN HERE"
headers = {"Authorization": f"Token {api_token}"}

username = "xanthippe"  # update to match your USERNAME!

pythonanywhere_host = "www.pythonanywhere.com"  # or "eu.pythonanywhere.com" if your account is hosted on our EU servers
pythonanywhere_domain = "pythonanywhere.com"  # or "eu.pythonanywhere.com"

# make sure you don't use this domain already!
domain_name = f"{username}.{pythonanywhere_domain}"

api_base = f"https://{pythonanywhere_host}/api/v1/user/{username}/"
command = (
    f"/home/{username}/.virtualenvs/fasthtml_venv/bin/uvicorn "
    "--uds $DOMAIN_SOCKET "
    "my_fasthtml.main:app "
)

response = requests.post(
    urljoin(api_base, "websites/"),
    headers=headers,
    json={
        "domain_name": domain_name,
        "enabled": True,
        "webapp": {"command": command}
    },
)
pprint(response.json())
```

If everything was successful, you should see something like:

```python
{'domain_name': 'xanthippe.eu.pythonanywhere.com',
 'enabled': True,
 'id': 42,
 'user': 'xanthippe,
 'webapp': {'command': '/home/xanthippe/.virtualenvs/fasthtml_venv/bin/uvicorn '
                       'my_fasthtml.main:app --uds $DOMAIN_SOCKET',
            'domains': [{'domain_name': 'xanthippe.eu.pythonanywhere.com',
                         'enabled': True}],
            'id': 42}}
```

Now, if you go to the website URL defined in `domain_name` you should get

```text
Hello world!
I'm FastHTML on PythonAnywhere!
```

You have a working FastHTML website hosted on PythonAnywhere!  However, this site
will not currently appear on the "Web" page inside your PythonAnywhere account;
we have a user interface that is a work-in-progress, though, and if you'd like
to try that out, [drop us a line](mailto:support@pythonanywhere.com).


## Getting and listing webapps

If you do a "get" request to the `websites/` API endpoint, you'll get a list
of your websites:

```python

# the same setup as above...

endpoint = urljoin(api_base, "websites/")
response = requests.get(endpoint, headers=headers)
pprint(response.json())
```

...will give you something like this:

```python
[{'domain_name': 'xanthippe.eu.pythonanywhere.com',
  'enabled': True,
  'id': 42,
  'user': 'xanthippe,
  'webapp': {'command': '/home/xanthippe/.virtualenvs/fasthtml_venv/bin/uvicorn '
                        'my_fasthtml.main:app --uds $DOMAIN_SOCKET',
             'domains': [{'domain_name': 'xanthippe.eu.pythonanywhere.com',
                          'enabled': True}],
             'id': 42}}]
```

Likewise, you can get the information about a particular website by getting
it:

```python

# the same setup as above...

endpoint = urljoin(api_base, f"websites/{domain_name}/")
response = requests.get(endpoint, headers=headers)
pprint(response.json())
```

...and you'll get this:

```python
{'domain_name': 'xanthippe.eu.pythonanywhere.com',
 'enabled': True,
 'id': 42,
 'user': 'xanthippe,
 'webapp': {'command': '/home/xanthippe/.virtualenvs/fasthtml_venv/bin/uvicorn '
                       'my_fasthtml.main:app --uds $DOMAIN_SOCKET',
            'domains': [{'domain_name': 'xanthippe.eu.pythonanywhere.com',
                         'enabled': True}],
            'id': 42}}
```


## Reload (or disable/enable)

If you want to change the code of your web app, you need to disable and re-enable it, after making the changes.  That's an equivalent of reloading the web app.

```python

# the same setup as above...

endpoint = urljoin(api_base, f"websites/{domain_name}/")
# disable:
response = requests.patch(endpoint, headers=headers, json={"enabled": False})
print(response)
# enable:
response = requests.patch(endpoint, headers=headers, json={"enabled": True})
print(response)
```

However, `enabled` is the only property of the website that you can patch -- if you'd like to update the serving `command`, you'll need to delete the current app, and re-deploy it with a new one.

To only disable the web app, just run the first request (setting the `enabled` state to `False`).  Once you want to re-enable it, you can set it to `True` again.


## Delete

To delete your FastHTML web app, use the following code -- mind the `/` at the end of the endpoint!

```python

# the same setup as above...

response = requests.delete(
    urljoin(api_base, f"websites/{domain_name}/"),
    headers=headers
)
print(response)
```

You should get `204` on successful delete.


# Supported UI features

## Logs

You can access the logs from the **Files** page or from a console; they're located
in `/var/log`.

### The error log

For example, `/var/log/xanthippe.eu.pythonanywhere.com.error.log`.

By default, uvicorn logs its status messages to the standard error stream, so
if all is well you'll see something like this:

```text
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on unix socket /var/sockets/xanthippe.eu.pythonanywhere.com/app.sock (Press CTRL+C to quit)
```

The last line is uvicorn saying that it has successfully started, and is listening
for incoming requests on an internal [unix domain socket](https://en.wikipedia.org/wiki/Unix_domain_socket).
That socket is internal to our web-hosting system -- you won't be able to see
it in a console or on the "Files" page inside PythonAnywhere.

### The server log

For example, `/var/log/xanthippe.eu.pythonanywhere.com.server.log`.

By default, uvicorn logs incoming requests to the standard output stream, so
you'll see something like this:

```text
INFO:      - "GET / HTTP/1.1" 200 OK
```

### The access log

For example, `/var/log/xanthippe.eu.pythonanywhere.com.access.log`.

This will also show incoming requests, but will be formatted similarly to other
PythonAnywhere web apps -- for example:

```text
1.2.3.4 - - [17/Oct/2023:13:14:00 +0000] "GET / HTTP/1.1" 200 32 "-" "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36" "1.2.3.4" response-time=0.286
```


# Technical details

If you just want to get FastHTML up and running, all you need to do is follow
the recipe above.  However, if you'd like to understand a bit more about what is
going on, or to build on these instructions to do more than just FastHTML, read on!

The command that we are providing for our FastHTML site in the instructions above is this:

```text
/home/xanthippe/.virtualenvs/fasthtml_venv/bin/uvicorn my_fasthtml.main:app --uds $DOMAIN_SOCKET
```

Breaking that down:

* `/home/xanthippe/.virtualenvs/fasthtml_venv/bin/uvicorn` is the path to uvicorn in your virtualenv
* `my_fasthtml.main:app` is telling uvicorn, which is running in your home directory `/home/xanthippe/`, to load up the ASGI app called `app` from the file `my_fasthtml/main.py`
* `--uds $DOMAIN_SOCKET` is telling uvicorn to listen for incoming requests on a unix domain socket -- the location of that socket is provided by our system in the environment variable `DOMAIN_SOCKET`

As we mentioned above, that domain socket (which will be something like
`/var/sockets/xanthippe.eu.pythonanywhere.com/app.sock`) is internal to the
part of our system that serves websites; you won't be able to see
it in a console or on the "Files" page inside PythonAnywhere.

If you want to use an ASGI framework that is not FastHTML, you should be able to
get it up an running just by changing the first argument to point to the ASGI
object that your framework exports.

But in addition, you can even use our new website hosting system to host non-ASGI
servers!  It supports any server that is able to listen for incoming requests on a unix domain socket.
You'll just need to work out the appropriate incantation to tell it how to
listen on the socket provided in `$DOMAIN_SOCKET`.

## Optional `uvicorn` command arguments

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

