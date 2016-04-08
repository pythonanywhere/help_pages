
<!--
.. title: SSH tunnelling
.. slug: SSHTunnelling
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->





##How to use a local MySQL GUI with PythonAnywhere


**This requires a paid account for the SSH access**

There are two ways to do this.


###MySQL Workbench


If you're running MySQL Workbench, you can configure it to connect using SSH directly with settings like this:

| Setting  | Value |
|--|--|
| SSH Hostname:  | ssh.pythonanywhere.com |
| SSH Username:  | **your PythonAnywhere username** |
| SSH Password:  | **the password you use to log in to the PythonAnywhere website** |
| SSH Key file:  | **should not be necessary when you specify the password** |
| MySQL Hostname:  | **your PythonAnywhere database name, eg. yourusername.mysql.pythonanywhere-services.com** |
| MySQL Server Port:  | 3306 |
| Username:  | **your PythonAnywhere username** |
| Password:  | **your PythonAnywhere database password** |
| Default Schema:  | **your database name** |


###Manual SSH tunneling


For other tools, you can set up a tunnel that pretends to be a MySQL server running on your machine but actually sends data over SSH to your PythonAnywhere MySQL instance.

As long as you're not running a MySQL instance locally, just invoke SSH locally (that is, on your own machine -- not on PythonAnywhere) like this (replacing **username** with your PythonAnywhere username):

    :::bash
    ssh -L 3306:username.mysql.pythonanywhere-services.com:3306 username@ssh.pythonanywhere.com


That -L option means "forward LOCAL port 3306 to REMOTE host username.mysql.pythonanywhere-services.com port 3306" (the port numbers can be different, but in this case the standard MySQL port would be easiest). You can also use -R to cause remote connections to be forwarded back to you, but that's a pretty unusual thing to do for most people.

**REMEMBER** that you need to keep your this process open at all times while you're accessing your PythonAnywhere MySQL server from your local machine! As soon as that closes, your forwarded connection is also lost.

At this point, you should be able to run MySQL as normal. One thing to watch out for, however - many MySQL clients treat the hostname localhost as special, meaning "connect to the local server over a domain socket". What you want to do is force it to connect to your local machine on port 3306, and you can do this by specifying 127.0.0.1 for the host instead of localhost. For example, to use the command-line mysql client you'd invoke it like this:

    :::bash
    mysql -h 127.0.0.1 -u username -p


Finally, if you are running a MySQL server locally and hence port 3306 is already in use, you can modify your SSH invocation to use any other port:

    :::bash
    ssh -L 3333:username.mysql.pythonanywhere-services.com:3306 username@ssh.pythonanywhere.com


However, you'd then need to configure your MySQL client to use this other port, as this is not the default for MySQL.

Thanks to Cartroo for this great guide
