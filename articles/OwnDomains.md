
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


##Configuring the domain at the domain registrar


To use your own domain name with a PythonAnywhere web app there are two steps 

  1. Purchase a domain name from a [domain name registry](https://en.wikipedia.org/wiki/Domain_name_registry). 
  1. Create a CNAME record for (say) www.yourdomain.com pointing to the value specified on the "Web" tab for your application; this will be of the form **webapp-XXXX.pythonanywhere.com**. This tells [the domain name system](//en.wikipedia.org/wiki/Domain_Name_System) that when someone asks for your website, they should get it from us. 


##Domains without a www prefix (naked domains)


One small problem with setting up DNS like this is that it doesn't allow "naked domains" -- that is, you can have your site at `www.yourdomain.com` or `somethingelse.yourdomain.com`, but not at just `yourdomain.com`. [Here's some more information about that, and some recommendations](/pages/NakedDomains). 


##General Instructions


CNAME records have two parts. The **Alias** and the *Canonical Name*. The alias in this case should be **www**. The address should be the value from the "Web" tab. 

Different DNS providers call them different things. So: 

  * Alias, AKA: domain name, Alias name, 
  * Canonical Name, AKA: the address, FQDN, Fully Qualified Domain Name, or Host Name. 


##Testing your configuration


CNAME changes can take a little while to propagate from your registrar to the rest of the Internet. You can see whether the change has reached PythonAnywhere yet by looking at the app on the web tab; it will show a warning if the CNAME it sees for your domain is not the one it expects. You can also use this [CNAME lookup tool](https://www.whatsmydns.net/) if you want to get a second opinion -- enter your web app's name (including the "www") and select "CNAME" from the dropdown. It will check the CNAME from a bunch of different places around the Internet, which will give you a feel for how far the setup has got. 

If your CNAME is still not working after a couple of hours, you should double-check your setup. 


##Specific DNS providers


  * [godaddy.com](//support.godaddy.com/help/article/7921/adding-or-editing-cname-records)


##Associating a PythonAnywhere web app with your domain


If you want to create a new web app associated with the domain, just click the "Add a new web app" button on the Web tab, and specify the domain on the first page. 

If you want your domain to show a web app that you've already created, the process is a little more complicated. Let's say that the app you want to show is currently displayed at `fred.pythonanywhere.com`, and you want it to appear at `www.yourdomain.com`. Once you've done the CNAME setup as described above, here's what you do: 

  * Click the "Add a new web app" button, and on the first page specify your domain (exactly as you did at the registrar -- don't forget the `www` if you used it there). 
  * On the next page, select "Manual configuration", then click next and complete the setup process. This will set up a web app on your domain with a simple "Hello world" kind of page. 
  * Now comes the more difficult bit; you need to replace the PythonAnywhere configuration for your new domain with the one for the old domain. This configuration is done by files inside `/var/www` in your account. Each domain you are running a web app for has a file there named after the domain, with dots replaced by underscores and `_wsgi.py` at the end. 
  * So: start a bash console 
  * In it, copy the configuration for your existing app on top of the new app, with a command like this (don't forget to change the filenames to match your original domain and your new domain: 
    * `cp /var/www/fred_pythonanywhere_com_wsgi.py /var/www/www_yourdomain_com_wsgi.py`
  * Finally, go back to the Web tab and reload the web app for your new domain. 

That should do the job. 
