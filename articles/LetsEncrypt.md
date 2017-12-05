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

You'll also need your pythonanywhere site to be able to serve static
files from your `wellknown` directory. Head over to web app tab and set up a new
mapping:

* Static URL: `/.well-known/acme-challenge`
* Static Path: `/home/YOURUSERNAME/letsencrypt/wellknown`

(don't forget to replace "YOURUSERNAME" with your actual username, here and in
the instructions below) and then **reload your web app**

We'll need to create a simple config file. Put the following (with suitable
replacements) into a file at `/home/YOURUSERNAME/letsencrypt/config`

    :::bash
    WELLKNOWN=/home/YOURUSERNAME/letsencrypt/wellknown

Now we need to actually request a certificate:

    :::bash
    ~/dehydrated/dehydrated --config ~/letsencrypt/config --cron --domain www.yourdomain.com --out ~/letsencrypt --challenge http-01
    # susbtitute www.yourdomain.com with your own domain name, including the www. part

* **Tip**: _If you're using our password-protection feature for your web app, you'll need to switch that off for the duration of this procedure_

If you get a warning saying something like this:

    To use dehydrated with this certificate authority you have to agree to their
    terms of service which you can find here: https://letsencrypt.org/documents/LE-SA-v1.1.1-August-1-2016.pdf
    To accept these terms of service run `/home/username/dehydrated/dehydrated --register --accept-terms`.

...then you need to run the command they specify, and *then run the original dehydrated command again*.

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
