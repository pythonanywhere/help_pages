
<!--
.. title: Starting encrypted connection
.. slug: StartingEncryptedConnection
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->





##The "Starting encrypted connection" message never disappears


For example, a message like this:

    Starting encrypted connection to consoles-1.pythonanywhere.com on port 443


We sometimes have problems with firewalls blocking our connections, so if you're behind a corporate firewall or proxy, that could be the cause.

Another possiblity is that there is some kind of certificate error. To test this, try manually visiting [https://consoles-1.pythonanywhere.com](https://consoles-1.pythonanywhere.com/) in your browser. It should give you a 404 message, but **if it gives you a certificate warning or a security error**, do let us know.

Failing that, here are a few more things to try:

  * try a different web browser on the same PC
  * try a different PC at the same location
  * try accessing PythonAnywhere from a different location
