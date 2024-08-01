
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

There are a number of ways to do this.  The first thing you need to know is
the SSH hostname for your account:

* If your account is on our global, US-based system at `www.pythonanywhere.com`, then the SSH hostname is `ssh.pythonanywhere.com`
* If your account is on our EU-based system at `eu.pythonanywhere.com`, then the SSH hostname is `ssh.eu.pythonanywhere.com`

Note the difference in hostnames for both SSH and MySQL:

| Hostname  | SSH | MySQL |
|--|--|--|
| Global-US | `ssh.pythonanywhere.com` | *username*`.mysql.pythonanywhere-services.com` |
| EU | `ssh.eu.pythonanywhere.com` | *username*`.mysql.eu.pythonanywhere-services.com` |

Armed with that, you can do one of the following:


## MySQL Workbench

If you're running MySQL Workbench, you can configure it with settings like this using "Standard TCP/IP over SSH":

| Setting  | Value |
|--|--|
| SSH Hostname:  | **your SSH hostname** |
| SSH Username:  | **your PythonAnywhere username** |
| SSH Password:  | **the password you use to log in to the PythonAnywhere website** |
| SSH Key file:  | **should not be necessary when you specify the password** |
| MySQL Hostname:  | **your PythonAnywhere database hostname, eg. yourusername.mysql.pythonanywhere-services.com** |
| MySQL Server Port:  | 3306 |
| Username:  | **your PythonAnywhere database username** |
| Password:  | **your PythonAnywhere database password** |
| Default Schema:  | **your database name, eg yourusername$mydatabase** |

<img alt="MySQL Workspace connection dialog" src="/MySQL_workspace_login.png" class="bordered-image">

* You may also need to allow ssh login based management as one of the mysql workbench options under *server connections -> remote management*.

* It's also a good idea to set the *Edit -> Preferences -> SQL Editor -> DBMS_Connection keep alive interval* setting to
  200, to avoid any "lost connection" issues due to our 5-minute connection timeout.

* If you're running really long-running commands (for example, dumps of large tables) and you get client-side timeouts,
  you can also set *Edit → Preferences → SQL Editor → DBMS connection read time out (in seconds)*, which has a default of
  600, to something larger, like 6000.


## DBeaver
If you're running DBeaver, you can configure it with the following settings:

* Check "Use SSH tunnel" in *Connect to new database -> Mysql -> SSH tab*

| Setting              | Value                                                                                         |
|----------------------|-----------------------------------------------------------------------------------------------|
| Host/IP:             | **your SSH hostname (ssh.eu.pythonanywhere.com or ssh.pythonanywhere.com)**                   |
| User Name:           | **your PythonAnywhere username**                                                              |
| Password:            | **the password you use to log in to the PythonAnywhere website**                              |
| Local port:          | **3306 if you are not running a local database, else a random number you pick**               |
| Remote port:         | **3306**                                                                                      |
| Keep-Alive interval: | **0**  */otherwise connection will fail/*                                                 |
| MySQL Hostname:      | **your PythonAnywhere database hostname, eg. yourusername.mysql.pythonanywhere-services.com** |
| MySQL Server Port:   | 3306                                                                                      |


* Test tunnel configuration... (should be successfull)
* Go to the *Main tab*

| Setting      | Value                                                                                                                                    |
|--------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Server Host: | **your PythonAnywhere db hostname (username.mysql.eu.pythonanywhere-services.com or username.mysql.pythonanywhere-services.com)**        |
| Port:        | **3306**                                                                                                                                 |
| Username:    | **your PythonAnywhere database username**                                                                                                         |
| Password:    | **your PythonAnywhere database password**


* Test Connection... (should be successfull)
* Click "OK"


## From Python code

If you're running Python code on your local machine, and you want it to access
your MySQL database, you can install [the `sshtunnel` package](https://pypi.python.org/pypi/sshtunnel)
and then use code like this:

    import MySQLdb
    import sshtunnel

    sshtunnel.SSH_TIMEOUT = 10.0
    sshtunnel.TUNNEL_TIMEOUT = 10.0

    with sshtunnel.SSHTunnelForwarder(
        ('your SSH hostname'),
        ssh_username='your PythonAnywhere username', ssh_password='the password you use to log in to the PythonAnywhere website',
        remote_bind_address=('your PythonAnywhere database hostname, eg. yourusername.mysql.pythonanywhere-services.com', 3306)
    ) as tunnel:
        connection = MySQLdb.connect(
            user='your PythonAnywhere database username',
            passwd='your PythonAnywhere database password',
            host='127.0.0.1', port=tunnel.local_bind_port,
            db='your database name, eg yourusername$mydatabase',
        )
        # Do stuff
        connection.close()

This example uses [the mysqlclient library](https://mysqlclient.readthedocs.io/index.html), which
you can install on your machine with

```
pip install mysqlclient
```

...but you can use any MySQL library you like.

If you have trouble with the SSH Tunnel connection, the project provides a
helpful [troubleshooting guide](https://github.com/pahaz/sshtunnel/blob/master/Troubleshoot.rst)

If you're getting intermittent connection errors, try increasing one or both of
the timeouts that are set on `sshtunnel`.


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
| Host:  | **your SSH hostname** |
| Port:  | 22 |
| Username:  | **your PythonAnywhere username** |
| Password:  | **the password you use to log in to the PythonAnywhere website** |


## JetBrains PyCharm

You can set up the SSH tunnelling from the SSH/SSL tab of the PyCharm connection
setup dialog:

<img alt="PyCharm SSH tunnelling dialog" src="/pycharm-ssh-tunnel-dialog.png" class="bordered-image">

* The "proxy host" should be your SSH hostname (see the options for that at the top of this help page)
* The "proxy user" should be your PythonAnywhere username
* The "proxy password" should be the password you use to log in to our website (not your MySQL password)

You should also be aware that there is a problem in PyCharm where it does not
recognise database names with dollar signs in them (which all databases have
on PythonAnywhere.  They have [posted a workaround for that on their site](https://youtrack.jetbrains.com/issue/DBE-10067).


## Sequel-Pro

*Contributed by Baodong Liu*

I prefer Sequel-Pro, which is a very good looking and easy to use interface for
you to have the convenience of managing your database. The limitation is that
Sequel-Pro can only be installed on a Mac computer, not Windows.

### Initial installation

It is important to upgrade Sequel-Pro to 1.1.2, the most recent version.
After you install the 1.1.2 version, you will need to move the downloaded
software to your MacBook Applications. You can simply go to Finder to check the
Devices from there. You will find your downloaded Sequel-Pro. Just move it to
Applications in Finder. You will need to confirm this from the admin authority.
After you successfully move Sequel-Pro to Applications, you can launch it from
your Applications.

The first thing you need to do on Sequel-Pro is to configure local server and
import a database from your own computer directory. You will enter the following
information from the "Standard" option of connections.

| Setting  | Value |
|--|--|
| Host: | 127.0.0.1 |
| Username: | root |
| Password: | root |
| Port: | 8889 |

After entering the above information, you will be able to see that you are
running your SQL testing environment. Just select "Add Database" from the
"Choose Database" drop-down menu. You can then test it from there, and import a
local database to Sequel-Pro.

### Connecting to PythonAnywhere

Now, you are ready to connect your Sequel-Pro to your database that you have
previously set up on to Pythonanywhere.

To do this, you will need to use the SSH option, rather than the Standard one
you used earlier. You will then be asked to provide information on both MySQL
Host and SSH Host information. You will need to enter all the required boxes
correctly to have the access to your PythonAnywhere database. Here are the
details:

| Setting  | Value |
|--|--|
| Name: | (you can write whatever you want) |
| MySQL Host: | **your PythonAnywhere database hostname, eg. yourusername.mysql.pythonanywhere-services.com** |
| Username: | **your PythonAnywhere database username** |
| Password: | **your PythonAnywhere database password** |
| Database: | (optional, so you can leave it blank) |
| Port: | 3306 |
| SSH Host: | **your SSH hostname** |
| SSH User: | **your PythonAnywhere username** |
| SSH Password: | **the password you use to log in to the PythonAnywhere website** |
| SSH Port: | (optional, so you can leave it blank) |

After entering all the above information correctly, you will successfully be
connected to your database in Pythonanywhere. Your fun of managing your own
database starts right away.


## Manual SSH tunnelling

For other tools that you want to run on your own machine, you can set up a tunnel that pretends to be a MySQL server
running on your machine but actually sends data over SSH to your PythonAnywhere
MySQL instance.  If you're using a Mac or Linux, you probably already have the
right tool installed -- the `ssh` command.  If you're using Windows, see the "Using PuTTY on Windows"
section below.

### Using SSH (Linux/Mac)

As long as you're not running a MySQL instance locally, just invoke SSH locally
(that is, on your own machine -- not on PythonAnywhere) like this, replacing
**username** with your PythonAnywhere username and **yoursshhostname** with
your SSH hostname:

    :::bash
    ssh -L 3306:username.mysql.pythonanywhere-services.com:3306 username@yoursshhostname

That -L option means "forward LOCAL port 3306 to REMOTE host
`username.mysql.pythonanywhere-services.com` port 3306".

If you are running a MySQL instance locally, then it will probably already be using
local port 3306, which means that the `ssh` command won't be able to.  You can modify your SSH invocation
to use any other port -- this one would use the local post 3333.

    :::bash
    ssh -L 3333:username.mysql.pythonanywhere-services.com:3306 username@yoursshhostname

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

* Start PuTTY and enter your SSH hostname into the "Host name" field
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

## Debugging the SSH connection

If you're having issues with the SSH connection, start with checking if you typed your PythonAnywhere username correctly while creating the tunnel -- the username is **case-sensitive**, so if your username is "MyUsername", then you have to use that -- "myusername" won't work.

If you eliminate that, and still can't connect, this command is a good starting point for further debugging:

    :::bash
    ssh -v <username>@<ssh hostname>

For more details about SSH and PythonAnywhere check [this page](/pages/SSHAccess).

