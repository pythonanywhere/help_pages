
<!--
.. title: SSH Access
.. slug: SSHAccess
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



If you have a paid-for PythonAnywhere account, you can access it via ssh.
Here's how:

From a command line with ssh installed

    ssh <username>@ssh.pythonanywhere.com


The server's fingerprint is:

    d5:50:bd:8e:23:eb:14:3f:cf:15:87:42:0b:bf:e2:60


NB: &lt;username&gt; is your PythonAnywhere username -- not your email address.
It's also case-sensitive, so if your username is "MyUsername", then you have to
use that -- "myusername" won't work.

The password is the same password you use to login to the web site.

You can use public / private keys to login via ssh. Please add your public keys
to `~/.ssh/authorized_keys` in order to enable passwordless logins.


### Debugging

Sometimes, for some reason, you may not be able to login using SSH. The
starting point to working out what is going wrong is to run:

    ssh -v <username>@ssh.pythonanywhere.com


###Filezilla etc


You can also use SSH access to get files into your account using Filezilla and
other similar upload tools. [Details here](/pages/FTP)
