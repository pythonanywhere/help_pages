
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



*If you need to rebuild your virtualenv following a system image upgrade*


The instructions below will contain instructions for people who use plain
`virtualenv` and `virtualenvwrapper`; make sure that you use the appropriate ones
for the kind of virtualenv you're using.  Use a **Bash console** to enter the
commands.

##1) Use a requirements.txt file to record what packages you're using

If you've already got a `requirements.txt` file, you can skip this bit, although
you may want to just do the bit where we double-check what version of Python
we're using.

  1. Activate your virtualenv, using `source /home/myusername/path/to/virtualenv/bin/activate` or, if you're using virtualenvwrapper `workon my-virtualenv-name`
  2. Save the list of packages to a requirements file
    * `pip freeze > /tmp/requirements.txt`
  3. Double-check which version of python is in your virtualenv
    * `python --version`
  4. Deactivate the virtualenv
    * `deactivate`



##2) Remove your old virtualenv

Using plain virtualenvs:

    :::bash
    rm -rf /home/myusername/path/to/virtualenv

or, if using virtualenvwrapper:

    :::bash
    rmvirtualenv my-virtualenv-name


##3) Create a new virtualenv

Using the appropriate Python version in place of `X.Y`:

    :::bash
    virtualenv --python=pythonX.Y /home/myusername/path/to/virtualenv

or, with virtualenvwrappper

    :::bash
    mkvirtualenv --python=pythonX.Y my-virtualenv-name



##4) Reinstall your packages

    :::bash
    pip install -r /tmp/requirements.txt  # or path to your existing requirements.txt


##5) Restart your web app.

On the **Web** tab, use the "Reload" button to restart your website code using the
new virtualenvs -- don't forget to do this for all of your websites if you have several.

You will also need to restart any always-on tasks that use them --
just disable them, then enable them again.  Scheduled tasks that use virtualenvs
will pick them up the next time they run.


##6) All done!

We're here to help! If you get stuck or confused, just drop us a note at
[support@pythonanywhere.com](mailto:support@pythonanywhere.com], and we'll
be happy to help.
