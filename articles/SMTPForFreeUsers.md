<!--
.. title: SMTP for free users
.. slug: SMTPForFreeUsers
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Free users are restricted to HTTP/HTTPS only, to a
[whitelist of sites](https://www.pythonanywhere.com/whitelist/). Because
most email services work over SMTP, which is not HTTP or HTTPS, that means you
cannot normally use SMTP on Free accounts.  Here are some solutions to work around
that.


## Use an HTTP/HTTPS-based email service

Services like [Mailgun](http://mailgun.com/) or
[sendgrid](https://sendgrid.com/) allow you to send email using HTTP(S)
requests, and their API endpoint are on our whitelist.  This is the most
reliable option, and works well so long as your code isn't limited to using
SMTP.

Here's how you do it:
* [on Mailgun](https://documentation.mailgun.com/en/latest/quickstart-sending.html#how-to-start-sending-email)
* [on Sendgrid](https://docs.sendgrid.com/api-reference/mail-send/mail-send)


## Use Gmail's SMTP servers

We have added a special exception to our firewall rules for Gmail's SMTP
servers. If you use them, it should work.

However, we have to hard-code the IP addresses of Google's servers into our
firewall, and these sometimes change, which means that, on occasion, Google may
switch to a new Gmail server which we don't know about, and that would
temporarily block email until we are able to update the firewall.

One other thing that's quite important: we highly recommend you use an
[app-specific password](/pages/GmailAppSpecificPasswords)
instead of your normal Google login password for this.  This has two advantages:

 * Google's security systems sometimes block your first attempt to use their SMTP servers from a new IP address, which can be a pain if you're running code on different servers (which happens a lot on PythonAnywhere as we change our systems).  They don't seem to do this for app-specific passwords.
 * It's much better not having a copy of your main Google password on a third-party service like PythonAnywhere, because you can always revoke the password from the Google site if necessary, without having to log in here.

For Django, you can use the settings:

    :::python
    EMAIL_HOST = "smtp.gmail.com"
    EMAIL_HOST_USER = "yourusername@gmail.com"
    EMAIL_HOST_PASSWORD = 'yourpassword'
    EMAIL_PORT = 587
    EMAIL_USE_TLS = True

The settings for other frameworks are similar.
