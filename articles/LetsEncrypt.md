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

Let's Encrypt provide free SSL certificates for HTTPS. It's easy
to get a Let's Encrypt certificate working on PythonAnywhere.
Here's how:

* **Tip**: _free sites at yourusername.pythonanywhere.com already have HTTPS, you don't need your own certificate for them._

## Make sure you've enabled the PythonAnywhere API

The first step to do that is to make sure you have an API token set up for your
account; go to the "Account" page and then click the "API token" tab. If you see
this:

<img alt="API token set up" src="/api-token-set-up.png" style="border: 2px solid lightblue; max-width: 70%;">

...then you're all set. If, however, you see this:

<img alt="API token not set up" src="/api-token-needs-generation.png" style="border: 2px solid lightblue; max-width: 70%;">

...then you need to click the button to generate a key.

Once you've generated your key, it needs to be available in a console. Either:
    
* start a new Bash console
* run the following in your current Bash console
  
        :::bash
        export API_TOKEN=yourapitoken 


## Install the PythonAnywhere helper scripts

Start a *new* Bash console (old ones won't have API access) and run this command
to install the PythonAnywhere helper scripts:

    pip3.5 install --user --upgrade pythonanywhere

(If you're on our "classic" image and don't have Python 3.6 available, you can use pip3.5 instead.)

## Install dehydrated

We use a package called "dehydrated" to get our Let's Encrypt certificate.
To install it, run the following in the Bash console:

    :::bash
    git clone https://github.com/lukas2511/dehydrated.git ~/dehydrated

Now we need some directories to store our keys, certificates and associated files:

    :::bash
    mkdir -p ~/letsencrypt/wellknown

## Set up static file mappings

You'll need your PythonAnywhere site to be able to serve static
files from the `wellknown` directory you just created. Head over to web app tab and set up a new
mapping (replacing "YOURUSERNAME" with your actual username):

* Static URL: `/.well-known/acme-challenge`
* Static Path: `/home/YOURUSERNAME/letsencrypt/wellknown`

The result should look like this (with a different username in the second column):

<img alt="Let's Encrypt static files setup" src="/letsencrypt-staticfiles.png" style="border: 2px solid lightblue; max-width: 70%;">

If you're using our password-protection feature for your web app, you'll also need to switch that off for the duration of this procedure;
you can turn it on again once you've got the certificate.

Next, reload your web app using the button at the top of the page.

## Configure dehydrated

Now we'll need to create a simple config file. Go back to the Bash console, and
create it like this (replacing "YOURUSERNAME" with your actual username):

    :::bash
    echo WELLKNOWN=/home/YOURUSERNAME/letsencrypt/wellknown > ~/letsencrypt/config

Next, if this is the first time you've ever created a Let's Encrypt certificate
from PythonAnywhere, you need to register with them by running this command:

    :::bash
    cd ~/letsencrypt
    ~/dehydrated/dehydrated --register --accept-terms

## Generate the certificate

Now we need to actually request a certificate (replace "www.yourdomain.com" with
the actual hostname of your website as it's specified on the "Web" page):

    :::bash
    cd ~/letsencrypt
    ~/dehydrated/dehydrated --config ~/letsencrypt/config --cron --domain www.yourdomain.com --out ~/letsencrypt --challenge http-01

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

## Install the certificate

To install the certificate, just run the following PythonAnywhere helper script (replacing www.yourdomain.com
with your actual domain name):

    pa_install_webapp_letsencrypt_ssl.py www.yourdomain.com

It should print out something like this:

    < Setting up SSL for www.yourdomain.com via API >
       \
        ~<:>>>>>>>>>
    < Reloading www.yourdomain.com via API >
       \
        ~<:>>>>>>>>>
      _________________________________________________________________
    /                                                                   \
    | That's all set up now :-) Your new certificate will expire         |
    | on 12 November 2018, so shortly before then you should             |
    | renew it (see https://help.pythonanywhere.com/pages/LetsEncrypt/)  |
    | and install the new certificate.                                   |
    \                                                                   /
      -----------------------------------------------------------------
       \
        ~<:>>>>>>>>>

If you get any errors, just email us at [support@pythonanywhere.com](mailto:support@pythonanywhere.com).

You're all set!  However, when your certificate expires (you can see that
the script told you when that will happen) you'll need to renew it.  See below
to find out how to do that -- or, indeed, how to set things up so that you don't
have to remember to do anything!


## Certificate renewal

**Tip**: _If you followed these instructions originally before mid-August 2018,
and have just come back here to renew the certificate, you will need to go through
the first two sections ("Make sure you've enabled the PythonAnywhere API" and
"Install the PythonAnywhere helper scripts") before running these commands._

Let's Encrypt certificates expire after 90 days, but you can renew them when
they're 60 days old -- meaning that you can renew one and get the new certificate
installed before the old one expires.

To renew your certificate, assuming you've left the static file mapping in
place and still have your `letsencrypt` and `letsencrypt.sh` directories, you
just need to re-run the dehydrated command:

    :::bash
    cd ~/letsencrypt
    ~/dehydrated/dehydrated --cron --domain www.yourdomain.com --out . --challenge http-01

and then run the certificate installation script again:

    pa_install_webapp_letsencrypt_ssl.py www.yourdomain.com

...but so that you don't need to remember to do that, you can set up a daily
scheduled task to do it for you.   Go to the "Tasks" tab, and set up a daily task
with this command:

    cd ~/letsencrypt && ~/dehydrated/dehydrated --cron --domain www.yourdomain.com --out . --challenge http-01 && pa_install_webapp_letsencrypt_ssl.py www.yourdomain.com

Don't forget to replace both instances of `www.yourdomain.com` with your actual
website's hostname.

Most days, this will fail with a message like this from the dehydrated script:

    Valid till Nov 12 15:23:59 2018 GMT (Longer than 30 days). Skipping renew!

Followed by a message from the `pa_install_webapp_letsencrypt_ssl.py` saying
something like this:

    POST to set SSL details via API failed, got <Response [400]>:{"cert":["Certificate has not changed."]}

...but this is harmless.  When your certificate really does have just 30 days to
go, it will succeed and your certificate will be renewed, and the new one
installed.


## Checking expiration date

Forgot when your certificate will expire?

Assuming your files are in the default directories, you can run this command:

    openssl x509 -enddate -noout -in ~/letsencrypt/www.yourdomain.com/cert.pem

and if you have multiple domains, you can create a bash script in your `letsencrypt` directory called `check_expirations.sh` that contains lines like this:

    echo www.domain1.com expires $(openssl x509 -enddate -noout -in ~/letsencrypt/www.domain1.com/cert.pem)
    echo www.domain2.com expires $(openssl x509 -enddate -noout -in ~/letsencrypt/www.domain2.com/cert.pem)
    echo www.domain3.com expires $(openssl x509 -enddate -noout -in ~/letsencrypt/www.domain3.com/cert.pem)

which you can then run with `bash ~/letsencrypt/check_expirations.sh`.
