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

Let's Encrypt provide free SSL certificates for HTTPS. It's possible, but a
little fiddly to get a Let's Encrypt certificate working on PythonAnywhere.
Here's how:

The standard letsencrypt client needs all kinds of root privileges.  Instead,
we use an alternative called "letsencrypt-nosudo":

    git clone https://github.com/diafygi/letsencrypt-nosudo
    cd letsencrypt-nosudo

Next we follow the instructions from the [letsencrypt-nosudo github page](https://github.com/diafygi/letsencrypt-nosudo).
We use openssl (which is
preinstalled on PythonAnywhere) to create a user private/public key pair, then
a private key and signing request for our domain.  Next we use the
letsencrypt-nosudo command-line script to get our certificate signed by
letsencrypt.  To go through the letsencrypt "ACME" verification process, we'll
need to host a static file on our domain.

    :::bash
    # user public/private key pair
    openssl genrsa 4096 > user.key
    openssl rsa -in user.key -pubout > user.pub

    # domain private key and csr
    export DOMAIN=www.obeythetestinggoat.com  # replace this with your own domain name!
    openssl genrsa 4096 > $DOMAIN.key
    openssl req -new -sha256 -key $DOMAIN.key -subj "/CN=$DOMAIN" > $DOMAIN.csr

    # now launch the signing script and follow the instructions!
    python sign_csr.py --file-base --public-key user.pub $DOMAIN.csr > $DOMAIN.crt

At this point it'll ask you to run a series of command-line scripts in another
window.  Use ctrl+z if you know how to do that, or start a new Bash console,
and follow the instructions.  You'll have to be in the same directory as you
were earlier

    :::bash
    cd letsencrypt-nosudo
    export DOMAIN=www.obeythetestinggoat.com  # in case this comes in useful again, replace with yours
    openssl dgst -sha256 -sign user.key # etc etc as per instructions

There's two of those signing steps, and then it will ask you to:

    STEP 4: Please update your server to serve the following file at this URL:

    URL: http://www.obeythetestinggoat.com/.well-known/acme-challenge/asdfasdfasdfasdfasdf
    File contents: "qwerqwerqwerqwerqwerqwerqwer"

At this point you'll need your pythonanywhere site to be able to serve a static
file.  Head over to the web tab and set up a new mapping:

* Static URL: /.well-known/
* Static Path: /tmp/letsencrypt.well-known/

After hitting **Reload** on my web app to get that live, put the
static file there with the contents asked for:

    :::bash
    mkdir -p /tmp/letsencrypt.well-known/acme-challenge
    # replace asdfasdfasdf and qwerqwerqwer as appropriate
    echo "qweqwerqwerqwerqwerqwer" > /tmp/letsencrypt.well-known/acme-challenge/asdfasdfasdfasdf
    # check it worked:
    export DOMAIN=www.obeythetestinggoat.com  # replace with yours if you're in a different Bash console, skip if you used ctrl+z
    curl http://$DOMAIN/.well-known/acme-challenge/asdfasdfasdfasdf
    # should show qwerwqerqwer or equivalent

Once this is working, go back to the original console and continue the script:

    :::bash
    cat $DOMAIN.crt
    # should -----BEGIN CERTIFICATE----- etc etc!


The Let's Encrypt certificate is missing the intermediate certificate, so
you'll need to get it from Let's Encrypt and add it to your certificate chain:

    :::bash
    curl https://letsencrypt.org/certs/lets-encrypt-x3-cross-signed.pem.txt >> $DOMAIN.crt

And now the last step is to hand over two files to the pythonanywhere admins.
Put the following 2 files somewhere in your home directory on PythonAnywhere:

* www.obeythetestinggoat.com.key
* www.obeythetestinggoat.com.crt

and send us Feedback or an email to support@pythonanywhere.com with the
location of the files.

It's not ideal at the moment, because of the manual step involved -- we, the
pythonanywhere admins, currently have to manually update your certificate files
for you.  But the other steps could be automated pretty well.  And this should
motivate us to get some kind of automatic process for HTTPS certificates in
place!
