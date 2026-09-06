
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


## How do I find out how large my MySQL database is?

To find out how much space the current database is using, start a MySQL
console on the database in question, then run this:

    :::sql
    SELECT table_schema "Database Name"
         , SUM(data_length + index_length) / (1024 * 1024) "Database Size in MB"
    FROM information_schema.TABLES
    GROUP BY table_schema;


## How to delete a database I don't need any more?

Start a MySQL console and run the following command:

    :::sql
    drop database `<your_username>$<your_database_name>`;

replacing placeholders in brackets respectively with your `username` and the
`database name` that should be deleted.  See ["Using MySQL"](/pages/UsingMySQL/#deleting-existing-database) 
help page or more details.


## How to optimise disk space?

We use MySQL innodb tables with the file_per_table setting set to true - this has many advantages, but it does mean that tables that have lots of random row deletions can end up taking way more space on disk than the space than they actually need.

### Step 1 - Discover the tables with the most "free" space

    :::sql
    SELECT concat(table_schema, ".", table_name) as table_name, 
       (data_length+index_length)/1024/1024 AS total_mb, 
       data_length/1024/1024 AS data_mb, 
       index_length/1024/1024 AS index_mb, 
       data_free/1024/1024 as free_mb 
    FROM information_schema.tables 
    WHERE table_schema LIKE '%$%' 
    ORDER BY free_mb DESC 
    LIMIT 10;

This will show the top 10 tables with the amount of space "free" this is the space that is present in the files that comprise the tables. Tables with a high free_mb (> ~ 1G) may be candidates for optimization. Here's example output showing that Big$Table.my_cache_table has ~1.4G free that could be recovered.

    :::bash
    +-------------------------------+--------------+--------------+--------------+--------+---------------+
    | table_name                    | total_mb     | data_mb      | index_mb     | tables | free_mb       |
    +-------------------------------+--------------+--------------+--------------+--------+---------------+
    | Big$Table.my_cache_table      |  16.09375000 |  16.01562500 |   0.07812500 |      1 | 1480.00000000 |
    | table1$project.api_wordinbook | 369.71875000 |  77.09375000 | 292.62500000 |      1 |  164.00000000 |
    | lk$mls.properties             | 473.34375000 | 473.34375000 |   0.00000000 |      1 |  148.00000000 |
    | lu$site.db_item               |   2.01562500 |   2.01562500 |   0.00000000 |      1 |  137.00000000 |
    | Smart$panel.Data_twittos      |   0.01562500 |   0.01562500 |   0.00000000 |      1 |  135.00000000 |
    | So$pr.help                    | 255.81250000 | 255.81250000 |   0.00000000 |      1 |   70.00000000 |
    | ao$billing.silk_sqlquery      |  55.12500000 |  53.07812500 |   2.04687500 |      1 |   61.00000000 |
    | i$info.Pe                     |  48.57812500 |  48.57812500 |   0.00000000 |      1 |   52.00000000 |
    | Smart$panel.Data_activites    |   1.01562500 |   1.01562500 |   0.00000000 |      1 |   48.00000000 |
    | Smart$panel.Data_activites_2  |   1.01562500 |   1.01562500 |   0.00000000 |      1 |   48.00000000 |
    +-------------------------------+--------------+--------------+--------------+--------+---------------+

### Step 2 - Optimise Tables

If there are tables in the above query that are candidates for optimization, you can run

    :::sql
    optimize table <table_name>;

> [!WARNING]: Because this involves copying the table, there needs to be enough space still available on the server for 2 copies of the table

Because we use innodb tables, this is performed by an ALTER TABLE of the table, but it happens in such a way that the exclusive lock is only taken briefly. See The MySQL docs for more details.

Both of these queries can take a really long time to run. The time the second one takes predictably seems to be related to the size of the database (total_mb).