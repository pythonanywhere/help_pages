
<!--
.. title: Accessing your PostgreSQL database from outside PythonAnywhere
.. slug: AccessingPostgresFromOutsidePythonAnywhere
.. date: 2017-05-12 19:09 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

> Warning -- this will only work in paid accounts

PostgreSQL databases on PythonAnywhere are protected by a firewall, so external
computers can't access them.

However, if you have a paid account, you can access your database
from outside using a technique called an SSH tunnel, which essentially makes
a secure SSH connection to our systems, then sends the Postgres stuff over it.

There are a number of ways to do this:


## pgAdmin

If you're running pgadmin, you can use SSH in a local terminal to create an SSH
tunnel from your machine to PythonAnywhere and then connect to the local port
using pgAdmin.

First, we create the SSH tunnel:

    :::bash
    ssh -4 -L 9999:postgres-server-hostname:postgres-server-port username@ssh.pythonanywhere.com
    
where you should:

| replace                  | with                                                                                                  |
|--|--|
| postgres-server-hostname | **your PythonAnywhere database hostname, eg. yourusername-1234.postgres.pythonanywhere-services.com** |
| postgres-server-port     | **the port from the Postgres tab of the "Databases" page inside PythonAnywhere**                      |
| username                 | **your PythonAnywhere username**                                                                      |

----

When this has worked, it will appear that you have SSHed into your
PythonAnywhere account. As long as that SSH session is active, your SSH tunnel
will be in-place. The local side of your SSH tunnel will be at port 9999. 

If that doesn't work because you get an error like:

    :::text
    cannot listen to port: 9999
    
You can try any other port number greater than 1024 and less than 65536. Be
sure to use the correct port in the next step.

Now open the ["Server" dialog](https://www.pgadmin.org/docs/pgadmin4/4.14/server_dialog.html) in pgAdmin,
and give the connection a name on the "General" tab, then set up the stuff on the
"Connection" tab:


| Setting            | Value                                                           |
|--------------------|-----------------------------------------------------------------|
| Host name/address: | localhost                                                       |
| Port:              | 9999                                                            |
| Username:          | **any user you have set up on your Postgres server, eg. super** |
| Password:          | **the password corresponding to that user**                     |

----
Then you should be able to connect from pgAdmin to your PythonAnywhere Postgres
database.

## TablePlus

If you're using TablePlus, you can use the settings from this diagram provided by
devwon (Hyerin Won):

<img alt="TablePlus Postgres connection setup" src="/postgres-tableplus.png" style="border: 2px solid lightblue; max-width: 70%;">


## From Python code

If you're running Python code on your local machine, and you want it to access
your Postgres database, you can install [the `sshtunnel` package](https://pypi.python.org/pypi/sshtunnel)
and then use code like this:

    import psycopg2
    import sshtunnel

    sshtunnel.SSH_TIMEOUT = 5.0
    sshtunnel.TUNNEL_TIMEOUT = 5.0

    with sshtunnel.SSHTunnelForwarder(
        ('ssh.pythonanywhere.com'),
        ssh_username='your PythonAnywhere username', ssh_password='the password you use to log in to the PythonAnywhere website',
        remote_bind_address=('your PythonAnywhere database hostname, eg. yourusername-1234.postgres.pythonanywhere-services.com', the port on the databases page)
    ) as tunnel:
        connection = psycopg2.connect(
            user='a postgres user', password='password for the postgres user',
            host='127.0.0.1', port=tunnel.local_bind_port,
            database='your database name',
        )
        # Do stuff
        connection.close()

This example uses the `psycopg2` library, but you can use any Postgres
library you like.

If you have trouble with the SSH Tunnel connection, the project provides a
helpful [troubleshooting guide](https://github.com/pahaz/sshtunnel/blob/master/Troubleshoot.rst)


## Manual SSH tunnelling

For other tools that you want to run on your own machine, you can set up a tunnel that pretends to be a Postgres server
running on your machine but actually sends data over SSH to your PythonAnywhere
Postgres instance.  If you're using a Mac or Linux, you probably already have the
right tool installed -- the `ssh` command.  If you're using Windows, see the "Using PuTTY on Windows"
section below.

### Using SSH (Linux/Mac)

As long as you're not running a Postgres instance locally, just invoke SSH locally
(that is, on your own machine -- not on PythonAnywhere) like this, replacing
**username** with your PythonAnywhere username, **10123** with the port number
on the "Postgres" tab of the "Databases" page, and changing the hostname from
`yourusername-1234.postgres.pythonanywhere-services.com` to the one on the "Databases" page
likewise:

    :::bash
    ssh -L 5432:yourusername-1234.postgres.pythonanywhere-services.com:10123 username@ssh.pythonanywhere.com

That -L option means "forward LOCAL port 5432 to REMOTE host
`yourusername-1234.postgres.pythonanywhere-services.com` port 10123".

If you are running a Postgres instance locally, then it will probably already be using
local port 5432, which means that the `ssh` command won't be able to.  You can modify your SSH invocation
to use any other port -- this one would use the local post 3333.

    :::bash
    ssh -L 3333:yourusername-1234.postgres.pythonanywhere-services.com:10123 username@ssh.pythonanywhere.com

**REMEMBER** You need to keep your this `ssh` process open at all times while
you're accessing your PythonAnywhere Postgres server from your local machine! As
soon as that closes, your forwarded connection is also lost.

After all of that, you'll have a server running on your computer (hostname
127.0.0.1, port 5432 -- or 3333 or something else if you have Postgres running locally),
which will forward everything on to the Postgres server on PythonAnywhere.

Now skip down to the "Using the tunnel" section below.

### Using PuTTY on Windows

The `ssh` command is not normally installed on Windows, but you can use a tool
called PuTTY instead:

Download and install PuTTY from [here](https://www.putty.org).  Once you've done that:

* Start PuTTY and enter ssh.pythonanywhere.com into the "Host name" field
* In the "Category" tree on the left, open Connection -> SSH -> Tunnels
* If you don't have a Postgres database running on your local machine, enter "Source port" 5432.  If you
  do have one running, use some other port, for example 3333.
* Set "Destination" to *the hostname from the databases page*:`*your-postgres-port*,
* Click the "Open" button, and enter the username and password you would use to log in to the PythonAnywhere website.
* Once it's connected, leave PuTTY running -- it will manage the SSH tunnel.

After all of that, you'll have a server running on your computer (hostname
127.0.0.1, port 5432 -- or 3333 or something else if you have Postgres running locally),
which will forward everything on to the Postgres server on PythonAnywhere.


### Using the tunnel

At this point, you should be able to run code that connects to Postgres using this local server.
For example, you could use the code that is inside the `with` statement in the
"From Python code" section above, replacing `tunnel.local_bind_port` with the
port you specified in either SSH or PuTTY -- 5432, or 3333 or something else if you have Postgres running locally.

