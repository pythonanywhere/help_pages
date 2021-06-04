<!--
.. title: Integrating a development environment with PythonAnywhere
.. slug: IntegratingWithPythonAnywhere
.. date: 2019-06-21
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

*This help page is a work-in-progress; as it stands it has been written for
one particular person who wants to add a "create a live website" feature to
a development environment.  We expect to be expanding it over time.*

In order to automatically create a website on PythonAnywhere, you need to use
our [API](/pages/API).  This page explains the process, and the API calls
you need to make.

## Creating a user account

Even if you have an account on PythonAnywhere, for testing purposes you should
create another one.  We've given instructions below that are way more detailed
than we would expect anyone using this help page would ever possibly need --
but you're welcome to use the screenshots and/or wording for your own
documentation :-)

### Simple PythonAnywhere signup instructions

The first step is, of course, to go to PythonAnywhere.  We have two sites,
one based in the EU and one in the US.  If you're in the EU, then go to:

 * [https://eu.pythonanywhere.com/](https://eu.pythonanywhere.com/)

If you're anywhere else in the world, go to:

 * [https://www.pythonanywhere.com/](https://www.pythonanywhere.com/)

You'll wind up here:

<img alt="PythonAnywhere front page" src="/integrating-pa-front-page.png" class="bordered-image">

Click either the "Pricing and signup" link to the top right, or the "Start running
Python online in less than a minute" button (they both go to the same place):

<img alt="PythonAnywhere plans page" src="/integrating-pa-plans-page.png" class="bordered-image">

Now click the "Create a Beginner account" button to create a free account:

<img alt="PythonAnywhere signup page" src="/integrating-pa-signup-page.png" class="bordered-image">

Make a note of the username you choose, you'll need it later.  You'll be taken
to the dashboard; take the tour if you like!  Also, don't forget to confirm
your email address by clicking the link in the message we send you, because
if you don't, you won't be able to reset your password if you forget it.

The next step is to generate an API token, which is what allows programs outside
PythonAnywhere to connect to the site and make changes on your behalf.  Click
the "Account" link near the top right and you'll be taken here:

<img alt="PythonAnywhere account page" src="/integrating-pa-account-page.png" class="bordered-image">

Select the "API token" tab near the center of the page:

<img alt="PythonAnywhere API tab with no token" src="/integrating-pa-api-no-token-page.png" class="bordered-image">

Click the "Create a new API token" button:

<img alt="PythonAnywhere API tab with no token" src="/integrating-pa-api-with-token-page.png" class="bordered-image">

That string of letters and numbers (`d870f0cac74964b27db563aeda9e418565a0d60d` in
the screenshot) is an API token, and anyone who has it can access your PythonAnywhere
account and do stuff -- so keep it secret.  If someone does somehow get hold of it,
you can revoke it on this page by clicking the red button -- that stops it from
working in the future, and creates a new one for you to use.

### End of sample signup instructions

...we now return to a slightly more expert-oriented guide for doing the actual
integration :-)

## Using the PythonAnywhere API

The full documentation for the PythonAnywhere API is [here](/pages/API).  What
we need to do to get a website running is:

 * Check if the user already has a website
 * If not, create it
 * Upload the files that make up the website's code
 * Upload a WSGI file, which connects the website's code to the web server
 * Upload any static file routes (eg. "URLs starting `/static/` should be served from such-and-such a directory)
 * Reload the website so that the changes are all live.

The easiest way to show the details of that is through an example, so we've
created one: [https://github.com/pythonanywhere/upload-website](https://github.com/pythonanywhere/upload-website).

In that repository, we have:

 * A super-simple example of a Flask site, with code, a template, and a static CSS file, in the `src` directory.
 * An upload script, `upload.py`.
 * A requirements file.

The upload script is the most interesting part of it.  When you run it, it will
prompt you for a username, an API token, and the PythonAnywhere region you
created the account in (`eu` or `www`).

Try it out with the user you just created; it will print out the details of the
steps it's taking to set things up, and present you with a URL at the end.

The code itself should be reasonably easy to understand, but if it's not,
please do let us know and we can expand this help page.







