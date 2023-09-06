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

Deployment of FastAPI-based (and other async) web apps on PythonAnywhere is experimental feature that is possible to use, but not guaranteed to work yet.

Important limitations to know about:

 * http only (we are working on https) 
 * programmatic access with api only
 * no stability of the interface guaranteed

I you are brave enough to try it, here is quick guide how to do it.

The first step when using the API is to get an API token -- this is what you use to authenticate yourself with our servers when using it.  To do that, log in to PythonAnywhere, and go to the "Account" page using the link at the top right.  Click on the "API token" tab; if you don't already have a token, it will look like this:

<img width="500" src="/images/file-api-no-token-page.png">

Click the "Create a new API token" button to get your token, and you'll see this:

<img width="500" src="/images/file-api-with-token-page.png">

That string of letters and numbers (`d870f0cac74964b27db563aeda9e418565a0d60d` in the screenshot) is an API token, and anyone who has it can access your PythonAnywhere account and do stuff -- so keep it secret. If someone does somehow get hold of it, you can revoke it on this page by clicking the red button -- that stops it from working in the future, and creates a new one for you to use.

Now you can use our experimental API to deploy your FastAPI web app.

We suggest that you create virtual environment with `fastapi` and `uvicorn` installed (we assume that in the guide below)

To create an environment called `fast_venv` run `makevirtualenv fast_venv --python=python3.10` and then `pip install uvicorn fastapi`


Create a file `my_fastapi_app.py` with a simple minimal code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
        return {"message":"Hello from FastAPI"}
```

and put it into directory `/home/XXXX/fast_api_app` where XXXX is your PythonAnywhere username.

Now you can run simple code to start your app:

```python
from urllib.parse import urljoin

import requests

api_token = "YOUR TOKEN HERE"
username = "YOUR USERNAME HERE"
pythonanywhere_host = "www.pythonanywhere.com"

api_base = "https://{pythonanywhere_host}/api/v1/user/{username}/".format(
    pythonanywhere_host=pythonanywhere_host,
    username=username,
)

requests.post(
    urljoin(api_base, "websites/"),
    headers={"Authorization": "Token {api_token}".format(api_token=api_token)},
    json={
        "domain_name": f"{username}.pythonanywhere.com", 
        "enabled": True, 
        "webapp": {"command": f"/home/{username}/.virtualenvs/fast_venv/bin/uvicorn my_fastapi_app:app --uds $DOMAIN_SOCKET"}
    },
)
```

If you go to XXXX.pythonanywhere.com where XXXX is your PythonAnywhere username you should get `{"message":"Hello from FastAPI"}` back.

TODO:
 * other operations, list, delete, patch, enable/disable
 * explain uds