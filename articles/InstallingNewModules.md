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

## Installing Python modules on PythonAnywhere


Your account has many modules [already installed](https://www.pythonanywhere.com/batteries_included/).
You can install new modules into PythonAnywhere by using a **Bash Console**


##1\. Using the --user flag

To install a package into your account so that your Python programs can see it
by default, use one of the `pip` commands.   There is one for each Python version:
`pip3.12` installs modules for Python 3.12, `pip3.13` installs modules for Python
3.13, and so on.  Modules that you install for one Python version are not visible
from others, so it's important to use the right one.

Example: to install the `pwhich` module for Python 3.13, you'd run this in a Bash
console (not in a Python one):

    :::bash
    pip3.13 install --user pwhich

Please note, the command line option before the module name is quite literally `--user`, you
don't need to replace it with your username, or to add your username to the
command line!

Do let us know if there are any packages you think should be part of our
standard "batteries included" -- just use the "Send feedback" link above, or
send us a message at [support@pythonanywhere.com](mailto:support@pythonanywhere.com).


##2\. Using a virtualenv

We've also included `virtualenv` and `virtualenvwrapper`, so if you create a
[virtualenv](/pages/VirtualenvsExplained) you can install whatever versions of various packages you want to.
However, in a virtualenv, the `--user` mentioned above is not needed. In fact
using `--user` will cause an error in a virtualenv.

You can specify which Python version to use for your virtualenv using the
`--python` option.  So, to create a new Python 3.13 virtualenv, run this command:

    :::bash
    $ mkvirtualenv my-virtualenv --python=python3.13

...or similarly for other python versions.

Once you're in a virtualenv,  to install packages you can just use pip with no
Python version number or `--user` flag:

    :::bash
    (my-virtualenv) $ pip install pwhich


###Using virtualenvs in web apps

You need to enter the location of your virtualenv on the "Web" tab to use it in
a web app. Check out the [example here](/pages/VirtualEnvForNewerDjango)



##3\. Installers that print out excessive amounts

Some packages, when they are installing, print out huge amounts of stuff, and
that can cause problems -- you'll get an error saying this:

```
Your console is printing so much that it's interfering with other users, so it has been closed
```

To avoid this, you can add the `-q` command-line flag to your `pip` command.



##4\. Installing non-Python packages

You don't have root access to the computers where your code runs on PythonAnywhere,
so you can't use tools like `apt` to install packages.  However, for non-Python tools that
can be downloaded and compiled from source using `make`, there are
[some tricks that will often work](/pages/CompilingCPrograms).

