
<!--
.. title: How to move a domain from one PythonAnywhere user account to another
.. slug: MovingDomainToAnotherPythonAnywhereAccount
.. date: 2018-01-01 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Here is a sample checklist to move an existing website (eg:
`www.mywebsite.com`) from one PythonAnywhere account to another PythonAnywhere
account:

1. setup your new account, and transfer all the files over to the new
   account. This may include:
    - a git clone to get your source code over to the new account 
    - a database backup from the old account and restore to the new account database. See our help pages for doing [MySQL](/pages/MySQLBackupRestore) and [Postgres](/pages/RegularPostgresBackups) backup and restores.
    - [transfer over](/pages/UploadingAndDownloadingFiles) any other files on disk that your website is using that isn't in version control
2. create a new website on your new account (eg:
   `newaccount.pythonanywhere.com`) and make sure that everything is
   connected and working. Some things to check include:
    - compare and reference any changes you had made to the
      `/var/log/www_mywebsite_com_wsgi.py` file in your old account, and
      make similar changes to the wsgi file on the new account
    - are [static file mappings](/pages/StaticFiles) setup correctly
    - are the correct databases connected
    - are there any erroring urls/endpoints on your site
3. delete your website (`www.mywebsite.com`) from the old account
4. in your new account, [rename](/pages/UsingANewDomainForExistingWebApp)
   your `newaccount.pythonanywhere.com` website to `www.mywebsite.com`
