
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



If you have a paid-for PythonAnywhere account, you can access it via SSH.
The SSH server for your account depends on which one of our sites you signed up
to:

* If you're using our global, US-hosted site at `www.pythonanywhere.com`, then the
  SSH server's hostname is `ssh.pythonanywhere.com`
* If you're using our EU-hosted site at `eu.pythonanywhere.com`, then the
  SSH server's hostname is `ssh.eu.pythonanywhere.com`

Here's how to use that:

From a command line with the `ssh` command installed

    ssh <username>@<ssh server hostname>

The server's fingerprint is:

    MD5:d5:50:bd:8e:23:eb:14:3f:cf:15:87:42:0b:bf:e2:60
    SHA256:zy2jmqxNg/fs6tFZK55OjHTI3B2UofzOiUvTPtcX3/Y

NB: &lt;username&gt; is your PythonAnywhere username -- not your email address.
It's also case-sensitive, so if your username is "MyUsername", then you have to
use that -- "myusername" won't work.

The password is the same password you use to login to the web site.

### Passwordless logins

You can also use public/private keys to enable passwordless logins via SSH.

Just add your public keys to the file `~/.ssh/authorized_keys` -- it's a plain-text
file with one key per line.

If you don't have a public/private key pair yet, you can generate one by running the following command on your system:

    $ ssh-keygen -t rsa -b 2048
    Generating public/private rsa key pair.
    Enter file in which to save the key (/home/username/.ssh/id_rsa): 
    Enter passphrase (empty for no passphrase): 
    Enter same passphrase again: 
    Your identification has been saved in /home/username/.ssh/id_rsa.
    Your public key has been saved in /home/username/.ssh/id_rsa.pub.

Running the following command copies the generated keys to the pythonanywhere server:

    $ ssh-copy-id <username>@<ssh server hostname>
    <username>@<ssh server hostname>'s password: 

The next time you use `ssh <username>@<ssh server hostname>`, your password will not be prompted! 


### Debugging

Sometimes, for some reason, you may not be able to login using SSH. The
starting point to working out what is going wrong is to run:

    ssh -v <username>@<ssh server hostname>

If the SSH port appears closed to you, this is likely that you failed to
authenticate several times, and your IP has been banned for a little while.
This mechanism is necessary to protect the SSH service from hackers hammering
the service. So, check your credentials, check the IP address again, and
try again a little later (something like an hour later).

### Filezilla, etc

You can also use SSH access to get files into your account using Filezilla and
other similar upload tools. [Details here](/pages/UploadingAndDownloadingFiles).
