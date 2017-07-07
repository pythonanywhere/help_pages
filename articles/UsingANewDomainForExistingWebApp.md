
<!--
.. title: Using a new domain for existing webapp
.. slug: UsingANewDomainForExistingWebApp
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

If you have a free account on PythonAnywhere, you can run a website at the
domain *yourusername*`.pythonanywhere.com`.  But if you have a paid account,
you can run the site on any domain that you own.

If you already have a web application up and running on PythonAnywhere and you
want to point a new domain at it -- for example, if you have a site at
`conrad.pythonanywhere.com` and you want it to show up at `www.conradsdomain.com` --
there are two steps:

 * Go to the "Web" tab, and click on the pencil icon next to the web app name.
   Change it from `conrad.pythonanywhere.com` to `www.conradsdomain.com`.

   ![click on the pencil icon!](/rename_webapp.jpg)

   This tells the PythonAnywhere system that when it receives a request for
   your domain, it should use your web app to respond to the request.

 * After you've done that, you'll see a new "DNS setup" section on the "Web"
   tab.  This will have a "CNAME" value, which you'll need to use in some
   configuration with the company you bought the domain from.  There's
   [more information about CNAME setup here](/pages/OwnDomains#configuring-the-domain-at-the-domain-registrar).
