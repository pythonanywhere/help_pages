<!--
.. title: Types of consoles
.. slug: TypesOfConsoles
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

In the [Consoles page](https://www.pythonanywhere.com/consoles/)
you'll find links to start various types of console:

  * Python using either the standard Python shell or [IPython](https://ipython.readthedocs.io/en/stable/). If you've never tried IPython, check it out, it's pretty cool!
  * Bash
  * [PyPy](//pypy.org/)
  * Custom consoles
  * MySQL (on [accounts created after 2026-01-15 (or 2026-01-08 in the EU system)](/pages/FreeAccountsFeatures), paid feature)
  * Postgres (paid feature)
  
For the available **Python/IPython** consoles, check the available Python versions
for your [system image](https://help.pythonanywhere.com/pages/ChangingSystemImage/).

**Custom consoles** are basically Bash commands which start a console with
additional setup, like activating a virtual environment, exporting
some environment variables, etc. For example, if you're developing a
project which uses a virtualenv, you might want to have a console that
opens an IPython shell with that venv activated. Such a command for a
custom console would look like:

    source virtualenvwrapper.sh && workon my_venv && ipython
    
If you want to start a custom Bash console which performs some set up
actions at start, you could use a script like this:

```bash
#!/bin/bash --init-file

source ~/.bashrc
cd MyProjectDir
git status
```

After making the script executable, you can use it as a
command that starts a new custom console -- it will source your
`.bashrc` file, enter `MyProjectDir` and show output of the `git
status` command at the start.
