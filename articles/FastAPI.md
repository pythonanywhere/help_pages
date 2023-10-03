<!--
.. title: Deploying FastAPI on PythonAnywhere (beta)
.. slug: FastAPI
.. date: 2023-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

# Disclaimer

Deployment of FastAPI-based (and other async) web apps on PythonAnywhere is experimental feature that is possible to use, but not guaranteed to work yet.

Important limitations to know about:

 * HTTPS only on default PythonAnywhere subdomains (e.g. `username.eu.pythonanywhere.com`)
 * no support for static files mappings
 * no support for HTTP password
 * programmatic management with API only (no web UI)
 * no stability of the interface guaranteed

If you are brave enough to try it, here is a quick guide how to do it.

# Prerequisites

## API token

The first step when using the API is to get an API token -- this is what you use to authenticate yourself with our servers when using it.  To do that, log in to PythonAnywhere, and go to the "Account" page using the link at the top right.  Click on the "API token" tab; if you don't already have a token, it will look like this:

<img width="500" src="/images/file-api-no-token-page.png">

Click the "Create a new API token" button to get your token, and you'll see this:

<img width="500" src="/images/file-api-with-token-page.png">

That string of letters and numbers (`d870f0cac74964b27db563aeda9e418565a0d60d` in the screenshot) is the API token, and anyone who has it can access your PythonAnywhere account and do stuff -- so keep it secret. If someone does somehow get hold of it, you can revoke it on this page by clicking the red button -- that stops it from working in the future, and creates a new one for you to use.

Now you can use our experimental API to deploy your FastAPI web app.

## Virtual environment

We suggest to create a virtual environment with `fastapi` and `uvicorn` installed (it's assumed in the following guide).

To create an environment called `fast_venv` run:

```bash
mkvirtualenv fast_venv --python=python3.10 
# and then 
pip install uvicorn fastapi
```


## The code of your web app

Create a directory `~/my_fastapi/` with `main.py` file in it containing the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello from FastAPI"}
```


# Manage your web app via API

## Create

Now you can run this simple code to create your app (for simplicity, we assume the
PythonAnywhere username is `xanthippe`) -- we will use `uvicorn` to serve it:

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
    f"/home/{username}/.virtualenvs/fast_venv/bin/uvicorn "
    "--uds $DOMAIN_SOCKET"  # DOMAIN_SOCKET is an environment variable provided by us
    "my_fastapi.main:app "
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
 'webapp': {'command': '/home/xanthippe/.virtualenvs/fast_venv/bin/uvicorn '
                       'my_fastapi.main:app --uds $DOMAIN_SOCKET',
            'domains': [{'domain_name': 'xanthippe.eu.pythonanywhere.com',
                         'enabled': True}],
            'id': 42}}
```

Finally, if you go to `domain_name` you should get `{"message":"Hello from FastAPI"}` back.

However, this web app will not currently appear in the UI on your PythonAnywhere account!

## Delete

To delete your FastAPI web app, use the following code -- mind the `/` at the end of the endpoint!

```python

# the same setup as above...

response = requests.delete(
    urljoin(api_base, f"websites/{domain_name}/"),
    headers=headers
)
print(response)
```

You should get `204` on successful delete.

## Reload (or disable/enable)

If you want to change the code of your web app, you need to disable and re-enable it, after making the changes.  That's an equivalent of reloading the web app.

```python

# the same setup as above...

endpoint = urljoin(api_base, f"websites/{domain_name}/")
# disable:
requests.patch(endpoint, headers=headers, json={"enabled": False})
# enable:
requests.patch(endpoint, headers=headers, json={"enabled": True})
```

However, if you'd like to update the serving `command`, you'd need to delete the current app, and re-deploy it with a new one. 

To only disable the web app, just run the first request (setting the `enabled` state to `False`).  Once you want to re-enable it, you can set it to `True` again.

# Supported UI features

## Logs

You can access the logs using the **Files** tab and going to `/var/log` directory.

Sample logs (when serving with 
[the default uvicorn logging](https://github.com/encode/uvicorn/blob/40b99b8436c0c261e3a85d10e291424072946292/uvicorn/config.py#L74)
) would look like:

* **error log**, e.g. `/var/log/xanthippe.eu.pythonanywhere.com.error.log`:

```text
INFO:     Started server process [1]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on unix socket /var/sockets/xanthippe.eu.pythonanywhere.com/app.sock (Press CTRL+C to quit)
```

* **server log**, e.g. `/var/log/xanthippe.eu.pythonanywhere.com.server.log`:

```text
INFO:      - "GET / HTTP/1.1" 200 OK
```

**Access log** will show the `nginx` logs, similarly to other PythonAnywhere web apps.

<!-- # TODO: -->
<!--  * other operations, list, delete, patch, enable/disable -->
<!--  * explain uds -->
