
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
  1. Create a new entry on the [Web tab](/pages/OwnDomainsweb_app_setup) for your new domain 
  1. Create a CNAME record with your domain provider, pointing at the new web app 


##Purchasing a domain name


We don't recommend any particular domain registrar, they're all pretty similar. Just google around, compare prices (they should all be very similar), and pick the one that seems to have the friendliest user interface. 


##Creating a PythonAnywhere web app for your new domain


If you want to create a brand new web app associated with the domain, just click the "Add a new web app" button on the Web tab, specify the domain on the first step, and go on to choose your python version, framework and so on. 

If you want your domain to show a web app that you've already created, the process is a little more complicated. Let's say that the app you want to show is currently displayed at `jane.pythonanywhere.com`, and you want it to appear at `www.yourdomain.com`. 

  * Click the "Add a new web app" button, and on the first page specify your domain (including the www.). 
  * On the next page, select "Manual configuration", then click next and complete the setup process. 
  * Next we want to copy the WSGI file configuration from your old webapp to the new one 
    * click through to the old web app config for `jane.pythonanywhere.com`
    * click the link to the wsgi configuration file 
    * copy all the contents (using Ctrl+A, Ctrl+C for example) 
    * click back to go back to the web tab 
    * click through to the tab for your new web app, `www.yourdomain.com`. 
    * click the link to *its* wsgi configuration file 
    * Delete all the existing contents, and paste in the code from the old file 
    * Hit "Save", and go back to the web tab. 

You're now ready to do the CNAME config. take a note of the CNAME config on the web tab, it'll look something like this: **webapp-XXXX.pythonanywhere.com**. 


##Configuring the domain at the domain registrar


Once you've purchased your domain and created the new webapp config on pythonanywhere, you'll want to find the configuration screen on your domain provider that allows you to set up a *CNAME*. 

The CNAME record will point (say) www.yourdomain.com to the value specified on the "Web" tab for your application; this will be of the form **webapp-XXXX.pythonanywhere.com**. This tells [the domain name system](//en.wikipedia.org/wiki/Domain_Name_System) that when someone asks for your website, they should get it from us. 

CNAME records have two parts. The **Alias** and the *Canonical Name*. The alias in this case should be **www**. The address should be the value from the "Web" tab. 

Different DNS providers call them different things. So: 

  * Alias, AKA: domain name, Alias name, 
  * Canonical Name, AKA: the address, FQDN, Fully Qualified Domain Name, or Host Name. 


##Testing your configuration


CNAME changes can take a little while to propagate from your registrar to the rest of the Internet. You can see whether the change has reached PythonAnywhere yet by looking at the app on the web tab; it will show a warning if the CNAME it sees for your domain is not the one it expects. You can also use this [CNAME lookup tool](https://www.whatsmydns.net/) if you want to get a second opinion -- enter your web app's name (including the "www") and select "CNAME" from the dropdown. It will check the CNAME from a bunch of different places around the Internet, which will give you a feel for how far the setup has got. 

If your CNAME is still not working after a couple of hours, you should double-check your setup. 


##Specific DNS providers


  * [godaddy.com](https://ca.godaddy.com/help/add-a-cname-record-19236)


##Domains without a www prefix (naked domains)


One small problem with setting up DNS like this is that it doesn't allow "naked domains" -- that is, you can have your site at `www.yourdomain.com` or `somethingelse.yourdomain.com`, but not at just `yourdomain.com`. [Here's some more information about that, and some recommendations](/pages/NakedDomains). 
