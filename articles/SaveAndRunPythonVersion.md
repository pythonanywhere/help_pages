
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



The Save &amp; Run button defaults to the version of Python that was the most recent one that we supported
when your account was created -- which for all but the oldest accounts will be a recent 3.x. If you want to use
a different version,
you can do so by inserting a special line at the top of your file, called a
[hashbang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29).

For example, you could use 2.7 like this:

    :::python
    #!/usr/bin/python2.7
    print "hello from python 2.7"


Or you could use 3.4 like this:

    :::python
    #!/usr/bin/python3.4
    print("hello from python 3.4")


You can also use a hashbang to run your script in a virtualenv that you've
defined by pointing it at the python executable in the virtualenv.

    :::python
    #!/home/myusername/.virtualenvs/myvenv/bin/python
    print("hello from python in a virtualenv")


**NB** the hashbang has to be the very first line in the file.
