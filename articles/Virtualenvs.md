
<!--
.. title: How to use a virtualenv in your web app (to get newer versions of django, flask etc)
.. slug: Virtualenvs
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



A [virtualenv](https://virtualenv.pypa.io/en/latest/) is a way to create a python environment that's isolated and separate from the normal system-wide installed packages. It's particularly useful if you decide our 'default' versions of packages are not the versions you want to use -- to get the latest django, for example.


##Using a virtualenv in your web app


Create a new web app using the "manual config" option, or visit one of your existing web apps, and you'll see a section called "Virtualenvs" in the config tab. This allows you to specify the path to an existing virtualenv. Read on for instructions on how to create one.


##Creating a virtualenv


We recommend using *virtualenvwrapper*, a handy command-line tool, to create your virtualenv. Here's an example:

    $ mkvirtualenv myvirtualenv --python=/usr/bin/python3.4


    Running virtualenv with interpreter /usr/bin/python3.4
    Using base prefix '/usr'
    New python executable in myvirtualenv/bin/python3.4
    Also creating executable in myvirtualenv/bin/python
    Installing setuptools, pip...done.


    (myvirtualenv) $ which python
    /home/myusername/.virtualenvs/bin/python
    (myvirtualenv) $ deactivate
    $ which python
    /usr/bin/python
    $ workon myvirtualenv
    (myvirtualenv) $ which python
    /home/myusername/.virtualenvs/bin/python


    (myvirtualenv) $ python
    Python 3.4.0 (default, Apr 11 2014, 13:05:11)
    [GCC 4.8.2] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>


  * You can specify whichever version of Python you like for your virtualenv, but *it must match the version of python you've chosen for your web app*
  * Once you create your virtualenv, you need to **activate** it. It's automatically activate straight after you create it with `mkvirtualenv`, and you can re-activate it later with `workon myvirtualenv`.
  * You can tell whether your virtualenv is active, because its name appears in your prompt -- you see `(myvirtualenv) $`.


##Installing virtualenvwrapper if you need to


If you see a `command not found` error when trying to run `mkvirtualenv`, you'll find some installation instructions here: [InstallingVirtualenvWrapper](/pages/InstallingVirtualenvWrapper)


##Installing stuff into your virtualenv


    $ workon myvirtualenv


    (myvirtualenv) $ which pip  # this lets you check that the virtualenv has been activated
    /home/myusername/.virtualenvs/myvirtualenv/bin/pip


    (myvirtualenv) $ pip install django==1.7.1 # or flask, or whichever modules you want to use, optionally specifying a version number


    Downloading/unpacking django==1.7.1
      Downloading Django-1.7.1-py2.py3-none-any.whl (7.4MB): 7.4MB downloaded
    Installing collected packages: django
    Successfully installed django
    Cleaning up...



##Using your virtualenv back in your web app


Now that you have a virtualenv, and you know its path, you can go and enter it back in the **Web** tab.

Go to the Virtualenv section, and enter the path: `/home/myusername/.virtualenvs/myvirtualenv`

  * TIP: if you're using virtualenvwrapper, you can just enter the name of the virtualenv, *myvirtualenv*, and the system will automatically guess the rest of the path (*/home/myusername/.virtualenvs etc*) after you hit ok

Now, **Reload** your web app, and you should find it has access to all the packages in your virtualenv, instead of the system ones.
