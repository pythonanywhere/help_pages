
<!--
.. title: Upgrading to the new virtualenv system
.. slug: UpgradingToTheNewVirtualenvSystem
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



Here's how to use the new, shiny virtualenv system if you were using the old (slightly hacky) solution based on `exec` and `activate_this`. 


##Edit your wsgi file and remove the activate_this call


Go to the **Web** tab and follow the link to your wsgi file. Look for the 'activate_this' lines, which should look something like this: 

    activate_this = '/home/myusername/.virtualenvs/django17/bin/activate_this.py'
    with open(activate_this) as f:
        code = compile(f.read(), activate_this, 'exec')
        exec(code, dict(__file__=activate_this))


Take a note of the path to your virtualenv (in this case, it's */home/myusername/.virtualenvs/django17/*), and then just go ahead go ahead and delete those activate_this lines altogether. Mkay. 


##Add the virtualenv path to your web app config


Back on the **Web** tab, paste in the path to your virtualenv in the virtualenv section. Hit reload, and, hey presto! your virtualenv should just work 


##If you see any errors with missing modules


The old `activate_this` system used to actually leave all the system-installed modules on the *sys.path*, which caused all sorts of weird problems with shadowing. If you find that your web app is now showing you errors because it's missing some packages, it's probably because you were relying on some system-installed packages without realising it. 

To fix it you have two choices 

  * Installed those packages explicitly into your virtualenv 
  * Delete and re-create your virtualenv with the `--system-site-packages` option, to explicitly make yourself a virtualenv with system packages. 

The former is probably preferable. We're here if you need help! Just drop us a line in the forums. 
