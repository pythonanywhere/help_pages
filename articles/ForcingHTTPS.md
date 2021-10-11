<!--
.. title: Forcing HTTPS
.. slug: ForcingHTTPS
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

**Please note that if you have a custom domain, forcing HTTPS is something that
you should do after you have [set up HTTPS](/pages/HTTPSSetup) -- otherwise you
will be forcing visitors to your site to use a protocol that it does not support,
and they will get security errors.**


### What is forcing HTTPS?

For some web sites you might want to not just offer HTTPS access to your users
-- you might want to force all connections to go through HTTPS, so that when
someone visits `http://www.yoursite.com/` they're automatically redirected to
`https://www.yoursite.com/`.   This is something you can set up on the
"Web" page:

<img alt="Force HTTPS button" src="/force-https.png" class="bordered-image">

Click on the slider to activate it, and then reload your website using the
button at the top -- you're all set.


### FAQ:  can I force HTTPS on the naked domain?

The best way to do that is to use the free secure naked domain redirection service
at [NakedSSL](https://www.nakedssl.com/).


### Alternative solution: CloudFlare

Edge caching providers like CloudFlare have their own solutions for HTTPS redirecting,
which are worth looking into:

* [CloudFlare support article on https redirects](https://support.cloudflare.com/hc/en-us/articles/200170536-How-do-I-redirect-all-visitors-to-HTTPS-SSL-)
* [Our own blog post on setting up CloudFlare and PythonAnywhere](https://blog.pythonanywhere.com/80/)
