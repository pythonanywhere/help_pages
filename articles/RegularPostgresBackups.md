
<!--
.. title: How to implement regular Postgres backups on PythonAnywhere
.. slug: RegularPostgresBackups
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



Your Postgres data on PythonAnywhere is fully protected against hardware failure. However, we do not automatically support rolling back to a point in time. If you want protection from accidental changes, you can set up a scheduled task to regularly back your data up to a file, which you can re-load into Postgres at a later date.

Here's an example of a command that can dump a particular database called "mydb":

    :::bash
    pg_dump --host=HOSTNAME --port=PORT --user=super --format=c --file=pgbackup`date -%F-%H%M`.dump mydb


You'll want to experiment with `pg_dump` and `pg_restore` until you have a backup command which you have confidence in -- remember, an untested backup procedure isn't a backup procedure at all!
