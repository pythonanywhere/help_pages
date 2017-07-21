
<!--
.. title: Error Reloading web app
.. slug: ErrorReloadingWebApp
.. date: 2017-07-21 10:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

## What to do when you see "error reloading web app".



### Could it be a short-term glitch?

The first thing to is wait a few minutes and try again.  Sometimes there's just
a short-term glitch on the server, and next time you try it, everything should be
fine.

This should only happen rarely however.  If you see errors frequently when reloading
your web app, read on, there probably is a real issue.


### Did the reload time-out?  Could something be causing your site to respond slowly?

When we reload your web app, we "ping" it with a single hit at the end of the reload
process, to ensure the web app has fully loaded and is responding to requests (otherwise
the first hit on the site feels very slow, as python has to load up your web framework,
all your dependencies, etc.  Subsequent hits should be faster).

We set a **20-second timeout** on that first hit.  So, if for some reason your web app
is slow to respond -- either slow in general, or just slow to respond to that first hit --
then you'll see these timeout errors.

So, it may be worth looking into reasons your app might be slow, and if you find some,
try to optimize your code, or do less processing in your web requests, and do more of it
asynchronously somehow.  See [this page on async web work](/pages/AsyncInWebApps).


### Did your site actually reload correctly?

If your app seems to be working fine, then maybe it's nothing to worry about.

If your app is slow to respond to the first hit (as per the above), for example,
but it performs well for all subsequent hits, then you don't really need to do
anything.


### Is your site showing errors? (500)

If your site is showing an "unhandled exception" error page, then that might 
point toward the source of the problem.  Check your **error log** and **server log**,
you'll find links to them from the web tab


### 502 and 504 errors

If your site is showing a 502 or a 504 error, that's more serious.  It means
we haven't been able to load your code at all.

One possiblity could be that you're doing something that's incompatible with our
hosting model, like trying to manually bind to a port (see, eg,
[Flask504Error](/pages/Flask504Error)).  Don't do that!


###  Harakiri  (another kind of timeout)

Have a look in your **server log** for any messages saying "harakiri".  Those
indicate that your web app is not only timing out on the first hit, but it's
actually hitting our server-side 5-minute timeout for requests.  Take a look
through your code for anything that could be taking a very long time to complete.

And, again, see [this page on async web work](/pages/AsyncInWebApps) for alternative
places to run your code.

