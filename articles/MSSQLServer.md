
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
SQL Server ourselves) then you have two options in terms of Python packages
to use.

### pymssql

This is the easiest option.  Just connect to it like this:

    host = "123.456.789.012"
    username = "yourusername"
    password = "yourpassword"
    database = "yourdatabasename"

    conn = pymssql.connect(host, username, password, database)
    cursor = conn.cursor()

...changing the `host`, `username`, `password` and `database` variables
appropriately, of course.


### pyodbc

This is much trickier to set up, so if you can use `pymssql` then we definitely
recommend that option.   But if you have a bunch of scripts that already use
`pyodbc` and need them to work on PythonAnywhere, it is possible.

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
