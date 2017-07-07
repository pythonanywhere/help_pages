
<!--
.. title: Hosting a static site
.. slug: hosting-a-static-site
.. date: 2016-05-09 11:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


Hosting a static site (ie, a site that doesn't need to run python code to
process requests, so only HTML and JavaScript) is possible on PythonAnywhere,
using a little hack.

First, set up a web app using any framework and Python version (it doesn't matter
which, since we won't need them.  Maybe just choose Manual Configuration and Python3.5).

Then, on the Web tab configuration screen, scroll down to the **Static Files**
section, and add one new entry:

* URL: /
* Path: /home/yourusername/path/to/your/static/site

Hit **Reload** on the web tab.

Then, any files in */home/yourusername/path/to/your/static/site* will be served
automatically.  Start with */home/yourusername/path/to/your/static/site/index.html*
for example!

