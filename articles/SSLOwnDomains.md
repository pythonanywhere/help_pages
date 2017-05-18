
<!--
.. title: Using SSL on your own domain
.. slug: SSLOwnDomains
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->




## In brief


We need you to point us to the location of two files, saved into your files area somewhere:

  * The **Private Key**, which should be **unencrypted**, ie it should start with `----BEGIN PRIVATE KEY` (or BEGIN RSA PRIVATE KEY)
  * The **Combined Certificate**, which consists of your certificate *and* the certificate chain sent to you by your vendor. It should have several BEGIN/END CERTICATE blocks.


## Detailed instructions


To enable SSL/HTTPS for your custom domain (that is, not `yourusername.pythonanywhere.com`, which gets it automatically), you'll need to get an SSL certificate. We don't sell them ourselves, so the first thing is to identify someone who will provide you with a certificate -- an SSL certificate vendor. An excellent choice for free certificates is [Let's Encrypt](/pages/LetsEncrypt), though you do have to renew the certificate every three months. Other companies charge for the certificates, but the certificates last longer. You may find that your domain name registrar provides them ([GoDaddy](//www.godaddy.com/) and Namecheap certainly do), so if you've found their customer service to be good, you might want to use them.

To get the certificate, you'll need to send them a text file called a "Certificate Signing Request" (CSR), which is basically an encoded representation of a request to a certificate-issuing organisation (a "Certification Authority", or CA -- your certificate vendor may be a CA themselves, or they may resell certificates from a CA) saying "please give me a SSL certificate for the following domain, signed by yourselves, that can only be unlocked using my private key." And in order to generate one of those, you'll need to generate a private cryptographic key. Here are detailed instructions on how to do that on PythonAnywhere.

  * From a Bash console on PythonAnywhere, generate the private key and CSR using the openssl command, like this (all on one line, replacing yourdomain.com appropriately):
    * `openssl req -new -newkey rsa:2048 -nodes -keyout yourdomain.com.key -out yourdomain.com.csr`
  * When the command asks you questions, you need to answer like this:
    * Common name: your site's hostname, eg. www.yourdomain.com The www. is important; a certificate for yourdomain.com won't work on www.yourdomain.com, and vice versa, so make sure you enter the one you use for your website.
    * Organisation: your business or other organisation name.
    * Organisation unit: your department -- just your organisation name again if you prefer.
    * City or locality: your city
    * State or province: as you'd expect. Leave blank if not applicable
    * Country: your two-letter ISO country code as per [this Wikipedia page](//en.wikipedia.org/wiki/ISO_3166-1#Officially_assigned_code_elements)
    * When it asks you for a passphrase, leave it blank.
  * Next, you need to provide the contents of the CSR (yourdomain.com.csr -- not the key!) to your certificate vendor. They will generate the certificate for you, or will get the CA to do so on their behalf, and send it back to you.
  * The certificate (which you should save on PythonAnywhere as yourdomain.com.cert) will be a text file starting with something like `BEGIN CERTIFICATE` (with some dashes on either side), then some encoded stuff, then `END CERTIFICATE` (again, with dashes). It's an encoded proof that the CA have certified that the person who owns the private key (the yourdomain.com.key file, which they haven't seen, but which was used to sign the CSR they did receive) definitely is you.
  * Because not all browsers necessarily trust your particular CA to certify people, you also often need a "certificate chain" AKA a "certificate bundle", which connects your certificate with someone who is trusted by all browsers. This is yet another text file, with several certificates in it. The certificate vendor should send it to you alongside your own certificate (typically marked as the certificate for Nginx servers). You can tell the difference between the two because your certificate will just have one "BEGIN/END" bit in it, while the chain will probably have several. (Some CAs are able to offer certificates that are trusted directly, though they tend to be the most expensive ones. Check with your certificate vendor if you're unsure.)
  * Once you have the certificate and the chain, create a new file which has your certificate at the top, then the chain afterwards. (You may have to add a newline so that you don't get the END line of your certificate on the same line as the BEGIN for the first line of the chain.) Save that as yourdomain.com.combined.cert
  * Get your private key: This is the private key that you would have created as part of the process of generating the CSR. You will need to give it to us unencrypted, so make sure that the key starts with the line `-----BEGIN PRIVATE KEY-----`. if you see something like `Proc-Type: 4,ENCRYPTED` then it's encrypted and you need to decrypt it before we can use it: `openssl rsa -in server.key.encrypted -out server.key`

Finally tell us in a "Send feedback" message (link at the top right of this page) where in your file storage on PythonAnywhere we can find the yourdomain.com.key and the yourdomain.com.combined.cert files, and which website it's for. We can take it from there.


## Verifying your key and certificate match

In the whole key-generation, csr-signing, cert receiving, file-concatenating dance, it is easy to get confused, particularly if you're managing more than one key or cert.  There's a step you can take right at the end to verify that your private-key/cert pair actually match.  Run these two commands:

    openssl rsa -noout -modulus -in yourdomain.com.key | openssl md5
    openssl x509 -noout -modulus -in yourdomain.com.combined.cert | openssl md5

*([source](https://kb.wisc.edu/middleware/page.php?id=4064))*

The output from the two commands (a hash of your public key) should match -- if they don't, it means the private key doesn't match the cert, and you need to start again, or check a different key.




## Forcing HTTPS


For some sites, you might not only want to offer an HTTPS connection to your users -- you might want to force all access to your site to go through HTTPS. [Here are some hints on how to do that for different web frameworks](/pages/ForcingHTTPS).
