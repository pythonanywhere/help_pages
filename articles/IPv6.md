
<!--
.. title: IPv6
.. date: 2016-08-16 11:35:28 UTC+01:00
.. slug: IPv6
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Unfortunately, because we're using AWS as a hosting provider, and they don't support IPv6, that's a problem for us for now.


We do have some ideas about how we might be able to get around it, but for now,
you can support IPv6 if you use an edge caching / proxy service in front of
PythonAnywhere. For example, [cloudflare](https://www.cloudflare.com/) can
provide IPv6 support in front of your PythonAnywhere web app (and last we
checked, it was included in their free plan!)

Here's a [blog post about using cloudflare with PythonAnywhere](https://blog.pythonanywhere.com/80/).

