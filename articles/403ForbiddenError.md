
<!--
.. title: 403 Forbidden error
.. slug: 403ForbiddenError
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



## Why do I get a "403 Forbidden" or "[Errno 111] Connection refused" error when accessing a website from PythonAnywhere?


Free accounts' internet access goes via a proxy "allowlist". [Here is the list
of sites currently allowed](https://www.pythonanywhere.com/whitelist/).

We operate this to prevent malicious users from using our site to hack into and
spam other websites. **Paid-for accounts don't have this limitation**, because
we can connect them to real people. Spammers and criminals prefer to be
anonymous, so we figure they're unlikely to sign up for paid accounts here.


### [Errno 111] Connection refused


This error suggests that either the library you're using doesn't support using
a proxy, or that it needs to be configured to use a proxy. Have a look at the
docs for the library to determine which it is and consider raising an issue
with the project about proxy support.


## Proxy Details

In order to make a connection to a site that is on the allowlist, you will need to connect
through our proxy server. This is an HTTP proxy at `proxy.server:3128`. Most
Python libraries recognise and use the setting that we supply (for
instance, with `requests`, you don't need to do anything special), others need
to be specifically configured to use the proxy (check the documentation of the
library to find out how) and some don't work through the proxy at all (for
instance, any library that uses httplib2 on Python 3 e.g. `twilio`)


## Upgrading your account

Paying users have unrestricted access.  You can [upgrade your account here if you're on our US site](https://www.pythonanywhere.com/pricing/),
or [from here if you're on our EU site](https://eu.pythonanywhere.com/pricing/).

After you upgrade you'll need to kill any old consoles and start new ones to get your
new Internet settings.  You'll also need to restart any webapps and scheduled tasks.


## Requesting an addition to the allowlist

See [this page](/pages/RequestingAllowlistAdditions/)

