<!--
.. title: Connecting to Microsoft SQL Server
.. slug: MSSQLServer
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


##Connecting to Microsoft SQL Server

If you have a paid PythonAnywhere plan, and you have a Microsoft SQL Server
database elsewhere on the Internet that you want to connect to (we don't host
SQL Server ourselves) then the best package to use is `pyodbc`.  It can be
a little fiddly to set up, though.

The aim is to create a ODBC *Data Source Name* (DSN) called `sqlserverdatasource`
that your pyodbc code will be able to use to connect to the database.  To do this:


1. Create a new file inside your home directory, called `odbcinst.ini`, and containing the following:

        [FreeTDS]
        Description = TDS driver (Sybase/MS SQL)
        Driver = /usr/lib/x86_64-linux-gnu/odbc/libtdsodbc.so
        Setup = /usr/lib/x86_64-linux-gnu/odbc/libtdsS.so
        CPTimeout =
        CPReuse =
        FileUsage = 1

2. create another file in your home directory called `.freetds.conf` (note the "." at the start), and in it put the following:

        [sqlserver]
            host = YOUR_SQL_SERVER_IP_ADDRESS
            port = YOUR_SQL_SERVER_PORT
            tds version = 7.0

    ...changing the `YOUR_SQL_SERVER_IP_ADDRESS` and `YOUR_SQL_SERVER_PORT` appropriately, of course.

3. Create yet another file in your home directory, called `odbc.ini`, and put this in it:

        [sqlserverdatasource]
        Driver = FreeTDS
        Description = ODBC connection via FreeTDS
        Trace = No
        Servername = sqlserver

4. Finally, when you want to connect to the database from your Python code:

        import os
        import pyodbc

        os.environ["ODBCSYSINI"] = "/home/YOUR_PYTHONANYWHERE_USERNAME"

        conn = pyodbc.connect('DSN=sqlserverdatasource;Uid=YOUR_SQL_SERVER_USERID;Pwd=YOUR_SQL_SERVER_PASSWORD;Encrypt=yes;Connection Timeout=30;')

    ...again, changing `YOUR_PYTHONANYWHERE_USERNAME`, `YOUR_SQL_SERVER_USERID`,
    and `YOUR_SQL_SERVER_PASSWORD` appropriately.

    **Note:** if you're using an Azure-hosted database, you need to specify both
    the username and the server name in `YOUR_SQL_SERVER_USERID`, separated by an `@`.  For example,
    `yourusername@yourservername`.  See [this help page](https://blogs.msdn.microsoft.com/cdndevs/2015/05/21/python-and-data-sql-database-on-azure-as-a-data-source-for-python-applications/)
    for more information.


Once you've done that, it should all work fine!

### If you have more than one SQL server database to connect to

If at a later stage you want to add more DSNs to be able to connect to other
SQL Server instances, you need to add a new block to both `.freetds.conf`
and to `odbc.ini`.

For `.freetds.conf`, just add something identical to the code above, but
change the `sqlserver` in
square brackets at the start to something different (say, `secondsqlserver`, or
perhaps something more descriptive), and, of course, change the `host` and `port`
parameters appropriately.  After that, `.freetds.conf` will look something like this:

    [sqlserver]
        host = YOUR_ORIGINAL_SQL_SERVER_IP_ADDRESS
        port = YOUR_ORIGINAL_SQL_SERVER_PORT
        tds version = 7.0

    [secondsqlserver]
        host = YOUR_NEW_SQL_SERVER_IP_ADDRESS
        port = YOUR_NEW_SQL_SERVER_PORT
        tds version = 7.0

For `odbc.ini`, again, add something identical to the code above, but
replace the `sqlserverdatasource` with `secondsqlserverdatasource` or something
more descriptive, and then change the `Servername` to the name you used in
`.freetds.conf`, eg. `secondsqlserver`.  So you'll wind up with something like this:

    [sqlserverdatasource]
    Driver = FreeTDS
    Description = ODBC connection via FreeTDS
    Trace = No
    Servername = sqlserver

    [secondsqlserverdatasource]
    Driver = FreeTDS
    Description = ODBC connection via FreeTDS
    Trace = No
    Servername = secondsqlserver

Once you've done that, you should be able to connect to your second SQL Server
database using the same `pyodbc.connect`, but changing the value assigned to the
DSN to the one you put in square brackes in `odbc.ini`.  For example:

    conn = pyodbc.connect('DSN=secondsqlserverdatasource;Uid=YOUR_SQL_SERVER_USERID;Pwd=YOUR_SQL_SERVER_PASSWORD;Encrypt=yes;Connection Timeout=30;')


### Static IPs

Some database-in-the-cloud providers expect you to set up a whitelist containing
all of the IP addresses that you expect to connect to your database from.  This
can be problematic because PythonAnywhere code can run on different machines
with different IP addresses.

[This page has some suggestions on what to do](/pages/StaticIPForExternalWhitelists)



