<!--
.. title: What is a virtualenv, and why would I use one?
.. slug: VirtualenvsExplained
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


The Python programming language has a bunch of packages build in, the
["Standard Library"](https://docs.python.org/3.6/library/index.html), which do a lot of useful things.
However, most code that you write will probably use packages that aren't officially part of Python --
they're separate open-source packages, which are maintained by separate groups of people.
For example, a simple Flask app might depend on three: the [Flask](http://flask.pocoo.org/) framework,
[Flask-SQLAlchemy](http://flask-sqlalchemy.pocoo.org/2.1/),
and the underlying [SQLAlchemy]((http://www.sqlalchemy.org/)) package that Flask-SQLAlchemy depends on.
There's an official website that lists almost
all of the popular Python packages, the [Python Package Index](https://pypi.python.org/pypi), normally
abbreviated to PyPI.

If you were to install Python on your own machine, you'd just get the standard library; if you wanted
Flask and the others, you'd need to install them separately.   PythonAnywhere, in order to make it easy
to get started, has a [*lot*](https://www.pythonanywhere.com/batteries_included/) of them pre-installed.
But it doesn't have everything -- there are 177,776 packages on PyPI as of this writing, so you can see
how that might be a bit impractical.

The normal way to install packages from PyPI is using a tool called `pip`.  It can install things three
different ways:

1. For the entire system, so that every Python program you run has access to it.  Unfortunately you can't
do this on PythonAnywhere -- everyone has the same system image.
2. Just for your own user account, so just your programs (and no-one else's) have access to it.  Other
people on the system would have to install it too in order to use it.  This is possible on PythonAnywhere,
but it's not the best way, which is:
3. Into a virtualenv.  A virtualenv, or "virtual environment", is a separate directory in your home
directory that contains non-system packages that you've chosen to install into the virtualenv.
When you run some Python code (or in your website setup) you can say "use the virtualenv called X",
and then that code will have access to the standard library and the virtualenv's packages -- nothing else.

So why is that useful?  It's basically because code changes over time.  You can be pretty certain that
the Python core developers won't change things drastically in a new version in a manner that will cause
your code to stop working -- or, at least, they won't do it without plenty of warning.   But the same
doesn't necessarily hold for other packages.

*(I'm going to use Flask as an example of a rapidly-changing package below, which isn't remotely fair --
the Flask team are super-careful about not breaking people's stuff without warning.  But the risks still
hold -- maybe you might miss their announcement that they were going to change things.  Or, more likely,
you might encounter a problem with a package with a less-careful maintainer.)*

Let's say you create a website based on Flask 0.12.  You have it up and running, and people are using it.
One day, you decide to write a new, separate website.   You've heard that the latest version of Flask,
0.18, has lots of great new stuff in it, so you install it on PythonAnywhere so that you can use the new things.

Unfortunately, what you didn't realise was that 0.18 wasn't backward-compatible with 0.12 -- that is, the code
that you wrote with 0.12 doesn't work with 0.18.   Your popular site is broken, and people start sending you
grumpy emails.  So now you need to either roll back your account to the older version of Flask and write your new site using
0.12, or you need to change all of your old code to work with the new version.

If you've not done much development before, this may sound like a kind of abstract, "let's worry about it later"
kind of problem.   And it is, and would be... right up until the point you found yourself frantically dealing
with version compatibility problems and cursing the day you thought it might be a good idea to learn to code.

So how would a virtualenv have helped in this case?  Well, when you wrote your first app, you would have created
a virtualenv for it.  Into that virtualenv, you'd install Flask 0.12, and you'd have configured the website to
use that virtualenv.

When you started work on your new website later, and decided you wanted access to all of that Flask 0.18 goodness,
you'd create a completely new virtualenv, install 0.18 into that, and set up the new website to use it.
The two would be isolated from each other.   Disaster averted!
