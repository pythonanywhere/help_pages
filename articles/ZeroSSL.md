<!--
.. title: ZeroSSL: a free, web-based, Let's Encrypt SSL cert provider
.. slug: ZeroSSL
.. date: 2016-07-20
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->
PythonAnywhere has already provided walkthroughs for creating SSL certificates:
   * via [commercial providers](https://help.pythonanywhere.com/pages/SSLOwnDomains) and 
   * a [command-line method](https://help.pythonanywhere.com/pages/LetsEncrypt) for free Let's Encrypt certificates. 

A new service, **ZeroSSL**, bridges the gap by making free Let's Encrypt certs as easy (easier?) to generate as commercial providers. This guide will walk you through generating your first ZeroSSL certificate. *Note: I have no affiliation whatsoever with ZeroSSL, other than I used their service.*

### Let's Encrypt SSL certificates have a 90-day expiration period, which means you'll need to be extra vigilant to prevent your certificate from expiring. Commercial services can generate multi-year (and multi-domain) certificates. If re-generating every 90 days will be a problem, you should probably just pay for an annual (or longer) certificate and not risk your site's security.

We will start by generating a CSR (Certificate Signing Request) the same way we would for a commercial provider<sup>[1](#footnote_csr)</sup>. The following is copied from PythonAnywhere's SSL guide:

>  * From a Bash console on PythonAnywhere, generate the private key and CSR using the openssl command, like this (all on one line, replacing yourdomain.com appropriately):
    * `openssl req -new -newkey rsa:2048 -nodes -keyout yourdomain.com.key -out yourdomain.com.csr`
  * When the command asks you questions, you need to answer like this:
    * Common name: your site's hostname, eg. www.yourdomain.com **The www. is important; a certificate for yourdomain.com won't work on www.yourdomain.com, and vice versa, so make sure you enter the one you use for your website.**
    * Organisation: your business or other organisation name.
    * Organisation unit: your department -- just your organisation name again if you prefer.
    * City or locality: your city
    * State or province: as you'd expect. Leave blank if not applicable
    * Country: your two-letter ISO country code as per [this Wikipedia page](//en.wikipedia.org/wiki/ISO_3166-1#Officially_assigned_code_elements)
    * When it asks you for a passphrase, leave it blank.
  * Next, you need to provide the contents of the CSR (yourdomain.com.csr -- not the key!) to your certificate vendor. They will generate the certificate for you, or will get the CA to do so on their behalf, and send it back to you.
  
Download the `.csr` file to your computer or other secure location and delete it from your PA filesystem. You will need the `.key` file later so you can leave it up.

Now lets visit [ZeroSSL](https://zerossl.com/). Scroll down to the **FREE SSL Certificate Wizard** and click `Start`. 

  * Enter an email address
  * Leave "Domains" blank. *Remember, your cert will be only valid for the __exact__ Common Name you specified above.*
  * Leave "Let's Encrypt key" blank (no, the `.key` file you received from PA does NOT go here).
  * Paste the text of your `.csr` request in the CSR box. Paste the entire file, including the --BEGIN-- and --END-- lines. 
  * Select a verification method (I believe DNS is easier to set up) and accept the TOS and SA.

When you first click `Next`, ZeroSSL will generate a public key for you. Download this and save it, this will allow you to generate your future certificates. Next time, paste that key into the box instead of generating a new one.

Click `Next` again, and ZeroSSL will display instructions on verifying ownership of your domain. DNS verification only requires you to add a TXT record, I assume HTTP verification requires you to upload a file, but I did not try that.

Click `Next` one last time, and assuming the verification was successful, you've got a shiny new SSL certificate! Download it and again, keep a copy in a secure location. Make a note of your user id.

Upload your `.crt` file to your PA filesystem (probably the same directory as your private key). The certificate already contains the "intermediate certificate," so no need to combine certs as in the other SSL tutorials.

The final step is notifying the great PythonAnywhere staff:
> Finally tell us in a "Send feedback" message (link at the top right of this page) where in your file storage on PythonAnywhere we can find the yourdomain.com.key and the yourdomain.com.combined.cert files, and which website it's for. We can take it from there.

I have found that [DigiCert](https://www.digicert.com/help/)'s SSL verification service provides peace of mind. I would also suggest removing your `.crt` and `.key` files from PA once the certificate has been installed on your server and SSL has been verified.

### Add an entry to your iCal or Google Calendar to renew your certificate about 84 days from now!!

___

<a name="footnote_csr">1</a>: ZeroSSL offers to create a CSR request for you, which would allow you to bypass the PA command-line completely. However, the nature of private keys would indicate that generating them yourself is the most secure option. *(I have no training or deep knowledge regarding internet security, do not trust my opinion)*
