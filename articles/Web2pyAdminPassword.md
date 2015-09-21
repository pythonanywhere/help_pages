
<!--
.. title: Changing your Web2py Admin Password
.. slug: Web2pyAdminPassword
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



  * Open a Bash console and cd to your web2py directory. You'll know you're in the right place if there's a file called `parameters_443.py` in the directory.
  * Run this:

        ::python
        python -c "from gluon.main import save_password; save_password(raw_input('admin password: '),443)"
