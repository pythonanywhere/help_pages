
<!--
.. title: Using NVM to get the most updated version of node
.. slug: Node
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

NVM allows you to install and run different versions of node (and to manage and
install their "global packages" separately).  Using it, you can run versions of
Node up to 10.16.0 on PythonAnywhere.  Later versions are, unfortunately not
compatible with the way our system works.

First download the git repo

    git clone https://github.com/creationix/nvm.git

Now hook up your shell to use nvm

    source ~/nvm/nvm.sh

To automatically run this every time you start a bash shell, add it to your *bashrc*:

    echo 'source ~/nvm/nvm.sh' >> ~/.bashrc

You can now do a `nvm ls-remote` to see what versions of node are available, and then install them.  Here's how you'd install v6.11.4 for example:

    nvm ls-remote
    #...
    nvm install v6.11.4

You can run `nvm use v6.11.4` to use the new node. To set that as default, set up an nvm alias:

    nvm alias default v6.11.4

This will also solve any permission problems involved with installing with `npm
install --global` will work without needing to specify a prefix.
