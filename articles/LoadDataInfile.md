<!--
.. title: LoadDataInfile
.. slug: LoadDataInfile
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

When trying to get data into MySQL using `LOAD DATA INFILE`, you may see an
error a little like this:

    Error Code: 1045 Access denied for user 'myusername'@'%' (using password: YES)

There are two things you need to do to make this work:

### Use the command-line flag to enable loading client data

The newer versions of MySQL client block load data by default. You need to pass
it in as a command line switch. If you open up a Bash console you can connect to
the database manually like so:

    :::bash
    mysql -h myusername.mysql.pythonanywhere-services.com -u myusername 'myusername$default' -p --local-infile=1

"--local-infile=1" enables the load data command.  You will be prompted for your
password.


### Use `LOCAL` in the MySQL command

The MySQL command `LOAD DATA INFILE "foo.csv"` tries to load the contents of
the file `foo.csv` on the computer where the database is running.  On
PythonAnywhere, the MySQL server is on a different computer to the one where
your code runs, so your files aren't available.  Instead, you need to tell the
database to load the file from the computer where the MySQL *client* is running,
by adding the extra keyword `LOCAL`:

    LOAD DATA LOCAL INFILE "foo.csv"

