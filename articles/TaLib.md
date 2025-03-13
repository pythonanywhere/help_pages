<!--
.. title: Installing TA-Lib on PythonAnywhere
.. slug: TaLib
.. date: 2025-03-13 16:00:00 UTC
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

The TA-Lib operating system package is already installed on PythonAnywhere, so
in order to use it from Python you just need to install the correct version of
the [ta-lib Python bindings](https://pypi.org/project/ta-lib/).

Firstly, run this bash command to see which version of the OS package you have:

```bash
dpkg -l | grep ta-lib
```

You'll see something like this:

```
ii  ta-lib                                 0.4.0                                         amd64        no description given
```

The number in the middle (`0.4.0` in this example) is the version of the OS
package.

The version of the Python package that you need is the most recent one that has
the same first two parts of the version number as the OS package -- so, in this
example, it would be the most recent `0.4` release -- say, `0.4.123`.  The easiest
way to install that is to ask pip to install a version lower than the following
release -- in this example we'd want to tell it to  install the most recent
version that is less than `0.5`.  Here's how you would do that:

```bash
pip install 'ta-lib<0.5'
```

Note the single quotes around the package name and the version -- they're important!

That should complete successfully, and you'll have a working version of TA-Lib
and its Python bindings installed.


