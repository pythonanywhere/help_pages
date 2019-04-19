
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

To install a package into your account so that your Python programs can see it
by default, use one of the `pip` commands.   There is one for each Python version:
`pip2.7` installs modules for Python 2.7, `pip3.6` installs modules for Python
3.6, and so on.  Modules that you install for one Python version are not visible
from others, so it's important to use the right one.

Example: to install the `pwhich` module for Python 3.6, you'd run this in a Bash
console (not in a Python one):

    :::bash
    pip3.6 install --user pwhich

Please note, the command line option before the module name is quite literally `--user`, you
don't need to replace it with your username, or to add your username to the
command line!

Do let us know if there are any packages you think should be part of our standard "batteries included".


##2\. Using a virtualenv


We've also included `virtualenv` and `virtualenvwrapper`, so if you create a
[virtualenv](/pages/VirtualenvsExplained) you can install whatever versions of various packages you want to.
However, in a virtualenv, the `--user` mentioned above is not needed. In fact
using `--user` will cause an error in a virtualenv.

You can specify which Python version to use for your virtualenv using the
`--python` option.  So, to create a new Python 3.6 virtualenv, run this command:

    :::bash
    $ mkvirtualenv my-virtualenv --python=python3.6

...or similarly for Python 2.7:

    :::bash
    $ mkvirtualenv my-virtualenv --python=python2.7

Once you're in a virtualenv,  to install packages you can just use pip with no
Python version number or `--user` flag:

    :::bash
    (my-virtualenv) $ pip install pwhich

We recommend that in any Python 2.7 virtualenv you create, you install the following
security fix packages:

    :::bash
    (my-virtualenv) $ pip install urllib3[secure] pyopenssl ndg-httpsclient pyasn1

These should make sure that your code can make access external websites without
security warnings.


###Using virtualenvs in web apps


You need to enter the location of your virtualenv on the "Web" tab to use it in
a web app. Check out the [example here](/pages/VirtualEnvForNewerDjango)

