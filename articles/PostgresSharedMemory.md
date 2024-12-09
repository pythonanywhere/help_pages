
<!--
.. title: Postgres Shared Memory Error
.. slug: Postgres Shared Memory
.. date: 2024-12-09 11:46:28 UTC
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

# Postgres Shared Memory Error

If you are getting an error similar to the following when you are running a
query against your Postgres database:

```
psycopg2.errors.DiskFull: could not resize shared memory segment "/PostgreSQL.230765310" to 8388608 bytes: No space left on device
```

The error is not related to the amount of disk space you have available for
your Postgres instance. This error is related to shared memory available to
your Postgres database. Some postgres queries create temporary tables or files
and those tables or files are stored in shared memory. If the queries you are
running create temporary tables or files that are too big to be help in shared
memory, then you get that error.

Postgres creates hash tables when joining tables and there are no indexes on
the join colums. These hash tables are stored in shared memory and, if you are
joining a large number of records, then the hash tables may be too large for
the shared memory. You can use `EXPLAIN` on a query to see if there are
references to hash iun the output and, if there are, it may help to add indexes
to the columns that are joined on the table.

You can also reduce the shared memoey use of a joining query by limiting the
numbher of records that you are likely to join with additional filters in the
`WHERE` clause of your query.



