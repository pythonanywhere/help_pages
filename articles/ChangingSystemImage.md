<!--
.. title: Changing your system image
.. slug: ChangingSystemImage
.. date: 2021-02-18 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

You can change your account's system image from the "Account" page. This will
leave all of your files and data as they are, but will change the operating
system files to provide different versions of Python and different pre-installed
Python modules. This means that you can use the latest and greatest stuff :-)

However, **you may need to change your code to make it work with the new
system image**.

## Changing the system image

Go to the "Account" page, and click on the "System image" tab there.  You'll see
a "pencil" icon next to the name of your current image, so click on that and
you'll get a dropdown where you can select the one to switch to. The most
recent one will be at the bottom of the list.

> You will not be able to switch to a system image that is older than the one
> it had when you originally signed up.

We recommend that you read the rest of this page (in particular the part about
virtualenvs, if you are using them) before making the change.

## Using the new system image

Once you have changed the image, code that is currently running will
continue to use the old one, but new consoles you start will
have the new one. Any scheduled tasks and
websites will pick it up the next time they're (re)started. Always-on tasks
will need to be disabled, then enabled again to pick it up.
If you're using Jupyter/IPython notebooks, you'll need to kill
any existing ones using the process list on the "Consoles" page
to make them restart fully to pick up the new Python versions.

## Code changes

Updating the system image means that you may need to change your code afterwards
to make it work again.

### Pre-installed Python packages

Because the pre-installed Python modules will be upgraded,
the change might break any code you have that relies on the old
installed versions.

### Python versions

The new system image may not support the version of Python that you are using.
In particular, double-check the version your app itself is using by going to 
the Code section in the Web tab of your account Dashboard,
and check it against the [per-system-image list of Python versions](/pages/PythonVersions).

### Virtualenvs

Because of the changes to the point releases of Python
(for example, 3.10.5 might be replaced with 3.10.12), any
virtualenvs you have might break -- virtualenvs are not always
portable from one point release to another. You will need to
[rebuild](/pages/RebuildingVirtualenvs), and please note that this will require
you to gather information about the existing virtualenv before you change
the system image.  Also, make sure the Python
version you were previously using is available on the new system image
by checking [this page](/pages/PythonVersions).

### Cached versions of `pip` and packages installed with `pip`

We also recommend that you clear the `~/.cache` folder, since packages
stored there might be picked up when creating new virtualenvs leading
to confusion.  In particular, if after the changeover you start getting
errors like `NameError: name '_mysql' is not defined`, it is likely that you
have a version of the `mysqlclient` library that was installed from the cache
and is not compatible with the updated system image.

## Default Python versions

Along with a system image, your PythonAnywhere account has a set of
default Python versions:

* One of them is the default Python version used by `python` and
  `pip` in Bash consoles. (If your system image is "glastonbury", these
  must be `python2.7` because the older operating system that it uses
  require it to be set up that way.)

* Another one is the default Python 3 version used by `python3` and
  `pip3` in Bash consoles.

* The third one is the default Python used when "Run" button in our
  in-browser editor is pressed.

Each system image has [a range of available Python versions](/pages/PythonVersions).

When one of those defaults is not available after the system
image change, it will be automatically set to the most recent available
Python version.  For example, you might have your system image set to "haggis", with the default
`python3` set to `python3.6`. You update your system image to
"innit", in which Python 3.6 is not available any more.  Your
default `python3` will automatically be set to `python3.13`, which is the
default Python version in "innit".

### Python packages installed

We do not pre-install packages into all Python versions in all system images.
You can check what packages are installed in which system
image [here](https://www.pythonanywhere.com/batteries_included/).

### Webapp Python version

Remember that the Python version run by your app can be different to the defaults 
on the System Image page.

You can check the version your app itself is using by going to the 
Code section in the Web tab of your account Dashboard


## Database Server Versions

Changing the system image will not affect your database servers. Only the client
tools (for example, the `mysql` bash command) will be updated.

To update your MySQL or PostgreSQL server version, you need to contact us
using the "Send feedback" link on your account page, and we will handle the update for you. Updating
the server version involves a brief downtime for your account, so we'll coordinate
timing with you.


## Base Ubuntu version for each system image

|             |Ubuntu version|
|-------------|--------------|
| glastonbury | 20.04        |
| haggis      | 20.04        |
| innit       | 22.04        |
