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

[CloudFlare](https://www.cloudflare.com) is a security and acceleration service
that sits between your application and the big, bad internet. Here's how to get
all that goodness for your PythonAnywhere web app.

Since CloudFlare works by taking over the DNS configuration for a site, this
will only work for custom domains. I have used `minimumviableserver.com`
as an example.

The setup of a website on CloudFlare is pretty straightforward. If you give CloudFlare your domain, it automatically
interrogates the DNS system for the domain's current settings and provides
excellent instructions about what needs to be changed. You will see something like this afterwards (unless you they changed their interface :)

<img alt="screenshot of cloudflare dns settings page" src="/cloudflare-dns-settings.png" width="80%">

Now, you just need to set up a simple CNAME record for your PythonAnywhere web app. Assuming you've already created a web app on PythonAnywhere like this:

![Screenshot of web app creation](/cloudflare-new-webapp.png)


From the web app config tab you'll have a CNAME target for your PythonAnywhere web
app -- something like `webapp-120107.pythonanywhere.com`.

On the CloudFlare DNS config screen, create a CNAME for the `www` subdomain to point at this web app.  That's all you need to do to get your `www.yourdomain.com` site working!


Either way, now when we go to `www.minimumviableserver.com`, we see our web app, but how do we know it's going through CloudFlare? looking at the network logs in our
browser's developer tools, we can see that there are plenty of indicators in
the response headers.

Here are the response headers for a dynamically generated html page:
![Screenshot of dynamic response headers](/cloudflare-response-headers.png)

and these are the response headers for a static resource on that page:
![Screenshot of static response headers](/cloudflare-response-headers-static.png)


If you're a completist and you want to get the naked domain working (that is, `yourdomain.com` instead of `www.yourdomain.com`), you need something a bit more complicated called a "page rule".  Check the [cloudflare documentation](https://support.cloudflare.com/hc/en-us/articles/200172286-How-do-I-perform-URL-forwarding-or-redirects-with-CloudFlare), essentially you'll want to point yourdomain.com/* to www.yourdomain.com/$1.
