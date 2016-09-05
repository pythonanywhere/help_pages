
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



The Save &amp; Run button defaults to Python 3.4. If you want to use Python 2,
you can do so by inserting a special line at the top of your file, called a
[hashbang](https://en.wikipedia.org/wiki/Shebang_%28Unix%29):

For example:

    :::python
    #!/usr/bin/python2.7
    print "hello from python 2"



Will load Python 2,

Or, for example:

    :::python
    #!/usr/bin/python3.3
    print("hello from python 3.3")


will load python 3.3 instead of 3.4.

**NB** the hashbang has to be the very first line in the file.
