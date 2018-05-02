(<!--
.. title: Let's Encrypt
.. slug: LetsEncrypt
.. date: 2016-03-24
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Let's Encrypt provide free SSL certificates for HTTPS. It's possible
to get a Let's Encrypt certificate working on PythonAnywhere.
Here's how:

* **Tip**: _free sites at yourusername.pythonanywhere.com already have HTTPS, you don't need letsencrypt for them._

We use a package called "dehydrated" to get our Let's Encrypt certificate
(we don't use the standard one because it needs all kinds root privileges).
To get it, run the following in a Bash console in your home directory:

    :::bash
    git clone https://github.com/lukas2511/dehydrated.git ~/dehydrated

Now we need some directories to store our keys, certificates and associated files:

    :::bash
    mkdir -p ~/letsencrypt/wellknown
    cd ~/letsencrypt

You'll also need your PythonAnywhere site to be able to serve static
files from your `wellknown` directory. Head over to web app tab and set up a new
mapping (replacing "YOURUSERNAME" with your actual username):

* Static URL: `/.well-known/acme-challenge`
* Static Path: `/home/YOURUSERNAME/letsencrypt/wellknown`

The static files table needs to include at least an entry like the one below (with a different username in the second
column):

<img alt="Let's Encrypt static files setup" src="/letsencrypt-staticfiles.png" style="border: 2px solid lightblue; max-width: 70%;">

Please note that this step is mandatory even if you currently do not serve up static files in this way.

If you're using our password-protection feature for your web app, you'll also need to switch that off for the duration of this procedure;
you can turn it on again once you've got the certificate.

Next, reload your web app using the button at the top of the page.

Now we'll need to create a simple config file. Go back to the Bash console, and
create it like this (replacing "YOURUSERNAME" with your actual username):

    :::bash
    echo WELLKNOWN=/home/YOURUSERNAME/letsencrypt/wellknown > ~/letsencrypt/config

Next, if this is the first time you've ever created a Let's Encrypt certificate
from PythonAnywhere, you need to register with them by running this command:

    :::bash
    ~/dehydrated/dehydrated --register --accept-terms

Now we need to actually request a certificate (replace "WWW.YOURDOMAIN.COM" with
the actual hostname of your website as it's specified on the "Web" page):

    :::bash
    ~/dehydrated/dehydrated --config ~/letsencrypt/config --cron --domain WWW.YOURDOMAIN.COM --out ~/letsencrypt --challenge http-01

If you get a warning saying something like this:

    To use dehydrated with this certificate authority you have to agree to their
    terms of service which you can find here: https://letsencrypt.org/documents/LE-SA-v1.1.1-August-1-2016.pdf
    To accept these terms of service run `/home/username/dehydrated/dehydrated --register --accept-terms`.

...then it's probably because you haven't registered -- you need to run
the version of the command above (with the "--register" and "--accept-terms"
flags), and *then run the dehydrated command to request the certificate again*.

If this is successful, you will see something like this:

    :::text
    # INFO: Using main config file /home/YOURUSERNAME/letsencrypt/config
    # Processing www.yourdomain.com
    #  + Checking domain name(s) of existing cert... unchanged.
    #  + Checking expire date of existing cert...
    #  + Valid till Nov  3 13:48:00 2016 GMT (Less than 30 days). Renewing!
    #  + Signing domains...
    #  + Generating private key...
    #  + Generating signing request...
    #  + Requesting challenge for www.yourdomain.com...
    #  + Responding to challenge for www.yourdomain.com...
    #  + Challenge is valid!
    #  + Requesting certificate...
    #  + Checking certificate...
    #  + Done!
    #  + Creating fullchain.pem...
    #  + Done!

You'll now have a directory named `www.yourdomain.com` in
your `letsencrypt` directory and your certificate and key will be in there.

* **Keep your `/home/YOURUSERNAME/letsencrypt` directory safe**. It contains
  the information necessary for you to renew your certs.

To get your certificate installed email support@pythonanywhere.com to let us
know that you want us to install your certificate. Include your username, the
directory path to the certificates, and the domain name and we'll do the rest.


## Certificate renewal

To renew your certificate, assuming you've left the static file mapping in
place and still have your `letsencrypt` and `letsencrypt.sh` directories, you
just need to re-run:

    :::bash
    cd ~/letsencrypt
    ~/dehydrated/dehydrated --cron --domain www.yourdomain.com --out . --challenge http-01

and then let us know that you have a new certificate and where we can find it.


## Checking expiration date

Forgot when your certificate will expire?

Assuming your files are in the default directories, you can run this command:

    openssl x509 -enddate -noout -in ~/letsencrypt/www.yourdomain.com/cert.pem

and if you have multiple domains, you can create a bash script like this:

    echo www.domain1.com expires $(openssl x509 -enddate -noout -in ~/letsencrypt/www.domain1.com/cert.pem)
    echo www.domain2.com expires $(openssl x509 -enddate -noout -in ~/letsencrypt/www.domain2.com/cert.pem)
    echo www.domain3.com expires $(openssl x509 -enddate -noout -in ~/letsencrypt/www.domain3.com/cert.pem)

which you can run with `bash check_expirations.sh`
