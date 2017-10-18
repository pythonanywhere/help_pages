
<!--
.. title: Setting up Node projects
.. slug: Node
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



# Are you seeing an error that says "Permission denied" when trying to do an npm install --global?

This is because npm tries to install to a `/usr` path which you can't write to.
To solve this, you can either change the default directory for global packages
or use nvm to take care of installing globally. We recommend using nvm


# Using NVM to get the most updated version of node

NVM allows you to install and run different versions of node (and to manage and
install their "global packages" separately).

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


# Alternatively:  change the default npm-global directory

(note these steps are not compatible with the nvm solution above)

To change the default directory, do something like
    
    mkdir ~/.npm-global
    npm config set prefix '~/.npm-global'

Double check that you do have it setup correctly:

     npm config get prefix

Now npm install --global will install the packages to `~/.npm-global`.

You will also want to add `~/.npm-global` to your path:

    echo 'PATH=~/.npm-global/bin:$PATH' >> ~/.bashrc

Now any new bash consoles that you start will have that path convenience.


