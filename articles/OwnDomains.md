
<!--
.. title: Setting up a custom domain on PythonAnywhere
.. slug: OwnDomains
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



If you have a paid account on PythonAnywhere, you can set up web apps on your own domain -- that is, a domain that is not *your-username*`.pythonanywhere.com`

There are three steps

  1. (if you haven't already), purchase a domain name from a [domain name registry](https://en.wikipedia.org/wiki/Domain_name_registry).
  1. Create a new entry on the [Web tab](https://www.pythonanywhere.com/web_app_setup) for your new domain
  1. Create a CNAME record with your domain provider, pointing at the new web app


##Purchasing a domain name


We don't recommend any particular domain registrar, they're all pretty similar. Just google around, compare prices (they should all be very similar), and pick the one that seems to have the friendliest user interface.


##Creating a PythonAnywhere web app for your new domain

**PythonAnywhere web app doesnot exist**

Just click the "Add a new web app" button on the Web tab, specify the domain on the first step, and go on to choose your python version, framework and so on.

**PythonAnywhere web app already exists**

[This help page explains how to use a new domain for existing webapp](https://help.pythonanywhere.com/pages/UsingANewDomainForExistingWebApp),
for example if the app you want to show is currently displayed at `jane.pythonanywhere.com`, and you want it to appear at `www.yourdomain.com`.


##Configuring the domain at the domain registrar

Once you've purchased your domain and created the new webapp config on PythonAnywhere, you'll want to find the configuration screen on your domain provider that allows you to set up a *CNAME*.

The CNAME record will point (say) www.yourdomain.com to the value specified on the "Web" tab for your application; this will be of the form **webapp-XXXX.pythonanywhere.com**. This tells [the domain name system](//en.wikipedia.org/wiki/Domain_Name_System) that when someone asks for your website, they should get it from us.

CNAME records have two parts. The **Alias** and the *Canonical Name*. The alias in this case should be **www**. The address should be the value from the "Web" tab.

Different DNS providers call them different things. So:

  * Alias, AKA: domain name, Alias name,
  * Canonical Name, AKA: the address, FQDN, Fully Qualified Domain Name, or Host Name.


##Testing your configuration

CNAME changes can take a little while to propagate from your registrar to the rest of the Internet. You can see whether the change has reached PythonAnywhere yet by looking at the app on the web tab; it will show a warning if the CNAME it sees for your domain is not the one it expects.

You can also use this [CNAME lookup tool](https://www.whatsmydns.net/) if you want to get a second opinion: Enter your web app's name (including the `www.` prefix) and select "CNAME" from the dropdown. It will check the CNAME from a bunch of different places around the Internet, which will give you a feel for how far the setup has got.

If your CNAME is still not working after a couple of hours, you should double-check your setup.


##Specific DNS providers

  * [godaddy.com](https://ca.godaddy.com/help/add-a-cname-record-19236)
  * [gandi.net](https://wiki.gandi.net/en/dns/zone/cname-record)


##Domains without a www prefix (naked domains)

One small problem with setting up DNS like this is that it doesn't allow "naked domains" -- that is, you can have your site at `www.yourdomain.com` or `somethingelse.yourdomain.com`, but not at just `yourdomain.com`. [Here's some more information about that, and some recommendations](/pages/NakedDomains).
