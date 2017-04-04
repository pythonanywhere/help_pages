
<!--
.. title: Installing new modules
.. slug: InstallingNewModules
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->





##Installing Python modules on PythonAnywhere


You can install new modules into PythonAnywhere by using a **Bash Console**


##1\. Using the --user flag


We've included both `easy_install` and `pip` for Python versions 2.6, 2.7 and 3.3 (the default is 2.7, use `pip2.6` or `pip3` / `pip3.3` / `easy_install-3.3` for other versions), but you'll need to pass the `--user` flag to them, which will install modules to a directory (.local) inside your home folder. Please note, this is quite literally `--user`, you don't need to replace it with your username, or to add your username to the command line!

Example: to install the `pwhich` module, you'd run this:

    :::bash
    pip install --user pwhich


Do let us know if there are any packages you think should be part of our standard "batteries included".


##2\. Using a virtualenv


We've also included `virtualenv` and `virtualenvwrapper`, so if you create a virtualenv you can install whatever versions of various packages you want to. However, in a virtualenv, the `--user` is not needed. In fact using `--user` will cause an error in a virtualenv.

    :::bash
    $ mkvirtualenv my-virtualenv
    (my-virtualenv) $ pip install pwhich

We recommend that in any Python 2.7 virtualenv you create, you install the following
security fix packages:

    :::bash
    (my-virtualenv) $ pip install urllib3[secure] pyopenssl ndg-httpsclient pyasn1


###Using virtualenvs in web apps


You need to enter the location of your virtualenv on the "Web" tab to use it in a web app. Check out the [example here](/pages/VirtualEnvForNewerDjango)


##3\. To use Python 3



###Python 3, with --user


Use

    :::bash
    pip3.5 install --user packagename


*(installers for Python2.6 are `pip2.6` and `easy_install-2.6`, and you can also use `pip3.3` / `easy_install-3.3` or `pip3.4` / `easy_install-3.4`)*


###Python 3, with a virtualenv


Use the additional flag `--python=python3.5`, eg:

    :::bash
    mkvirtualenv --python=python3.5 myvirtualenv



###Packages requiring compilation


We provide some compilers (eg gcc, g++), but not all. If your package installation fails with an error that looks like it might have been trying to compile something, you'll need to contact us to get us to install it for you. Use the "send feedback" button.
