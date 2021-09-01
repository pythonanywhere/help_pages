<!--
.. title: Disk Quota
.. slug: DiskQuota
.. date: 2018-07-13
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Your account on PythonAnywhere has a specific amount of storage space available
for saving files -- Python scripts, images, data, or anything else you want.
Free accounts get a disk quota of 512MiB; paid accounts get more, the exact
amount depending on what kind of account you have.

You can view your current disk quota and the amount used on the dashboard and on
the "Files" page.

## Running out of disk space

If you run low on disk space, the text on the "Files" page showing how much you
are using will turn red.

If you run out completely, it will show that fact there, and also when your code
tries to write to disk you will get an error message -- something like this:

    Disk quota exceeded

(If you were running a script via Python, it might come in the form of an
`OSError`, but will include that message.)


## How to find what's using up all your space

Open up a **Bash console** and use the `du` ("disk-usage") to find out how much space
is being used in various places in your file storage:

    du -hs /tmp ~/.[!.]* ~/* | sort -h


## Cleaning up unused files

The files in `/tmp/` are the most common cause of an unexpected quota max-out.
It's usually safe to just delete them all:

    rm -rf /tmp/* /tmp/.*

You can also clean up any old, unused virtualenvs with `rmvirtualenv my-old-venv-name`.

Other tips for freeing up disk space:

* Uninstall python packages you don't need anymore with `pipX.Y uninstall <package name> --user` (replacing the X.Y with the Python version you installed the packages for -- for example, 3.8)
* Delete your cache files with `rm -rf ~/.cache/*`
