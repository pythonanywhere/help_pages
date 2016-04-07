<!--
.. title: Web2py: how to do a fake migration to change database hostname
.. slug: web2pyfakemigration
.. date: 2016-04-07
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

As mentioned in our recent newsletter and mailshot, we're finally switching
off the old `mysql.server` address for our mysql service in favour of the 
new `yourusername.mysql.pythonanywhere-services.com` address, which has been
the default for the last year or so.

If you're a web2py user and your DAL connection string still contains
`mysql.server`, you'll need to change it. 

It's actually the exact same database underneath, just a different address for
it, but changing DAL details in web2py causes web2py to think you need to do a
database migration, and that causes problems.

To get around these, we've been advised by other web2py users that you should
go through the following procedure:


1. Enable `fake_migrate_all` by adding this argument to the DAL constructor:

      ```python
      db = DAL(..., fake_migrate_all=True)
      ```

2. Load your site, at least once,

3. Disable `fake_migrate_all` by removing that argument again. This is important,
  because otherwise your web2py migrations will be disabled forever, and you won't
  be able to make changes to your models any more, and web2py will be confused...


