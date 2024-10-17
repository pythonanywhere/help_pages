<!--
.. title: Using the API to run ASGI sites on PythonAnywhere (beta)
.. slug: ASGIAPI
.. date: 2024-07-10 14:30:00 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

# Disclaimer

Deployment of ASGI-based (and other async) websites on PythonAnywhere is an
experimental feature.  Some important limitations to know about:

 * There is no support for static file mappings.
 * There is a very limited web UI for creating and managing async websites.
   Contact [support@pythonanywhere.com](mailto:support@pythonanywhere.com) if
   you would like us to enable it for your account.
 * We do not guarantee that the command line syntax and the API interface will remain the same.
 * We have not worked out the long-term pricing for ASGI sites, which will probably
   differ from the way we charge for traditional WSGI ones.  We're 99.9% certain that
   there will be a way to host them in a free plan, though!

If you are brave enough to try it, here is a quick guide how to do it using our
API.

**Note:** if you're just getting started with ASGI-based sites on
PythonAnywhere, we recommend that
you set them up using our `pa` command-line tool.  This provides the same
functionality as the API, but wrapped up so that you can quickly and easily use
it from Bash.  The API is generally only a better option if you're trying to
automate things.

We have [a help page on using the `pa` command-line tool](/pages/ASGICommandLine),
and we suggest that you go through at least one of the examples there before
trying the API.

If you've already done that, then read on!


## Prerequisites

### API token

The first step when using the API is to get an API token -- this is what you use
to authenticate yourself with our servers when using it.  To do that, log in to
PythonAnywhere, and go to the "Account" page using the link at the top right.
Click on the "API token" tab; if you don't already have a token, it will look
like this:

<img alt="API token not set up" src="/api-token-needs-generation.png" class="bordered-image">

Click the "Create a new API token" button to get your token, and you'll see this:

<img alt="API token set up" src="/api-token-set-up.png" class="bordered-image">

That string of letters and numbers (masked out
in the screenshot) is the API token, and anyone who has it can access your
PythonAnywhere account and do stuff -- so keep it secret. If someone does
somehow get hold of it, you can revoke it on this page by clicking the red
button -- that stops it from working in the future, and creates a new one for
you to use.

Now you can use our experimental API to deploy your website.  Note down the API
token, as you'll be using it in the code samples below.

## Creating a simple website to test against

We'll use FastAPI
as the example in this page, but the others are similar -- you'd just need to
change the command provided when creating the site, just as you would when using
the `pa` command-line tool.

### Virtual environment

Firstly, create a virtual environment with `requests`, `fastapi` and
`uvicorn` installed.

To create an environment called `fast_venv` run:

```bash
mkvirtualenv fast_venv --python=python3.10
```

...and then install the requirements:

```bash
pip install requests "uvicorn[standard]" fastapi
```


### The code of your website

Create a directory `~/my_fastapi/`.  In that directory, create a file called
`main.py`, with the following code:

```python
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message":"Hello from FastAPI"}
```

## Managing your website via the API

### Creating it

Now you can access the API to create your website.  Run `python` in your Bash
console, and then use the following code.  Don't forget to replace
`YOUR TOKEN HERE` with your actual API token, `YOURUSERNAME` with your
PythonAnywhere username, and to use the correct values for `pythonanywhere_host`
and `pythonanywhere_domain` based on whether your account is on our US-based
system at `www.pythonanywhere.com`, or our EU-based system at
`eu.pythonanywhere.com`.

```python
from pprint import pprint
from urllib.parse import urljoin

import requests


api_token = "YOUR TOKEN HERE" # Update to match your real API token
headers = {"Authorization": f"Token {api_token}"}

username = "YOURUSERNAME"  # update to match your username!

pythonanywhere_host = "www.pythonanywhere.com"  # or "eu.pythonanywhere.com" if your account is hosted on our EU servers
pythonanywhere_domain = "pythonanywhere.com"  # or "eu.pythonanywhere.com"

# make sure you don't use this domain already!
domain_name = f"{username}.{pythonanywhere_domain}"

api_base = f"https://{pythonanywhere_host}/api/v1/user/{username}/"
command = (
    f"/home/{username}/.virtualenvs/fast_venv/bin/uvicorn "
    "--uds $DOMAIN_SOCKET "
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

If you've used the `pa` command-line tool previously, you'll probably spot that
the `domain_name` and the `command` are
the same as the parameters that you would use with it.  The rest is the
boilerplate you need to write to access the API using `requests`.

If everything was successful, you should see something like:

```python
{'domain_name': 'YOURUSERNAME.pythonanywhere.com',
 'enabled': True,
 'id': 42,
 'user': 'YOURUSERNAME,
 'webapp': {'command': '/home/YOURUSERNAME/.virtualenvs/fast_venv/bin/uvicorn '
                       'my_fastapi.main:app --uds $DOMAIN_SOCKET',
            'domains': [{'domain_name': 'YOURUSERNAME.pythonanywhere.com',
                         'enabled': True}],
            'id': 42}}
```

Now, if you go to the website URL defined in `domain_name` you should get

```text
{"message":"Hello from FastAPI"}
```

You have a working FastAPI website hosted on PythonAnywhere, created via our
API.


### Getting and listing websites

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
[{'domain_name': 'YOURUSERNAME.pythonanywhere.com',
  'enabled': True,
  'id': 42,
  'user': 'YOURUSERNAME,
  'webapp': {'command': '/home/YOURUSERNAME/.virtualenvs/fast_venv/bin/uvicorn '
                        'my_fastapi.main:app --uds $DOMAIN_SOCKET',
             'domains': [{'domain_name': 'YOURUSERNAME.pythonanywhere.com',
                          'enabled': True}],
             'id': 42}}]
```

Likewise, you can get the information about a particular website by adding its
domain name, and a trailing slash, to the URL:

```python

# the same setup as above...

endpoint = urljoin(api_base, f"websites/{domain_name}/")
response = requests.get(endpoint, headers=headers)
pprint(response.json())
```

You'll get something like this:

```python
{'domain_name': 'YOURUSERNAME.pythonanywhere.com',
 'enabled': True,
 'id': 42,
 'user': 'YOURUSERNAME,
 'webapp': {'command': '/home/YOURUSERNAME/.virtualenvs/fast_venv/bin/uvicorn '
                       'my_fastapi.main:app --uds $DOMAIN_SOCKET',
            'domains': [{'domain_name': 'YOURUSERNAME.pythonanywhere.com',
                         'enabled': True}],
            'id': 42}}
```


### Using a custom domain for your web app

If you are using a custom domain, there will be an extra field called `cname`
in the output above. This is the CNAME that you can use in your DNS settings
for your web app. For more details on setting up DNS for a custom domain, see
[https://help.pythonanywhere.com/pages/DNSPrimer/](https://help.pythonanywhere.com/pages/DNSPrimer/), 
[https://help.pythonanywhere.com/pages/CustomDomains/](https://help.pythonanywhere.com/pages/CustomDomains/), 
[https://help.pythonanywhere.com/pages/NakedDomains/ ](https://help.pythonanywhere.com/pages/NakedDomains/) and 
[https://help.pythonanywhere.com/pages/TroubleshootingDNS/](https://help.pythonanywhere.com/pages/TroubleshootingDNS/)


### Enabling HTTPS for custom domains

```python

# the same setup as above...

endpoint = urljoin(api_base, f"domains/{domain_name}/ssl/")
response = requests.post(endpoint, headers=headers, json={'cert_type': 'letsencrypt-auto-renew'})
pprint(response.json())
```

You'll get something like this:

```python
{'status': 'OK'}
```

to let you know that it has been applied.


### Reload

If you have changed the code of your website, you need to reload it using
the API to pick up the new code:

```python

# the same setup as above...

endpoint = urljoin(api_base, f"websites/{domain_name}/reload")
response = requests.post(endpoint, headers=headers)
print(response)
```


### Disabling and enabling

If you want to temporarily disable your site without deleting it, or if you've
previously disabled it and you wnat to enable it, here's what you do:

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

However, `enabled` is the only property of the website that you can patch -- if
you'd like to update the serving `command`, you'll need to delete the current
site, and re-deploy it with a new one.


### Delete

To delete your website, use the following code -- mind the `/` at the end of the endpoint!

```python

# the same setup as above...

response = requests.delete(
    urljoin(api_base, f"websites/{domain_name}/"),
    headers=headers
)
print(response)
```

You should get a `204` status code on successful delete.
