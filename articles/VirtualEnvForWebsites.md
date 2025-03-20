<!--
.. title: How to use a virtualenv in your website's code
.. slug: VirtualEnvForWebsites
.. date: 2025-03-20 19:00:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

A [virtualenv](/pages/VirtualenvsExplained) is a way to create a python environment that's isolated and separate from the normal system-wide installed packages. It's particularly useful if you decide our 'default' versions of packages are not the versions you want to use -- to get the latest django, for example.


##Using a virtualenv in your web app


You can use a virtualenv in a new web app (created using the “Manual configuration” option) or in your existing web apps. To use a virtualenv in your web app, do the following:

1. Create a virtualenv

2. Install packages into your virtualenv

3. Configure your app to use this virtualenv



##Step 1: Create a virtualenv

Go to the **Consoles** tab and start a Bash console.

We recommend using *virtualenvwrapper*, a handy command-line tool, to create your virtualenv.

Specify which Python version to use for your virtualenv using the `--python`
option, but note that it must match the version of Python you've chosen for your
web app. So, to create a new Python 3.10 virtualenv, run this command:


    $ mkvirtualenv myvirtualenv --python=/usr/bin/python3.10

You’ll see your virtualenv being created


    created virtual environment CPython3.10.5.final.0-64 in 18417ms
      creator CPython3Posix(dest=/home/myusername/.virtualenvs/myvirtualenv, clear=False, no_vcs_ignore=False, global=False)
      seeder FromAppData(download=False, pip=bundle, setuptools=bundle, wheel=bundle, via=copy, app_data_dir=/home/myusername/.local/share/virtualenv)
        added seed packages: pip==22.1.2, setuptools==62.6.0, wheel==0.37.1
      activators BashActivator,CShellActivator,FishActivator,NushellActivator,PowerShellActivator,PythonActivator
    virtualenvwrapper.user_scripts creating /home/myusername/.virtualenvs/myvirtualenv/bin/predeactivate
    virtualenvwrapper.user_scripts creating /home/myusername/.virtualenvs/myvirtualenv/bin/postdeactivate
    virtualenvwrapper.user_scripts creating /home/myusername/.virtualenvs/myvirtualenv/bin/preactivate
    virtualenvwrapper.user_scripts creating /home/myusername/.virtualenvs/myvirtualenv/bin/postactivate
    virtualenvwrapper.user_scripts creating /home/myusername/.virtualenvs/myvirtualenv/bin/get_env_details


    (myvirtualenv) $ which python
    /home/myusername/.virtualenvs/myvirtualenv/bin/python

NOTE: If you see a `command not found` error when trying to run `mkvirtualenv`, you'll find some installation instructions here: [InstallingVirtualenvWrapper](/pages/InstallingVirtualenvWrapper)

Once your virtualenv is ready and active, you’ll see `(myvirtualenv) $` in your prompt.


##Step 2: Install packages into your virtualenv

Install the required packages into your virtualenv using `pip`. You can just use pip without the Python version number or `--user` flag.


    $ workon myvirtualenv


    (myvirtualenv) $ which pip  # this lets you check that the virtualenv has been activated
    /home/myusername/.virtualenvs/myvirtualenv/bin/pip


    (myvirtualenv) $ pip install django==1.7.1 # or flask, or whichever modules you want to use, optionally specifying a version number


    Downloading/unpacking django==1.7.1
      Downloading Django-1.7.1-py2.py3-none-any.whl (7.4MB): 7.4MB downloaded
    Installing collected packages: django
    Successfully installed django
    Cleaning up...



##Step 3: Configure your app to use this virtualenv


Now that you have a virtualenv, and know its path, configure your app to use this virtualenv.

Go to the **Web** tab, and in the Virtualenv section, enter the path: `/home/myusername/.virtualenvs/myvirtualenv`

  * TIP: if you're using virtualenvwrapper, you can just enter the name of the virtualenv, *myvirtualenv*, and the system will automatically guess the rest of the path (*/home/myusername/.virtualenvs etc*) after you hit ok.

Now, **Reload** your web app, and you should find it has access to all the packages in your virtualenv, instead of the system ones.

##Deactivating and reactivating your virtualenv

Once you create your virtualenv, you need to activate it. It's automatically activated straight after you create it with `mkvirtualenv`, and you can re-activate it later with `workon`.

Re-activate using `workon`:

    $ workon myvirtualenv
    (myvirtualenv) $ which python
    /home/myusername/.virtualenvs/myvirtualenv/bin/python
    (myvirtualenv) $ python
    Python 3.10.5 (main, Jul 22 2022, 17:09:35) [GCC 9.4.0] on linux
    Type "help", "copyright", "credits" or "license" for more information.
    >>>

To deactivate, use `deactivate`:

    (myvirtualenv) $ deactivate
    $ which python
    /usr/bin/python



