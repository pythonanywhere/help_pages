<!--
.. title: What is a virtualenv, and why would I use one?
.. slug: VirtualenvsExplained
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

A virtualenv is way to create an isolated Python environment with specific installed
packages inside it.

When you run your code normally -- as a website, a scheduled
task, or in any other way -- it doesn't run in a virtualenv, but in the
*system environment*.

But with appropriate setup, it can run in a virtualenv.  When you do that, the
running code will only see the specific packages that are installed in that env.

This means that you can have different virtualenvs for different uses.  For example,
if you had two websites, they could each use a different virtualenv so that they
could use different packages.  If one website needed Flask version
3.10.0, and another needed version 4.0.0, you could run both inside the same
PythonAnywhere account by making them use different virtualenvs with the appropriate
versions installed.

You don't need to use virtualenvs to run your code on PythonAnywhere -- indeed,
when you're getting started, it's best not to, and to use the system environment instead.  We have a lot of
[useful packages pre-installed](https://www.pythonanywhere.com/batteries_included/),
so you can just use them.  Doing that has the advantage that unlike virtualenvs,
the packages in the system environment don't use up any of your disk space.

But if you need extra modules that are not pre-installed, or if you want
to manage which specific versions of different packages you're using, using
a virtualenv is a good idea.

To create a virtualenv, we recommend using the `mkvirtualenv` Bash command.  This will
create a virtualenv in the directory `.virtualenvs` in your home directory:

```bash
mkvirtualenv myvirtualenv --python=python3.13
```

That command will create a virtualenv called `myvirtualenv` using Python version 3.13.
Note that the version of Python that you specify must be one
[that is available in your account's system image](/pages/PythonVersions).

When the command completes, you'll see a prompt that has the virtualenv's name at the start,
like this:

```bash
(myvirtualenv) 13:01 ~ $
```

When that is at the start of your Bash prompt, your virtualenv is active -- if you
run a Python script, it will only see the packages in the virtualenv.  You can then
use the `pip` command to install the packages that you need.

If you want to activate the virtualenv in the future -- let's say, if you're using
a new Bash console where it's not already active -- you use the `workon` command:

```bash
workon myvirtualenv
```

Here's how to use your virtualenvs in the parts of PythonAnywhere outside of Bash consoles:

  * [Specifying a virtualenv to be used when running from the editor](/pages/SaveAndRunPythonVersion)
  * Websites:
    * [General advice for virtualenvs in websites](/pages/VirtualEnvForWebsites)
    * [Virtualenvs for Django specifically](/pages/VirtualEnvForNewerDjango)
  * [Using virtualenvs in scheduled tasks](/pages/ScheduledTasks#using-a-virtualenv)
  * [Using virtualenvs in always-on tasks](/pages/AlwaysOnTasks#using-virtualenvs-in-always-on-tasks)
  * [How to use virtualenvs in an Jupyter Notebook](/pages/IPythonNotebookVirtualenvs)


# Notes for virtualenvs in `innit`
Some users have reported issues using virtualenvs in the `innit` system image.

There is a simple explanation for it and also, a simple fix.

The issue arises because we have symlinks in /usr/bin for all of the
versions of Python that `innit` supports. They point to where that Python
version is actually installed in /usr/local/bin. However, if a virtualenv is created
using the /usr/bin symlink, then the virtualenv will be broken and you
will not be able to install anything into it.

The simple fix is to ensure that /usr/local/bin is on your PATH before /usr/bin, then you can use

```bash
mkvirtualenv -p python3.11 venv
```
to create your virtualenv.

Alternatively, you can also just use
```bash
mkvirtualenv -p /usr/local/bin/python3.11 venv
```
to create your virtualenv and it will be created correctly.

