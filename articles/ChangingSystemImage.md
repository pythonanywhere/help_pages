<!--
.. title: Changing your system image
.. slug: ChangingSystemImage
.. date: 2020-08-12 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

You can change your account's system image from the "Account" page.  This will
leave all of your files and data as they are, but will change the operating
system files to provide different versions of Python and different pre-installed
Python modules.  This means that you can use the latest and greatest versions
of Python :-)

However, **you may need to change your code to make it work with the new
system image**.

## Changing the system image

Just click on the "pencil" icon next to the name of your current image, and
you'll get a dropdown where you can select the one to switch to.  The most
recent one will be at the bottom of the list.

> You will not be able to switch to a system image that is older than the one
> it had when you originally signed up.


## Using the new system image

Once you have changed the image, code that is currently running will
continue to use the old one, but new consoles you start will
have the new one.  Any scheduled tasks and
websites will pick it up the next time they're (re)started.  Always-on tasks
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

### Virtualenvs

Because of the changes to the point releases of Python
(for example, 3.7.0 might be replaced with 3.7.5), any
virtualenvs you have might break -- virtualenvs are not always portable from one
point release to another.
