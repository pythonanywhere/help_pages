
<!--
.. title: Accessing your MySQL database from outside PythonAnywhere
.. slug: AccessingMySQLFromOutsidePythonAnywhere
.. date: 2017-05-12 19:09 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

> Warning -- this will only work in paid accounts

If you have a paid PythonAnywhere account, you can access your MySQL database
from outside PythonAnywhere using one of several techniques, depending on what
you want to do.

### MySQL Workbench


If you're running MySQL Workbench, you can configure it to connect using SSH directly with settings like this:

| Setting  | Value |
|--|--|
| SSH Hostname:  | ssh.pythonanywhere.com |
| SSH Username:  | **your PythonAnywhere username** |
| SSH Password:  | **the password you use to log in to the PythonAnywhere website** |
| SSH Key file:  | **should not be necessary when you specify the password** |
| MySQL Hostname:  | **your PythonAnywhere database hostname, eg. yourusername.mysql.pythonanywhere-services.com** |
| MySQL Server Port:  | 3306 |
| Username:  | **your PythonAnywhere username** |
| Password:  | **your PythonAnywhere database password** |
| Default Schema:  | **your database name, eg yourusername$mydatabase** |

* You may also need to allow ssh login based management as one of the mysql workbench options under *server connections -> remote management*.

* It's also a good idea to set the *Edit -> Preferences -> SQL Editor -> DBMS_Connection keep alive interval* setting to 200, to avoid any "lost connection" issues due to our 5-minute connection timeout.


### From Python code

If you're running Python code on your local machine, and you want it to access
your MySQL database, you can install [the `sshtunnel` package](https://pypi.python.org/pypi/sshtunnel)
and then use code like this:

    import mysql.connector
    import sshtunnel

    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='your PythonAnywhere username', ssh_password='the password you use to log in to the PythonAnywhere website',
        remote_bind_address=('your PythonAnywhere database hostname, eg. yourusername.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = mysql.connector.connect(
            user='your PythonAnywhere username', password='your PythonAnywhere database password',
            host='127.0.0.1', port=tunnel.local_bind_port,
            database='your database name, eg yourusername$mydatabase',
        )
        # Do stuff
        connection.close()

This example uses the `mysql-connector` library, but you can use any MySQL
library you like.

If you have trouble with the SSH Tunnel connection, the project provides a
helpful [troubleshooting guide](https://github.com/pahaz/sshtunnel/blob/master/Troubleshoot.rst)


### Klipfolio

Klipfolio is an online business dashboard tool; you can connect it to your
PythonAnywhere MySQL server by setting up a datasource and using an SSH tunnel.
The settings are:

| Host:  | **your PythonAnywhere database hostname, eg. yourusername.mysql.pythonanywhere-services.com** |
| Port:  | 3306 |
| Database:  | **your database name, eg yourusername$mydatabase** |
| Driver:  | MySQL |
| Username:  | **your PythonAnywhere database username** |
| Password:  | **your PythonAnywhere database password** |

Then click the arrow next to the "Use an SSH tunnel" option -- this will reveal
new Host, Port, Username and Password inputs:

| Host:  | ssh.pythonanywhere.com |
| Port:  | 22 |
| Username:  | **your PythonAnywhere username** |
| Password:  | **the password you use to log in to the PythonAnywhere website** |


### Manual SSH tunnelling

For other tools, you can set up a tunnel that pretends to be a MySQL server
running on your machine but actually sends data over SSH to your PythonAnywhere
MySQL instance.  If you're using a Mac or Linux, you probably already have the
right tools installed.

As long as you're not running a MySQL instance locally, just invoke SSH locally
(that is, on your own machine -- not on PythonAnywhere) like this (replacing
**username** with your PythonAnywhere username):

    :::bash
    ssh -L 3306:username.mysql.pythonanywhere-services.com:3306 username@ssh.pythonanywhere.com


That -L option means "forward LOCAL port 3306 to REMOTE host
`username.mysql.pythonanywhere-services.com` port 3306" (the port numbers can
be different, but in this case the standard MySQL port would be easiest). You
can also use -R to cause remote connections to be forwarded back to you, but
that's a pretty unusual thing to do for most people.

**REMEMBER** that you need to keep your this process open at all times while
you're accessing your PythonAnywhere MySQL server from your local machine! As
soon as that closes, your forwarded connection is also lost.

At this point, you should be able to run code that connects to MySQL as normal.
One thing to watch out
for, however -- many MySQL clients treat the hostname localhost as special,
meaning "connect to the local server over a domain socket". What you want to do
is force it to connect to your local machine on port 3306, and you can do this
by specifying 127.0.0.1 for the host instead of localhost. For example, to use
the command-line mysql client you'd invoke it like this:

    :::bash
    mysql -h 127.0.0.1 -u username -p

Finally, if you are running a MySQL server locally and hence port 3306 is already
in use, you can modify your SSH invocation to use any other port:

    :::bash
    ssh -L 3333:username.mysql.pythonanywhere-services.com:3306 username@ssh.pythonanywhere.com


However, you'd then need to configure your MySQL client to use this other port,
as this is not the default for MySQL.  For example:

    :::bash
    mysql -h 127.0.0.1 --port 3333 -u username -p

You can also use this technique to give Python code access to the database
instead of using the the `sshtunnel` technique.


*Many thanks to user Cartroo for the first version of this guide!*
