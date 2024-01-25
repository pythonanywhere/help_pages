<!--
.. title: Deploying Async Django web app on PythonAnywhere (beta)
.. slug: AsgiDjango
.. date: 2023-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

# Disclaimer

Deployment of Django async web apps on PythonAnywhere is an experimental feature that is possible to use, but not guaranteed to work yet.

Some important limitations to know about:

 * HTTPS is only available on default PythonAnywhere subdomains (e.g. `username.eu.pythonanywhere.com` or `username.pythonanywhere.com`)
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

Now you can use our experimental API to deploy your FastAPI web app.

## Virtual environment

We suggest that you create a virtual environment with `requests`, `fastapi` and `uvicorn` installed (it's assumed in the following guide).

To create an environment called `async_django_venv` run:

```bash
mkvirtualenv async_django_venv --python=python3.10
# and then
pip install requests "uvicorn[standard]" django
```


## The code of your web app

In your home directory run the following command to create a basic Django project in `~/asyncdjango/`:

```bash
django-admin startproject asyncdjango
```

Modify `~/asyncdjango/asyncdjango/url.py` to look like this:

```python
from django.urls import path
from django.http import JsonResponse


async def async_view(request):
    return JsonResponse({'message': 'Hello from async Django!'})

urlpatterns = [
    path("", async_view),
]
```

# Manage your web app via API

## Create

Now you can run this simple code to create your app (for simplicity, we assume the
PythonAnywhere username is `xanthippe`) -- we will use `uvicorn` to serve it. Don't
worry about the details of the uvicorn command for now, we'll explain it later.

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
    f"/home/{username}/.virtualenvs/async_django_venv/bin/uvicorn "
    f"--app-dir /home/{username}/asyncdjango "
    "--uds $DOMAIN_SOCKET "
    "asyncdjango.asgi:application "
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
 'webapp': {'command': '/home/xanthippe/.virtualenvs/async_django_venv/bin/uvicorn '
                       '--app-dir /home/xanthippe/asyncdjango '
                       '--uds $DOMAIN_SOCKET '
                       'asyncdjango.asgi:application',
            'domains': [{'domain_name': 'xanthippe.eu.pythonanywhere.com',
                         'enabled': True}],
            'id': 42}}
```

Now, if you go to the website URL defined in `domain_name` you should get

```text
{"message":"Hello from async Django!"}
```

You have a working async Django website hosted on PythonAnywhere!  However, this site
will not currently appear on the "Web" page inside your PythonAnywhere account.


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
 'webapp': {'command': '/home/xanthippe/.virtualenvs/async_django_venv/bin/uvicorn '
                       '--app-dir /home/xanthippe/asyncdjango '
                       '--uds $DOMAIN_SOCKET '
                       'asyncdjango.asgi:application',
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
 'webapp': {'command': '/home/xanthippe/.virtualenvs/async_django_venv/bin/uvicorn '
                       '--app-dir /home/xanthippe/asyncdjango '
                       '--uds $DOMAIN_SOCKET '
                       'asyncdjango.asgi:application',
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

To delete your async web app, use the following code -- mind the `/` at the end of the endpoint!

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
Not Found: /favicon.ico
```

The penultimate line is uvicorn saying that it has successfully started, and is listening
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

If you just want to get async Django up and running, all you need to do is follow
the recipe above.  However, if you'd like to understand a bit more about what is
going on, or to build on these instructions to do more than just async Django, read on!

The command that we are providing for our FastAPI site in the instructions above is this:

```text
/home/xanthippe/.virtualenvs/async_django_venv/bin/uvicorn --app-dir /home/xanthippe/asyncdjango --uds $DOMAIN_SOCKET asyncdjango.asgi:application 
```

Breaking that down:

* `/home/xanthippe/.virtualenvs/async_django_venv/bin/uvicorn` is the path to uvicorn in your virtualenv
* `--uds $DOMAIN_SOCKET` is telling uvicorn to listen for incoming requests on a unix domain socket -- the location of that socket is provided by our system in the environment variable `DOMAIN_SOCKET`
* `--app-dir /home/xanthippe/asyncdjango` is telling uvicorn to add the directory `/home/xanthippe/asyncdjango` to the Python path, so that it can find the `asyncdjango`
* `asyncdjango.asgi:application` is telling uvicorn, to load up the ASGI app called `application` from the file `asyncdjango/asgi.py`

As we mentioned above, that domain socket (which will be something like
`/var/sockets/xanthippe.eu.pythonanywhere.com/app.sock`) is internal to the
part of our system that serves websites; you won't be able to see
it in a console or on the "Files" page inside PythonAnywhere.

