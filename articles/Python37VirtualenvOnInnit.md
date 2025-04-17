<!--
.. title: Python 3.7 virtualenvs on the "innit" system image
.. slug: Python37VirtualenvOnInnit
.. date: 2025-03-20 18:25:00 UTC+00:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

If you're using our "innit" system image, and want to create a [virtualenv](/pages/VirtualenvsExplained) to use
Python 3.7, you'll need to specify which versions of `pip`, `setuptools`, and 
`wheel` you want -- otherwise the `mkvirtualenv` command will install
versions that aren't compatible with that version of Python.  Here's an example of how to do that:

```bash
mkvirtualenv myvirtualenv --python=python3.7 --pip 24.0 --setuptools 68.0.0 --wheel 0.42.0
```

Version 24.0 is the last version of `pip`, 68.0.0 is the last version of 
`setuptools` and 0.42.0 is the last version of `wheel` that are compatible with 
Python 3.7.

You will also have to activate the virtualenv after making it -- normally,
`mkvirtualenv` does that for you automatically, but if it's run with the `--pip`
option it doesn't.  So:

```
workon myvirtualenv
```

If you don't specify the pip version and it installs an incompatible version, you'll
get an error that will look something like this when you run `pip`:

```
Traceback (most recent call last):
  File "/home/yourusername/.virtualenvs/myvirtualenv/bin/pip", line 5, in <module>
    from pip._internal.cli.main import main
  File "/home/yourusername/.virtualenvs/myvirtualenv/lib/python3.7/site-packages/pip/_internal/cli/main.py", line 11, in <module>
    from pip._internal.cli.autocompletion import autocomplete
  File "/home/yourusername/.virtualenvs/myvirtualenv/lib/python3.7/site-packages/pip/_internal/cli/autocompletion.py", line 10, in <module>
    from pip._internal.cli.main_parser import create_main_parser
  File "/home/yourusername/.virtualenvs/myvirtualenv/lib/python3.7/site-packages/pip/_internal/cli/main_parser.py", line 9, in <module>
    from pip._internal.build_env import get_runnable_pip
  File "/home/yourusername/.virtualenvs/myvirtualenv/lib/python3.7/site-packages/pip/_internal/build_env.py", line 18, in <module>
    from pip._internal.cli.spinners import open_spinner
  File "/home/yourusername/.virtualenvs/myvirtualenv/lib/python3.7/site-packages/pip/_internal/cli/spinners.py", line 9, in <module>
    from pip._internal.utils.logging import get_indentation
  File "/home/yourusername/.virtualenvs/myvirtualenv/lib/python3.7/site-packages/pip/_internal/utils/logging.py", line 13, in <module>
    from pip._vendor.rich.console import (
  File "/home/yourusername/.virtualenvs/myvirtualenv/lib/python3.7/site-packages/pip/_vendor/rich/console.py", line 41, in <module>
    from pip._vendor.typing_extensions import (
  File "/home/yourusername/.virtualenvs/myvirtualenv/lib/python3.7/site-packages/pip/_vendor/typing_extensions.py", line 1039
    def TypedDict(typename, fields=_marker, /, *, total=True, closed=False, **kwargs):
                                            ^
SyntaxError: invalid syntax
```

or

```
Traceback (most recent call last):
File "<string>", line 36, in <module>
File "<pip-setuptools-caller>", line 14, in <module>
File "/home/yourusername/.virtualenvs/myvirtualenv/lib/python3.7/site-packages/setuptools/__init__.py", line 18
  sys.path.extend(((vendor_path := os.path.join(os.path.dirname(os.path.dirname(__file__)), 'setuptools', '_vendor')) not in sys.path) * [vendor_path])  # fmt: skip
                                ^
SyntaxError: invalid syntax
```

or

```
File "/home/yourusername/.virtualenvs/myvirtualenv/lib/python3.7/site-packages/wheel/bdist_wheel.py", line 26, in <module>
  from ._bdist_wheel import bdist_wheel as bdist_wheel
File "/home/yourusername/.virtualenvs/myvirtualenv/lib/python3.7/site-packages/wheel/_bdist_wheel.py", line 21, in <module>
  from typing import TYPE_CHECKING, Callable, Iterable, Literal, Sequence, cast
ImportError: cannot import name 'Literal' from 'typing' (/usr/local/lib/python3.7/typing.py)
```