<!--
.. title: TLS version support
.. slug: TLSVersionSupport
.. date: 2021-10-11 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

## TL;DR for those who know the background

By default we support TLS 1.2 and 1.3 for websites; older protocol versions can
be supported for custom domains -- if you have old devices connecting to your
site and you need to use them, then [contact us](support@pythonanywhere.com) --
but do note that this will mean reduced security for your site.


## In more detail...

### What is TLS?

[TLS](https://en.wikipedia.org/wiki/Transport_Layer_Security) (Transport Layer
Security) is the name of the protocol used to make secure
connections across the Internet.  The earlier protocol that it is based on was
called SSL (Secure Sockets Layer) and that name is also still used by some
people when talking about TLS.

The use of TLS is what makes an HTTPS website secure -- when a site is visited
over HTTP, all of the data is sent in the clear, so someone who was able to tap
into the communications could see what is being sent and received.  By contrast,
HTTPS sends the data over a TLS connection, which means that anyone who
intercepted it would just see encrypted data.


### TLS versions

There are a number of versions of the TLS protocol, and of the SSL protocol that
preceded it.  Older versions have become deprecated as security problems with
them have been identified.  As of this writing:

* SSL 1.0 -- never released because it had security problems
* SSL 2.0 -- released in 1995, deprecated in 2011
* SSL 3.0 -- released in 1996, deprecated in 2015
* TLS 1.0 -- released in 1999, deprecated in 2020
* TLS 1.1 -- released in 2006, deprecated in 2020
* TLS 1.2 -- released in 2008, still regarded as OK
* TLS 1.3 -- released in 2018, still regarded as OK


### Which versions does PythonAnywhere support?

By default on PythonAnywhere, websites that we host are only available over TLS
1.2 and 1.3.  The reason we do not support older TLS versions is that an
attacker can (in theory) alter a connection so that it switches over to using an
older, broken version.  This is known as a
[protocol downgrade attack](https://en.wikipedia.org/wiki/Downgrade_attack).

More concretely:

* A browser connects to your website using TLS 1.2.
* The attacker, who is somehow able to monitor the connection, injects some extra data into it.
* The browser interprets this extra data as the server saying "I'd rather use TLS 1.1".
* The browser and the server continue to communicate using TLS 1.1.
* The attacker records the data and, due to a security problem with 1.1, is able to decrypt it.

What that means is that any server that supports TLS 1.1 or earlier is not really
secure.  So our normal web-serving infrastructure only supports 1.2 or higher.


### Older devices

Lack of support for TLS 1.1 can cause problems with older devices.  Some old Android devices (older
than 5.0 "Lollipop") don't support TLS 1.2, and by default Windows 7 doesn't
have it switched on (though support for it is built in).  Some old Internet-of-Things devices
don't support it either.

That probably won't matter for most websites -- it's better to have a properly
secure site that doesn't accept HTTPS connections from really old operating
systems and browsers than it is to have a site that isn't secure.

But for some people, support for TLS 1.0 and 1.1 might be necessary -- for
example, if your site is frequently used by people who are using Android devices
that haven't had an OS update since Lollipop was released in 2014, or by people
using old Windows 7 machines.


### Enabling support for legacy TLS

For custom domains, we can set things up so that your site is handled by special
"legacy TLS" servers which offer those lower-security protocols.  Unfortunately
we can't do that for websites that are running as subdomains of `pythonanywhere.com`
or `eu.pythonanywhere.com`

It's a two-step process to get that set up:

* Firstly, contact us at [support@pythonanywhere.com](support@pythonanywhere.com) so that we can set things up on the backend servers.
* Next, update your CNAME -- normally you would point your domain at our servers with a CNAME value of the form `webapp-XXXX.pythonanywhere.com` or `webapp-XXXX.eu.pythonanywhere.com`.  For legacy TLS sites, you would instead need to point it at `legacy-tls.pythonanywhere.com` or `legacy-tls.eu.pythonanywhere.com`

Please note, however, that doing this will make your site potentially vulnerable
to protocol downgrade attacks, even for the people who are accessing it using
the latest and greatest browsers and operating systems.  They might connect using
1.3, but be downgraded to 1.1.  The only way to be fully secure is to not allow
old versions of TLS at all.





