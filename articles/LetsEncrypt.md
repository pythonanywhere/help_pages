<!--
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

The standard letsencrypt client needs all kinds of root privileges.  Instead,
we use an alternative called "letsencrypt.sh"

To get it, run the following in a Bash console in your home directory:

    :::bash
    git clone https://github.com/lukas2511/letsencrypt.sh.git ~/letsencrypt.sh
    
    
Now we need some directories to store our keys, certificates and associated files:

    :::bash
    mkdir -p ~/letsencrypt/wellknown
    cd ~/letsencrypt
    
You'll also need your pythonanywhere site to be able to serve static
files from your `wellknown` directory. Head over to web app tab and set up a new
mapping:

* Static URL: `/.well-known/acme-challenge`
* Static Path: `/home/yourusername/letsencrypt/wellknown`

and then **reload your web app**
    
We'll need to create a simple config file. Put the following (with suitable
replacements) into a file at `/home/yourusername/letsencrypt/config`

    :::bash
    WELLKNOWN=/home/yourusername/letsencrypt/wellknown
    
Now we need to actually request a certificate:

    :::bash
    ~/letsencrypt.sh/letsencrypt.sh --cron --domain www.yourdomain.com --out . --challenge http-01
    # susbtitute www.yourdomain.com with your own domain name, including the www. part
    
If this is successful, you'll now have a directory named `www.yourdomain.com` in
your `letsencrypt` directory and your certificate and key will be in there. 

* **Keep your `/home/yourusername/letsencrypt` directory safe**. It contains
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
    ~/letsencrypt.sh/letsencrypt.sh --cron --domain www.yourdomain.com --out . --challenge http-01
    
and then let us know that you have a new certificate and where we can find it.


