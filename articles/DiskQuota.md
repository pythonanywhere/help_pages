
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


You can view your current disk quota and the amount used on the Files tab.

From time to time you'll find yourself looking at an error message in a console saying:

    Disk quota exceeded

And wonder why?  Where did all my space go?

(if you were running a script via Python, it might come in the form of an `OSError`)


## How to find what's using up all your space

Open up a **Bash console** and use the `du` ("disk-usage") to find out how much space
is being used in various places in your file storage:

    du -hs /tmp ~/.[!.]* ~/* | sort -h


## Cleaning up unused files

The files in `/tmp/` are the most common cause of an unexpected quota max-out.
It's usually safe to just delete them all:

    rm -rf /tmp/*

You can also clean up any old, unused virtualenvs with `rmvirtualenv my-old-venv-name`.

Other tips for freeing up disk space:

* Uninstall python packages you don't need anymore with `pipX.Y uninstall <package name> --user` (replacing the X.Y with the Python version you installed the packages for -- for example, 3.7)
* Delete your cache files with `rm -rf ~/.cache/*`
