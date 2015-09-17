
<!--
.. title: Using a new domain for existing webapp
.. slug: UsingANewDomainForExistingWebApp
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->




If you already have a web application up and running on PythonAnywhere and you want to point a new domain at it, do this: 

  * Add a new web app from the "Web" tab, entering your new domain name on the first page and selecting "Manual config" on the second. **Note**: if your account doesn't support enough web apps to add a new one, then drop us a line using the "Send feedback" link above; we can give your account an extra web app temporarily. 
  * Confirm that you have a "Hello world" page running on your new domain name. 
  * Start a new Bash console. 
  * Copy the WSGI configuration file for the existing web app on top of the one for your new domain. The files are in `/var/www`. The exact filenames will depend on the web app names, but it will look something like this: 

        cp /var/www/www_oldwebappdomain_com_wsgi.py /var/www/www_newwebappdomain_com_wsgi.py


  * Copy the "Static files" settings from the "Web" tab for your old web app to the tab for your new app. 
  * If you're using a virtualenv in your old web app, copy the directory for that over too. 
  * Reload your new web app 
  * Visit your new domain. You should now see the web app that was on your old domain is running there too. 

**Note**: If you don't have a spare webapp to copy the configuration to, you can instead make a note of the static files and other configuration on the webapp tab and then delete the current webapp. This **only** deletes the configuration of the webapp. It **does not** delete your code! 
