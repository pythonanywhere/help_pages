
<!--
.. title: MySQL database size
.. slug: MySQLDatabaseSize
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->





##How do I find out how large my MySQL database is?


To find out how much space the current database is using, start a MySQL console on the database in question, then run this:

    :::sql
    SELECT table_schema "Database Name"
         , SUM(data_length + index_length) / (1024 * 1024) "Database Size in MB"
    FROM information_schema.TABLES
    GROUP BY table_schema;
