
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




For some web sites you might want to not just offer HTTPS access to your users
-- you might want to force all connections to go through HTTPS, so that when
someone visits `http://www.yoursite.com/` they're automatically redirected to
`https://www.yoursite.com/`.   This is something you can set up on the
"Web" page:

<img alt="Force HTTPS button" src="/force-https.png" style="border: 2px solid lightblue; max-width: 70%;">

Click on the slider to activate it, and then reload your website using the
button at the top -- you're all set.


## FAQ:  can I force HTTPS on the naked domain?

You can't force-https if you're using a domain redirection service, but you can
if you've manually set up a naked domain config.  More info here: [Naked Domains](/pages/NakedDomains)


## Alternative solution: CloudFlare

Edge caching providers like CloudFlare have their own solutions for HTTPS redirecting,
which are worth looking into:

* [couldflare support article on https redirects](https://support.cloudflare.com/hc/en-us/articles/200170536-How-do-I-redirect-all-visitors-to-HTTPS-SSL-)

* [a blog post re: cloudflare and pythonanywhere](https://blog.pythonanywhere.com/80/)
