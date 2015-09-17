
<!--
.. title: External VCS
.. slug: ExternalVCS
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->





##Using external version control systems with PythonAnywhere


Rather than uploading and downloading files manually, you might prefer to pull in a whole repository of source code from somewhere like [GitHub](//www.github.com/) or [BitBucket](//www.bitbucket.org/).

Bash consoles — create them from the [Consoles page](https://www.pythonanywhere.com/consoles/) — include popular source control clients: `git`, `hg` and `svn`.

If you're pulling in from a private git repo on [GitHub](//www.github.com/), you may need to setup a new ssh key, and copy &amp; paste it into your [GitHub](//www.github.com/) account's authorised keys.

    ssh-keygen
    cat ~/.ssh/id_rsa.pub


Check out the [GitHub help pages](//help.github.com/linux-set-up-git/#_set_up_ssh_keys) for more info.


##Free account restrictions


Be aware that free users are restricted to a [whitelist](https://www.pythonanywhere.com/whitelist/) of sites, and to the HTTP/HTTPS protocol. We also allow the pure-git protocol certain popular services like github and bitbucket.

So you should be able to use bitbucket or github as normal. If you're storing your git or hg repository on your own server, then you'll need to use https in your repo URLs instead of the `git@` syntax...
