
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




If you already have a web application up and running on PythonAnywhere and you want to point a new domain at it, do one of these:

## If you have a spare web app that you can use temporarily
  * Add a new web app from the "Web" tab, entering your new domain name on the first page and selecting "Manual config" on the second.
  * Confirm that you have a "Hello world" page running on your new domain name.
  * Start a new Bash console.
  * Copy the WSGI configuration file for the existing web app on top of the one for your new domain. The files are in `/var/www`. The exact filenames will depend on the web app names, but it will look something like this:

        :::bash
        cp /var/www/www_oldwebappdomain_com_wsgi.py /var/www/www_newwebappdomain_com_wsgi.py


  * Copy the "Static files" settings from the "Web" tab for your old web app to the tab for your new app.
  * If you're using a virtualenv in your old web app, copy the directory for that over too.
  * Reload your new web app.
  * Visit your new domain. You should now see the web app that was on your old domain is running there too.

## If you don't have a spare web app
  * Make a note of the following settings:
    * All entries in the "Static Files" section.
    * The path to your virtualenv, if you're using one.
    * The enabledness, username and password under the "Password protection" section.
  * Delete you existing web app. **Note**:  This **only** deletes the configuration of the webapp. It **does not** delete your code!
  * Add a new web app from the "Web" tab, entering your new domain name on the first page and selecting "Manual config" on the second.
  * Start a new Bash console.
  * Copy the WSGI configuration file for the existing web app on top of the one for your new domain. The files are in `/var/www`. The exact filenames will depend on the web app names, but it will look something like this:

        :::bash
        cp /var/www/www_oldwebappdomain_com_wsgi.py /var/www/www_newwebappdomain_com_wsgi.py

  * Copy all the settings from your notes to the new web app.
  * Reload your new web app.
  * Visit your new domain. You should now see the web app that was on your old domain is running there.