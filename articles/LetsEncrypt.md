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
files from your `wellknown` directory. Head over to the web tab and set up a new
mapping:

* Static URL: `/.well-known/acme-challenge`
* Static Path: `/home/<your_username>/letsencrypt/wellknown`

and then **reload your web app**
    

Now we need to create a private key:

    :::bash
    openssl genrsa 4096 > user.key
    
Keep this key file safe. It's how the Let's Encrypt servers know who you are.
    
    
We'll need to create a simple config file. Put the following (with suitable
replacements) into a file at `/home/<your_username>/letsencrypt/config`

    :::bash
    WELLKNOWN=/home/<your_username>/letsencrypt/wellknown
    
Now we need to actually request a certificate:

    :::bash
    ~/letsencrypt.sh/letsencrypt.sh --cron --domain <your_web_app_name> --privkey user.key --out . --challenge http-01
    
If this is successful, you'll now have a directory named `<your_domain_name>` in
your `letsencrypt` directory and your certificate and key will be in there. 

To get your certificate installed email support@pythonanywhere.com to let us
know that you want us to install your certificate. Include your username, the
directory path, and the domain name and we'll do the rest.


## Certificate renewal

To renew your certificate, assuming you've left the static file mapping in
place and still have your `user.key` file and the `letsencrypt.sh` directory, you
just need to re-run:

    :::bash
    cd ~/letsencrypt
    ~/letsencrypt.sh/letsencrypt.sh --cron --domain <your_web_app_name> --privkey user.key --out . --challenge http-01
    
and then let us know that you have a new certificate and where we can find it.


