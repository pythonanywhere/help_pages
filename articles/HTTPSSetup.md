<!--
.. title: How to set up an HTTPS/SSL certificate for a custom domain
.. slug: HTTPSSetup
.. date: 2019-01-15 12:49:28 UTC+00:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

In order for a website to prove that it really is the site it says it is, it needs
an HTTPS certificate.  Once you've set up a website on a custom domain on PythonAnywhere, you'll need
to have one, as otherwise people who visit the site over HTTPS
will get a security error -- specifically, Chrome will say something like "NET::ERR_CERT_COMMON_NAME_INVALID"
and Firefox will just say "Your connection is not secure".

You do not need to do this for a non-custom domain (that is, one at *yourusername*`.pythonanywhere.com`)
because we supply an certificate so that they handle HTTPS by default.

But once you've created a website on a custom domain, we need to get a certificate
for you, and for this we need to prove that PythonAnywhere is the host for
the domain.  This is a security thing -- it stops us from doing nefarious things
like trying to get a certificate for `www.google.com` ;-)

The good news is that this is pretty easy from your side.  Once you've got
[the DNS stuff](/pages/CustomDomains) set up so that your custom domain is pointed
at PythonAnywhere's servers, and it is correctly handling non-secure requests to
its HTTP URLs, we can get a certificate for you using a free
service called [Let's Encrypt](https://letsencrypt.org/).  It's just a couple
of clicks, and we'll automatically renew the certificate so that it won't expire.

You can also upload custom certificates that you've bought from a certificate
provider like GoDaddy or Comodo, but it's a little harder to set up.  We
have [a help page on setting up custom certificates here](/pages/HTTPSCustomCerts).

To set up a free, auto-renewing Let's Encrypt certificate, follow these steps:

  * Go to the "Web" page, and select your website from the list on the left:

    <img alt="The 'Web' page" src="/https-setup-web-app-page.png" class="bordered-image">

  * Scroll down to the "Security" section:

    <img alt="The 'Security' section of the 'Web' page" src="/https-setup-security-section-no-cert.png" class="bordered-image">

    ...and click the pencil icon next to the "None" on the "HTTPS certificate" line
    to edit your certificate.

  * Select the "Auto-renewed Let's Encrypt certificate" option:

    <img alt="Selected auto-renewed Let's Encrypt certificate option" src="/https-setup-security-section-editor-letsencrypt-selected.png" class="bordered-image">

    ...and click the "Save" button.

  * After a brief pause, you should get a message saying that it's all set up:

    <img alt="Let's Encrypt all set up" src="/https-setup-security-section-letsencrypt-installed.png" class="bordered-image">

Once that's done, you're all set!  Just go to the HTTPS URL for your site, like
http*s*://www.yourdomain.com, and you'll see that the site is now marked as secure.

If you want to make your site even more secure, you can set it up so that when
people visit the non-secure URL they are automatically redirected to the secure
version.   This is called "forcing HTTPS", and is described on
[this help page](/pages/ForcingHTTPS).




