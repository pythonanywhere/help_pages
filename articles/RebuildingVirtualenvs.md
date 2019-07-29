
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



*If you need to rebuild your virtualenv following a system upgrade*


##1) Identify your virtualenv


Navigate to the **Web** tab and take a look at the *WSGI file* for each of your web apps. At the top (if it's using a virtualenv), you'll find a line that contains the line `activate_this`. That will include the path to your virtualenv.

  **_NOTE:_** If you can't find that line, read this: https://help.pythonanywhere.com/pages/UpgradingToTheNewVirtualenvSystem

  * If the path starts with `/home/myusername/.virtualenvs/...`, then you're using virtualenvwrapper.

The instructions below will contain instructions for people who use plain `virtualenv` and `virtualenvwrapper`. Use a **Bash console** to enter these commands.


##2) Use a requirements.txt file to record what packages you're using


If you've already got a `requirements.txt` file, you can skip this bit, although you may want to just do the bit where we double-check what version of Python we're using.

  1. Activate your virtualenv, using `source /home/myusername/path/to/virtualenv/bin/activate` or, if you're using virtualenvwrapper `workon my-virtualenv-name`
  2. Save the list of packages to a requirements file
    * `pip freeze > /tmp/requirements.txt`
  3. Double-check which version of python is in your virtualenv
    * `python --version`
  4. Deactivate the virtualenv
    * `deactivate`



##3) Delete your old virtualenv


    :::bash
    rm -rf /home/myusername/path/to/virtualenv


or, if using virtualenvwrapper:

    :::bash
    rmvirtualenv my-virtualenv-name



##4) Rebuild a new virtualenv


Using the appropriate Python version:

    :::bash
    virtualenv --python=pythonX.Y /home/myusername/path/to/virtualenv


or, with virtualenvwrappper

    :::bash
    mkvirtualenv --python=pythonX.Y my-virtualenv-name



##5) Reinstall your packages


    :::bash
    pip install -r /tmp/requirements.txt  # or path to your existing requirements.txt



##6) Restart your web app.


Back on the **Web** tab.

If you have multipe web apps with multiple different virtualenvs, you'll need to do this for each one, obviously.

We're here to help! If you get stuck or confused, just drop us a note, and we'll be happy to help.
