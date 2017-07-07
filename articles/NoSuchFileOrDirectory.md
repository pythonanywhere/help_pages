
<!--
.. title: No such file or Directory?
.. slug: NoSuchFileOrDirectory
.. date: 2016-12-17 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


# No such file or directory error?

Are you staring at an error that says:

```text
python: can't open file 'myfile.txt': [Errno 2] No such file or directory
```

Or maybe:

```text
IOError : No such file or directory
```


Are you saying something like: "Curses!  It works on my machine?"?


## Use absolute, not relative paths

One common reason for these kinds of errors is that your working directory settings might be different on PythonAnywhere from your own machine.

The fix is to use the full, absolute path, instead of a "relative" path.  So, eg:

    /home/yourusername/project-folder/myfile.txt

And not just *myfile.txt*.


## Tip: `__file__` for cross-platform scripts

"That's annoying!", I hear you exclaim, "my pythonanywhere username isn't the same as my local username.  and I'm on Windows maybe, so paths arent' the same!  Relative paths are so convenient! I don't want to run different code on my machine and on PA". A very reasonable grumble. But fear not:


```python
import os
THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
my_file = os.path.join(THIS_FOLDER, 'myfile.txt')
```

code like this, based on deriving the current path from Python's magic
`__file__` variable, will work both locally and on the server, both on
Windows and on Linux...


## Another possibility: case-sensitivity

One other thing that might be going on is that you're using the `wRoNG cAsINg`.
Casing doesn't matter on Windows but it does on Linux (and therefore, it
matters on PythonAnywhere).  So, be consistent with Uppercase and lowercase!

