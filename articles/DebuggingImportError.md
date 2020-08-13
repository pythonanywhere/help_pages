<!--
.. title: Debugging with sys.path / ImportError issues
.. slug: DebuggingImportError
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->




##The theory


When you say:

    :::python
    from foo.bar import baz

...Python will start by looking for a *module* named foo, and then inside that
a module named bar, and then inside that for an object named baz (which may be
a regular python object, or another module)

A **module** is defined as:

  * either a Python file
    * that is, a file on disk that ends in .py and contains valid Python (syntax errors, for example, will stop you from being able to import a file)

  * or a directory (aka folder) which contains Python files.
    * for a directory to become a module, it must contain a special file called `__init__.py`

When a module is actually a directory, the things you can import from it are:

  * any other modules that are inside the directory (ie, more .py files and directory)
  * any objects defined or imported inside the `__init__.py` of the directory

Finally, where does Python look for modules? It looks in each directory
specified in the special `sys.path` variable. Typically (but not always),
`sys.path` contains some default folders, including the current working
directory, and the standard "packages" directory for that system, usually called
site-packages, which is where pip installs stuff to.

So `from foo.bar import baz` could work in a few different ways:

    .
    `-- foo/
        |-- __init__.py
        `-- bar.py          <-- contains a variable called "baz"


Or

    .
    `-- foo/
        |-- __init__.py
        `-- bar/
            |-- __init__.py
            `-- baz.py


Or:

    .
    `-- foo/
        |-- __init__.py
        `-- bar/
            `-- __init__.py     <-- contains a variable called "baz"


What this means is that you need to get a few things right for an import to work:

1. The dot-notation has to work: from foo.bar import baz means foo has to be a module directory, and bar can either be a directory or a file, as long as it somehow contains a thing called baz. Spelling mistakes, including capitalization, matter
2. The top-level `foo` must be inside a directory that's on your sys.path.
3. If you have multiple modules called `foo` on your sys.path, that will probably lead to confusion. Python will just pick the first one.


##Debugging sys.path issues in web apps



###Can you run the wsgi file itself?

Try running this, making sure that you replace the `X.Y` with the version of
Python that you have specified as the one to use for your website on the "Web" page:

    $ pythonX.Y -i /var/www/www_my_domain_com_wsgi.py


Or, if you're using a virtualenv, activate it first, and then you can just use
`python` (because the version to use is "baked into" the virtualenv:

    $ workon my-virtualenv
    (my-virtualenv)$ python -i /var/www/www_my_domain_com_wsgi.py


If this shows any errors and won't even load python (eg. syntax errors), you'll need to fix them.

If it loads OK, it will drop you into a Python shell. Try doing the import manually at the command line. Then, check whether they really are coming from where you think they are:

    :::python
    from foo.bar import baz
    import foo
    print(foo.__file__)  # this should show the path to the module.  Is it what you expect?
    import sys
    print('\n'.join(sys.path)) # does this show the files and folders you need?




##Django-specific issues


In Django, we sometimes don't import modules directly in the WSGI file, but we
do specify a dot-notation import path to the settings in an environment
variable. Django will try and import it later, so you need to get this right as
if it was an import.

eg:

    :::python
    path = "/home/myusername/myproject"
    if path not in sys.path:
        sys.path.insert(0, path)

    os.environ["DJANGO_SETTINGS_MODULE"] = "myproject.settings"



What this implies is that you have a directory tree that looks like this:

    /home/myusername
    `-- myproject/
        |-- __init__.py
        `-- myproject/
            |-- __init__.py
            `-- settings.py

If in doubt, try the

    python -i /var/www/www_my_domain_com_wsgi.py
    >>> import myproject.settings
    # this should work. if this doesn't, figure out why.  print sys.path, etc.



###Other tips



####Can you run the files it's trying to import?


eg, if your wsgi file does `from myapp import settings`, can you run:

    pythonX.Y /path/to/myapp/settings.py


?


####Shadowing


Could there be any sort of "shadowing" going on? do any of your modules have the same name as system modules? eg, if you're trying to do

    :::python
    from package import thing


What happens if you open up a console and type

    :::python
    import package
    print(package.__file__)


does it give you the path to your package, or to a system package? if the former, it's best to rename your own module to avoid the conflict.

##Check virtualenv Python versions


If you're using a virtualenv, just double-check that the Python version of your virtualenv is the same as the one on the web tab.

  * you can check the virtualenv version with `python --version` (remember to activate your virtualenv fist with `workon my-virtualenv-name` first)
  * you can check the webapp python version on the **Web** tab, it's indicated near the top.


##Python version mismatch

If you manually install packages with pip, the packages will
be installed *only* for the specific Python version that you specified when
installing them.  For example, if you install a package like this:

    pip3.8 install --user foo

...then the package `foo` will only be installed for Python 3.8.

That means that if your website is configured to use a different Python version (say, 3.7)
on the "Web" page, it will not be able to use the `foo` package.

This can be confusing, because if you are running code elsewhere using Python 3.8,
it will work.  That's why it's important to make sure that you use the right
version of Python when running your WSGI file in the "Can you run the wsgi file itself?"
section above.

