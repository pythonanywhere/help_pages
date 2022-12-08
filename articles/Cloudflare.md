<!--
.. title: Using Cloudflare with PythonAnywhere
.. slug: Cloudflare
.. date: 2022-12-08
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

> Warning -- this will only work in paid accounts

[Cloudflare](https://www.cloudflare.com) is a security and acceleration service
that sits between your application and the big, bad internet. It provides DDoS
protection, acceleration of your site through caching, and a bunch more good stuff.
Here's how to get all that goodness for your PythonAnywhere website.

One note first; Cloudflare can currently only be used with custom domains, and
won't work with PythonAnywhere subdomains (like `yourusername.pythonanywhere.com`).  That's
because it works by taking over the DNS configuration for a site.  We have used
`www.minimumviableserver.com` as an example for this blog post.


## Initial setup

The setup of a website on CloudFlare is pretty straightforward. If you give
Cloudflare your domain, it automatically interrogates the DNS system for the
domain's current settings and provides excellent instructions about what needs
to be changed. You will see something like this afterwards:

<img alt="screenshot of cloudflare dns settings page" src="/cloudflare-dns-settings.png" width="80%">

Now, you just need to set up a simple CNAME record for your PythonAnywhere web
app. Assuming you've already created a web app on PythonAnywhere like this:

![Screenshot of web app creation](/cloudflare-new-webapp.png)

...then on the web app config tab you'll have a CNAME target for your site --
something like `webapp-120107.pythonanywhere.com`.

On the CloudFlare DNS config screen, create a CNAME for the `www` subdomain to
point at this web app.  That's all you need to do to get your
`www.yourdomain.com` site working!

> Note: you will see a warning saying that "You do not have a CNAME set up for
> your domain" even after you've created that CNAME.  One of the security
> features CLoudflare provide is that they hide where your site is actually
> hosted, which means that when the PythonAnywhere servers query the DNS system
> to check if you have a CNAME, they get responses saying that you don't.  You
> can ignore this message.


## Origin certificates

In order to completely secure the connection between Cloudflare and your site
running on PythonAnywhere, they will provide you with what they call an "origin"
certificate, and its associated private key.  You can upload that in the "HTTPS
certificate" part of the "Security" section of the "Web" page on PythonAnywhere.
It is a *Custom* certificate; the "Auto-renewed Let's Encrypt certificate" system
won't work with Cloudflare.

> Note: you will get a warning saying something like "Mismatch between
> certificate Common Name (CloudFlare Origin Certificate) and webapp
> (www.yourdomain.com).  This is a similar issue to the CNAME warning above, and
> is also something you can ignore.


## Checking that your site is protected

Now when you go to `www.minimumviableserver.com`, you'll see your site, but how
do you know it's going through CloudFlare? looking at the network logs in our
browser's developer tools, we can see that there are plenty of indicators in
the response headers.

Here are the response headers for a dynamically generated html page:

![Screenshot of dynamic response headers](/cloudflare-response-headers.png)

and these are the response headers for a static resource on that page:

![Screenshot of static response headers](/cloudflare-response-headers-static.png)


## "Naked" (aka "Apex" domains)

If you're a completist and you want to get the naked domain working (that is,
`yourdomain.com` instead of `www.yourdomain.com`), you need something a bit more
complicated called a "page rule".  Check the [cloudflare documentation](https://support.cloudflare.com/hc/en-us/articles/200172286-How-do-I-perform-URL-forwarding-or-redirects-with-CloudFlare);
essentially you'll want to point yourdomain.com/* to www.yourdomain.com/$1.


## Common issues

* If you use PythonAnywhere's "Force HTTPs" option then you may get
  a "too many redirects" error when you visit your site.  This is due to both
  Cloudflare and PythonAnywhere trying to force the browser to use HTTPS; only one should be
  configured to do that, and given that you're using Cloudflare for security, it
  should be Cloudflare.  You should just switch off "Force HTTPs" on the
  PythonAnywhere side.
* You will get the same problem with if you use your web framework's system for
  forcing HTTPS, like  Django's `SECURE_SSL_REDIRECT` setting.  The solution is
  the same, just switch off the framework option.
