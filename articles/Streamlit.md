<!--
.. title: Deploying Streamlit apps on PythonAnywhere (beta)
.. slug: Streamlit
.. date: 2024-06-10 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

This help page explains how to set up a Streamlit app on PythonAnywhere.

## Disclaimer

Deployment of Streamlit apps on PythonAnywhere is an
experimental feature.  Some important limitations to know about:

 * There is no support for static file mappings.
 * The primary way to manage Streamlit sites is via a set of command-line tools or with
   our API.  (There is a very limited web UI for creating and managing them --
   contact [support@pythonanywhere.com](mailto:support@pythonanywhere.com) if you would like us to enable it for your account --
   however, the command-line system is the most complete way to do it.)
 * We do not guarantee that the command line syntax and the API interface will remain the same.
 * We have not worked out the long-term pricing for those sites, which will
   probably differ from the way we charge for traditional WSGI ones.

If you are brave enough to try it, here is a quick guide on how to do it :-)

# Prerequisites

## Paid account
As Streamlit is not installed by default, you will need to install it in a
virtualenv. The size of a virtualenv with Streamlit and its dependencies is
too large for a free account, so you will need at least a basic Hacker paid account to
use it.

## API token

This help page explains how to manage your websites using our `pa` command-line
tool rather than the API, but you'll need to generate an API token so that
that tool knows how to connect to PythonAnywhere.

First, you will need an API token. [This page](/pages/GettingYourAPIToken) will
show you how to get that.

Now you can use our command-line tool or our experimental API to deploy your
Streamlit app.  This help page will show you how to use the command-line
tool, so you don't need to note down the API token -- now that it has been
generated, it's available to any code running inside Bash consoles on
PythonAnywhere.

## Installing the command-line tools

As a first step, start a fresh Bash console, and in there, install the latest
version of our command-line tool.

```bash
pip install --upgrade pythonanywhere
```
Running that install will make a new command, `pa` available, which we'll be
using later.


# A simple Streamlit app

Firstly, create a [virtualenv](/pages/VirtualenvsExplained) with `streamlit`
installed.  In your Bash console:

```bash
mkvirtualenv my_venv --python=python3.13
```

...and then:

```bash
pip install streamlit
```

Next, we'll create a minimal Streamlit app.  Create a directory
`~/my_streamlit/`
and inside it get the example Streamlit app, the same that is used in
[official Streamlit tutorial](https://docs.streamlit.io/get-started/tutorials/create-an-app):

```bash
mkdir ~/my_streamlit/
cd ~/my_streamlit/
wget https://raw.githubusercontent.com/streamlit/demo-uber-nyc-pickups/master/streamlit_app.py
```

That's enough setup!  Now you can move on to [creating your website](#creating-your-website)

# Managing your website

## Creating your website

In Bash, to deploy your website to your subdomain -- that is, to
*yourusername*`.pythonanywhere.com` if you're on our US system, or
*yourusername*`.eu.pythonanywhere.com` if you're on the EU system -- just run
the following (rather long) command.


```bash
pa website create --domain YOURUSERNAME.pythonanywhere.com --command '/home/YOURUSERNAME/.virtualenvs/my_venv/bin/streamlit run /home/YOURUSERNAME/my_streamlit/streamlit_app.py --server.address "unix://${DOMAIN_SOCKET}" --server.enableCORS false --server.enableXsrfProtection false --server.enableWebsocketCompression false'
```

...with the three instances of `YOURUSERNAME` replaced by your actual username, but with everything else
exactly as it is.

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

You have a working Streamlit app hosted on PythonAnywhere!  However, this site
will not currently appear on the "Web" page inside your PythonAnywhere account;
we have a user interface that is a work-in-progress, though, and if you'd like
to try that out, [drop us a line](mailto:support@pythonanywhere.com).


## Getting and listing websites

You can get a list of new style websites from PythonAnywhere with this command:

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
command      /home/YOURUSERNAME/.virtualenvs/my_venv/bin/streamlit run /home/YOURUSERNAME/my_streamlit/streamlit_app.py --server.address "unix://${DOMAIN_SOCKET}" --server.enableCORS false --server.enableXsrfProtection false --server.enableWebsocketCompression false
access log   /var/log/YOURUSERNAME.pythonanywhere.com.access.log
error log    /var/log/YOURUSERNAME.pythonanywhere.com.error.log
server log   /var/log/YOURUSERNAME.pythonanywhere.com.server.log
-----------  -------------------------------------------------------------------------------------------------------------------------
```


## Using a custom domain for your Streamlit app

If you are using a custom domain, there will be an extra field called `cname`
in the output above. This is the CNAME that you can use in your DNS settings
for your web app. For more details on setting up DNS for a custom domain, see:

- [How DNS works: a beginner's guide](https://help.pythonanywhere.com/pages/DNSPrimer/)
- [Setting up a custom domain on PythonAnywhere](https://help.pythonanywhere.com/pages/CustomDomains/)
- [Naked domains](https://help.pythonanywhere.com/pages/NakedDomains/)
- [Troubleshooting DNS](https://help.pythonanywhere.com/pages/TroubleshootingDNS/)


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
