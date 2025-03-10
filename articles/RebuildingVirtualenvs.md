<!--
.. title: Rebuilding a Virtualenv
.. slug: RebuildingVirtualenvs
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

If you are doing a [system image upgrade](/pages/ChangingSystemImage), you are
likely to need to rebuild your virtualenvs.

There are two steps to this process; firstly, *before* you change the image, you
will need to gather information about the virtualenv.  Then, *after* you have
changed it, you will be able to build a new one using that information.

The instructions below contain instructions for people who use plain
`virtualenv` and `virtualenvwrapper`; make sure that you use the appropriate ones
for the kind of virtualenv you're using.  Use a **Bash console** to enter the
commands.

## 1) Before the system image change

Firstly, activate the virtualenv.  If you're using virtualenvwrapper:

```bash
workon my-virtualenv-name
```

Or, if you're using a plain one:

```bash
source /home/myusername/path/to/virtualenv/bin/activate
```

Next, generate a `requirements.txt` file to record what packages you're using.
If you've already got a file like that, you can skip this, but otherwise:

```bash
pip freeze > /tmp/requirements.txt
```

Next, check which Python version you are using:

```bash
python --version
```

Finally, deactivate the virtualenv

```bash
deactivate
```

Now you have saved the information you need about the virtualenv, so you can
change the system image.


## 2) After the system image change

First of all, **start a fresh Bash console**.

We recommend that you create a new virtualenv with a different name, just in
case something goes wrong in its creation.

The first step is to remove the `.cache` directory from your home directory,
because it may have versions of packages that pip will think are the right ones,
but will only work with the old system image:

```bash
rm -rf ~/.cache/
```

> The `mysqlclient` library is particularly prone to problems like this; if
> after the change over you start getting errors like
> `NameError: name '_mysql' is not defined`, it is likely that you
> have a version of it that was installed from the cache
> and is not compatible with the updated system image.

The next step is to identify the version of Python that you are going to use; check
that the version that you identified when gathering data about your old virtualenv
is available in the new system image by looking at the table at the bottom of the
[system images page](/pages/ChangingSystemImage).  Note that the version that you
got above will be a full three-part version, for example 3.9.13.  The numbers after the second "."
are not important here; for example, if you got 3.9.13, any image that supported 3.9 would be OK.

Once you've determined the Python version, create the new virtualenv -- this will
only need the first two parts of the version number (eg. 3.9 or 3.12 -- not a full version
like 3.12.4).  If you're using
virtualenvwrapper, create it like this:

    :::bash
    mkvirtualenv --python=pythonX.Y my-new-virtualenv-name

Or, for a plain virtualenv:

    :::bash
    virtualenv --python=pythonX.Y /home/myusername/path/to/new-virtualenv

Next, you can reinstall your packages.  Ensure your new virtualenv is activated, then:

    :::bash
    pip install -r /tmp/requirements.txt  # or path to your existing requirements.txt

Once that's done, you can start using it.

If your virtualenv is used in a website, change the virtualenv setting on the "Web"
page, and then click the green "Reload" button to restart the site using it.
For always-on and scheduled tasks, change the command used to run them to pick up the new virtualenv
-- you will normally have a `workon` command, or use a specific path to the Python
interpreter to specify the virtualenv for those.


## 3) All done!

We're here to help! If you get stuck or confused, just drop us a note at
[support@pythonanywhere.com](mailto:support@pythonanywhere.com).
