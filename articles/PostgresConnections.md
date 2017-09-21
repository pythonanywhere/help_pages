<!--
.. title: Increasing the number of connections for your PostgreSQL server
.. slug: PostgresConnections
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

If you get an error from your PythonAnywhere PostgreSQL server saying

    OperationalError: FATAL: sorry, too many clients already

...you should first check your code to make sure that you're not leaving
connections open.

If you're sure you're not, you can increase the number of connections that the
server will allow at any one time.   Firstly, run the following command in a
Postgres console:

    alter system set max_connections = 30;

(or whatever number of connections you'd like).

Next, you need to restart your Postgres server.   Right now, you need to
contact us -- just drop us a line at
[support@pythonanywhere.com](mailto:support@pythonanywhere.com).   Don't
forget to let us know what your username is!
