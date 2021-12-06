<!--
.. title: Setting up a custom domain on PythonAnywhere
.. slug: CustomDomains
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


If you have a paid account on PythonAnywhere, you can set up websites on a
custom domain -- that is, a domain that is not `your-username.pythonanywhere.com`

There are three steps

  1. (if you haven't already), purchase a domain name from a [domain name registrar](https://en.wikipedia.org/wiki/Domain_name_registrar).
  1. Create a new entry on the [Web tab](https://www.pythonanywhere.com/web_app_setup) for your new domain
  1. Create a CNAME record with your domain provider, pointing at the new website

There are two optional, but recommended steps, to make your site secure.  Do
these *after* you've done the steps above:

  4. [Set up an HTTPS/SSL certificate](/pages/HTTPSSetup)
  5. [Force HTTPS on your website](/pages/ForcingHTTPS)


## Purchasing a domain name

We don't recommend any particular domain registrar, they're all pretty similar.
Just google around, compare prices (they should all be very similar), and pick
the one that seems to have the friendliest user interface.


## Creating a PythonAnywhere website for your new domain

For best performance and reliability on PythonAnywhere, we *strongly* recommend
that you use a CNAME to point your domain at our servers.  Without
going too much into the technical details, a CNAME means that you don't need
to do any DNS configuration beyond the initial setup; we can manage everything
for you, so if (for example) the IP address associated with your website gets
blocked in some country, or if it's subjected to a denial-of-service attack,
we can move your website over to a different IP address without you needing to
do anything.

The one restriction that CNAMEs have is that they cannot be used for "naked" or "apex"
domains.  To make that more concrete, you can use `www.yourdomain.com` or
`somethingelse.yourdomain.com` for the website, but not `yourdomain.com`.
But that doesn't have to be a problem; you can host your site on `www.yourdomain.com`
and then set things up so that people who visit `yourdomain.com` are automatically
redirected to `www.yourdomain.com`.  There's more information on that last bit later on.

Given all that, here's how to create the website:

**If you don't have a website for it yet**

Just click the "Add a new web app" button on the Web tab.  In the first step,
it will ask you for the domain name to use.  You should specify the
fully-qualified domain name -- that is, `www.yourdomain.com`, not just
`yourdomain.com`.  Next go on to choose your Python version, framework and so on.


**If you already have a website that you want to use**

[This help page explains how to use a new domain for existing website](https://help.pythonanywhere.com/pages/UsingANewDomainForExistingWebApp),
for example if the site you want to show is currently displayed at
`jane.pythonanywhere.com`, and you want it to appear at `www.yourdomain.com`.
Once again, you should specify the
fully-qualified domain name -- that is, `www.yourdomain.com` rather than
`yourdomain.com`.


## Configuring the domain at the domain registrar

Once you've purchased your domain and created the new website config on
PythonAnywhere, you'll want to find the configuration screen on your domain
provider that allows you to set up a CNAME record.

The CNAME record will point `www.yourdomain.com` to the value specified on
the "Web" tab for your application; this value will be of the form
`webapp-XXXX.pythonanywhere.com` where `XXXX` is some number or other (unless your site
is set up to support [legacy versions of TLS](/pages/TLSVersionSupport), in which case
it will be the value from that page).
Setting up this kind of record tells [the domain name system](//en.wikipedia.org/wiki/Domain_Name_System)
that when someone asks for your website, they should get it from one of the servers
that make up PythonAnywhere.

*Note: your website itself will not show up at the `webapp-XXXX.pythonanywhere.com`
address.  It's just an identifier for a server.*

CNAME records have two parts. The **Alias** and the **Canonical Name**. The alias
in this case should be `www`. The address should be the value from the "Web"
tab -- the one like `webapp-XXXX.pythonanywhere.com`.

Different DNS providers call them different things.

  * Alias: domain name, alias name, host, or just "name"
  * Canonical Name: the address, FQDN, Fully Qualified Domain Name, points to, or Host Name.

Specifically, if you're using GoDaddy, the alias is called the "host", and the canonical name
is called "points to".

If you're using OVH as your registrar, you may also see that they've automatically
created a TXT record for `www.yourdomain.com` with a value of `"3|welcome"` --
you'll need to delete that, as a domain can't have both a TXT record and a CNAME.

See [here](/pages/DNSPrimer) for more information about how DNS works. 


## Notes for specific DNS providers

Here's how to set up a CNAME for some popular registrars:

  * [GoDaddy](https://ca.godaddy.com/help/add-a-cname-record-19236)
  * [NameCheap](https://www.namecheap.com/support/knowledgebase/article.aspx/9646/2237/how-to-create-a-cname-record-for-your-domain)
  * [Gandi](https://wiki.gandi.net/en/dns/zone/cname-record)


## Testing your configuration

CNAME changes can take a little while to propagate from your registrar to the
rest of the Internet. You can see whether the change has reached PythonAnywhere
yet by looking at the site on the "Web" page; it will show a warning if the CNAME it
sees for your domain is not the one it expects.

You can also use this [CNAME lookup tool](https://www.whatsmydns.net/) if you
want to get a second opinion: Enter your website's name (including the `www.`
prefix) and select "CNAME" from the dropdown. It will check the CNAME from a
bunch of different places around the Internet, which will give you a feel for
how far the propagation has got.

If your CNAME is still not working after a couple of hours, you should
double-check your setup.  If it all looks OK, but the site isn't working,
[check out our DNS troubleshooting page](/pages/TroubleshootingDNS).


## Recommended: set up HTTPS for a secure site.

Once you have website working, you should set up HTTPS.  There are two steps to
do for this:

  1. [Set up an HTTPS/SSL certificate for your domain](/pages/HTTPSSetup)
  1. [Force HTTPS on your website](/pages/ForcingHTTPS)


## Optional: Set up a naked domain redirect

Most people want their site set up so that when someone goes to
`http://yourdomain.com/` they are redirected to `http://www.yourdomain.com/`,
or if they go to `http://yourdomain.com/foo` they are redirected to
`http://www.yourdomain.com/foo`, and so on.  Check out [this help page](/pages/NakedDomains)
for details on how to do that.


## Optional: Use custom PythonAnywhere subdomain

Usually custom domain means a domain you own, but we made possible to create 
custom subdomains based on username. You could name your web 
`whatever-yourusername.pythonanywhere.com` and it would work. It's still
available to paid accounts only. 


## Still having trouble?

We have [a separate page](/pages/TroubleshootingDNS/) dedicated to handling
specific problems -- 95% of DNS problems can be sorted quickly by following the
instructions there.

If you still can't get it working, [contact us](mailto:support@pythonanywhere.com) -- please
attach a screenshot of the DNS configuration you've set up on your registrar's site.

