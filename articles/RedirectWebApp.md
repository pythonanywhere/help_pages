<!--
.. title: How do I create a web app that redirects from one domain to another?
.. slug: RedirectWebApp
.. date: 2018-02-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


Sometimes you need to write a website that simply redirects from one domain to
another.  For example, you might have created a website at `yourusername.pythonanywhere.com`,
and it's become popular enough that you decided to upgrade to a paid plan and
host it on `www.yourdomain.com` -- but there are lots of links out there
that go to the old domain, and you want them to continue working.

The best solution is to have a simple website running at `yourusername.pythonanywhere.com`
which, when it receives a request, redirects the user to the new domain -- so
requests to `http://yourusername.pythonanywhere.com/something` are redirected
automatically to `http://www.yourdomain.com/something`, and so on.

To do this, you need to have a website on the "Web" tab for both domains; the
one on `www.yourdomain.com` is your main site, and the one on `yourusername.pythonanywhere.com`
is a simple Flask app using Python 3.6, with the following code in the
`flask_app.py` file:

    from flask import Flask, redirect, request

    app = Flask(__name__)

    from urllib.parse import urlparse, urlunparse

    FROM_DOMAIN = "yourusername.pythonanywhere.com"
    TO_DOMAIN = "www.yourdomain.com"

    @app.before_request
    def redirect_to_new_domain():
        urlparts = urlparse(request.url)
        if urlparts.netloc == FROM_DOMAIN:
            urlparts_list = list(urlparts)
            urlparts_list[1] = TO_DOMAIN
            return redirect(urlunparse(urlparts_list), code=301)
