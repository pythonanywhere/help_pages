<!--
.. title: Gmail App-Specific Passwords
.. slug: GmailAppSpecificPasswords
.. date: 2021-03-17 18:35:28 UTC
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Google sometimes blocks SMTP requests from IP addresses it doesn't recognise.
When that happens, you will normally get an error that looks like this:

    SMTPAuthenticationError: Please log in via your web browser and then try again.

If you're finding emails aren't getting sent, and you get that error, try visiting the security page on
your Google account, and have a look for security notifications. Things may start
working if you approve some requests listed there, but the best long-term fix is to
generate an application-specific password.

Here's the [Google Help page on how to do that](https://support.google.com/accounts/answer/185833?hl=en).

We've also had reports that app-specific passwords can also get blocked; you'll
start getting errors back when your code tries to authenticate saying something
like "Please log in via your web browser and then try again."

The solution to this seems to be:

  1. Confirm that recent logins really were from you on the [Google account security page](https://myaccount.google.com/security)
  2. Unlock the account by [entering a captcha](http://www.google.com/accounts/DisplayUnlockCaptcha).

Doing this should unlock the account, though it can take up to an hour to take effect.
