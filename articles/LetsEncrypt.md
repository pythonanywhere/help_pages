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
    ~/dehydrated/dehydrated --cron --domain www.yourdomain.com --out . --challenge http-01
    # susbtitute www.yourdomain.com with your own domain name, including the www. part

If this is successful, you'll now have a directory named `www.yourdomain.com` in
your `letsencrypt` directory and your certificate and key will be in there.

* **Keep your `/home/YOURUSERNAME/letsencrypt` directory safe**. It contains
  the information necessary for you to renew your certs.

To get your certificate installed email support@pythonanywhere.com to let us
know that you want us to install your certificate. Include your username, the
directory path, and the domain name and we'll do the rest.


## Certificate renewal

To renew your certificate, assuming you've left the static file mapping in
place and still have your `letsencrypt` and `letsencrypt.sh` directories, you
just need to re-run:

    :::bash
    cd ~/letsencrypt
    ~/dehydrated/dehydrated --cron --domain www.yourdomain.com --out . --challenge http-01

and then let us know that you have a new certificate and where we can find it.


