
<!--
.. title: How can I use a different version of Python for the Save & Run button?
.. slug: SaveAndRunPythonVersion
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



The Save &amp; Run button defaults to Python 3. If you want to use Python 2,
you can do so by inserting a special line at the top of your file, called a
[hashbang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29):

For example:

    :::python
    #!/usr/bin/env python2.7
    print "hello from python 2"



Will load Python 2,

Or, for example:

    :::python
    #!/usr/bin/env python3.3
    print("hello from python 3")



will load python 3.3 instead of 3.4.

**NB** the hashbang has to be the very first line in the file.

You could also use `/usr/bin/python2.7`, but the `/usr/bin/env python2.7`
formulation makes the hashbang compatible with virtualenvs.

## Save & Run with virtualenvs
At some point, you may want to run a Python file that requires specific
packages that you have installed into a virtualenv. In order to do this, you
can also use a shebang like above, except that the path you specify will be the
path to the python executable in your virtualenv. Like this:

Assuming your vitualenv directory is `/home/me/.virtualenvs/my-venv`, you would
use a shebang of:

    :::bash
    #!/home/me/.virtualenvs/my-venv/bin/python
