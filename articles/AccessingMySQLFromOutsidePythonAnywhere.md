
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

MySQL databases on PythonAnywhere are protected by a firewall, so external
computers can't access them.

However, if you have a paid account, you can access your MySQL database
from outside using a technique called an SSH tunnel, which essentially makes
a secure SSH connection to our systems, then sends the MySQL stuff over it.

There are a number of ways to do this:


## MySQL Workbench

If you're running MySQL Workbench, you can configure it to connect use a tunnel with settings like this:

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


## From Python code

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


## Klipfolio

Klipfolio is an online business dashboard tool; you can connect it to your
PythonAnywhere MySQL server by setting up a datasource and telling it to use an SSH tunnel.
The settings are:

| Setting  | Value |
|--|--|
| Host:  | **your PythonAnywhere database hostname, eg. yourusername.mysql.pythonanywhere-services.com** |
| Port:  | 3306 |
| Database:  | **your database name, eg yourusername$mydatabase** |
| Driver:  | MySQL |
| Username:  | **your PythonAnywhere database username** |
| Password:  | **your PythonAnywhere database password** |

Then click the arrow next to the "Use an SSH tunnel" option -- this will reveal
new Host, Port, Username and Password inputs:

| Setting  | Value |
|--|--|
| Host:  | ssh.pythonanywhere.com |
| Port:  | 22 |
| Username:  | **your PythonAnywhere username** |
| Password:  | **the password you use to log in to the PythonAnywhere website** |


## Manual SSH tunnelling

For other tools that you want to run on your own machine, you can set up a tunnel that pretends to be a MySQL server
running on your machine but actually sends data over SSH to your PythonAnywhere
MySQL instance.  If you're using a Mac or Linux, you probably already have the
right tool installed -- the `ssh` command.  If you're using Windows, see the "Using PuTTY on Windows"
section below.

### Using SSH (Linux/Mac)

As long as you're not running a MySQL instance locally, just invoke SSH locally
(that is, on your own machine -- not on PythonAnywhere) like this, replacing
**username** with your PythonAnywhere username:

    :::bash
    ssh -L 3306:username.mysql.pythonanywhere-services.com:3306 username@ssh.pythonanywhere.com

That -L option means "forward LOCAL port 3306 to REMOTE host
`username.mysql.pythonanywhere-services.com` port 3306".

If you are running a MySQL instance locally, then it will probably already be using
local port 3306, which means that the `ssh` command won't be able to.  You can modify your SSH invocation
to use any other port -- this one would use the local post 3333.

    :::bash
    ssh -L 3333:username.mysql.pythonanywhere-services.com:3306 username@ssh.pythonanywhere.com

**REMEMBER** You need to keep your this `ssh` process open at all times while
you're accessing your PythonAnywhere MySQL server from your local machine! As
soon as that closes, your forwarded connection is also lost.

After all of that, you'll have a server running on your computer (hostname
127.0.0.1, port 3306 -- or 3333 or something else if you have MySQL running locally),
which will forward everything on to the MySQL server on PythonAnywhere.

Now skip down to the "Using the tunnel" section below.

### Using PuTTY on Windows

The `ssh` command is not normally installed on Windows, but you can use a tool
called PuTTY instead:

Download and install PuTTY from [here](https://www.putty.org).  Once you've done that:

* Start PuTTY and enter ssh.pythonanywhere.com into the "Host name" field
* In the "Category" tree on the left, open Connection -> SSH -> Tunnels
* If you don't have a MySQL database running on your local machine, enter "Source port" 3306.  If you
  do have one running, use some other port, for example 3333.
* Set "Destination" to *yourusername*`.mysql.pythonanywhere-services.com:3306`.
* Click the "Open" button, and enter the username and password you would use to log in to the PythonAnywhere website.
* Once it's connected, leave PuTTY running -- it will manage the SSH tunnel.

After all of that, you'll have a server running on your computer (hostname
127.0.0.1, port 3306 -- or 3333 or something else if you have MySQL running locally),
which will forward everything on to the MySQL server on PythonAnywhere.


### Using the tunnel

At this point, you should be able to run code that connects to MySQL using this local server.
For example, you could use the code that is inside the `with` statement in the
"From Python code" section above.

One thing to watch out for, however -- some MySQL clients treat the hostname `localhost` as special,
meaning "connect to the local server over a domain socket".  What you want to do
is force it to connect to your local machine on port 3306, and you can do this
by specifying 127.0.0.1 for the host instead of localhost. For example, to use
the command-line mysql client you'd invoke it like this:

    :::bash
    mysql -h 127.0.0.1 -u username -p

Or, if you had to use port 3333 because you had a local MySQL server:

    :::bash
    mysql -h 127.0.0.1 --port 3333 -u username -p


*Many thanks to user Cartroo for the first version of this guide!*
