
<!--
.. title: Can I use Postgres on PythonAnywhere?
.. slug: Postgres
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



Yes! But you need a paying account.

If you want to use a Postgres server run by us:
-----------------------------------------------

  * If you have a free account, go to the Account page, and click on one of the
    buttons for upgrading to a paid account. In the dialog that appears, switch
    the Postgres option on, choose how much disk space you want for your
    Postgres databases, choose any other paid features you
    want, and then click "Upgrade to this custom plan". This will take you
    through a payment confirmation process.
  * If you already have paying account, go to the Account page, and click on
    the "Customize your plan" button. The popup window will be pre-configured
    with all of your current custom plan settings, so you just need to switch
    the Postgres option on, choose how much disk space you want for your PG
    databases, and then click "Switch to this custom plan". This will take you
    through the normal payment confirmation process.  (You won't be charged the
    new price until your next billing date.)

Once that's done, go to the "Databases" tab, then click the "Postgres" button.
You'll have a new option to create a Postgres server and specify the
adminstrator password.


If you want to use a Postgres server run by some other service
--------------------------------------------------------------

Just upgrade to any paid PythonAnywhere plan -- the cheapest one will work
just fine.  You don't need to check the "Postgres" option -- that is for
creating a PythonAnywhere-hosted Postgres server, which of course you don't
need.

Paid PythonAnywhere accounts have unrestricted Internet access
so once the upgrade has gone through, you will be able to connect to your
remote Postgres instance.
