
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
account with minimal downtime:

1. setup your new account, and transfer all the settings and files over to the
   new account. This may include:
    - a git clone to get your source code over to the new account 
    - a database backup from the old account and restore to the new account database. See our help pages for doing [MySQL](/pages/MySQLBackupRestore) and [Postgres](/pages/RegularPostgresBackups) backup and restores.
    - [transfer over](/pages/UploadingAndDownloadingFiles) any other files on disk that your website is using that isn't in version control
    - install any libraries you had installed on your old account. Make sure
      the new libraries are the same versions as before. You may want to use a
      [requirements.txt](https://pip.pypa.io/en/stable/user_guide/#id1) file.
    - upgrade your new account to have the same settings as your old account
      (you need to do this now if your website has any dependencies on paid
      features; otherwise you should upgrade before step 3 to minimize website
      downtime)
2. create a new website on your new account (eg:
   `newaccount.pythonanywhere.com`) by going through manual configuration, and
   make sure that everything is connected and working. Some things to check
   include:
    - compare and reference any changes you had made to the
      `/var/log/www_mywebsite_com_wsgi.py` file in your old account, and
      make similar changes to the wsgi file on the new account
    - similarly, on the PythonAnywhere web tab, double check that website
      configurations such as the working directory, python version, virtualenv
      paths etc are setup correctly by comparing them with your old website
      configurations
    - on the new website, are [static file](/pages/StaticFiles) being served?
      Is the correct database connected? Are there any erroring urls/endpoints?
3. delete your website (`www.mywebsite.com`) from the old account
4. in your new account, [rename](/pages/UsingANewDomainForExistingWebApp)
   your `newaccount.pythonanywhere.com` website to `www.mywebsite.com`
5. take the new cname (`webapp-XXXXXX.pythonanywhere.com`) generated after the
   rename, and change the CNAME record at your domain registrar. See the bottom
   half of [this](/pages/OwnDomains) help page for more details.
