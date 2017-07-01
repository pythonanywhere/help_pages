
<!--
.. title: Disk Quota Exceeded
.. slug: DiskQuotaExceeded
.. date: 2017-07-01 10:35:28 UTC+01:00
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

    du -hs ~/*    # this checks all the files and folders in your home folder
    du -hs /tmp   # this checks how much is being used in your temp folder
    du -hs ~/.virtualenvs/*   # virtualenvs can also use up lots of space


## Cleaning up unused files

The files in `/tmp/` are the most common cause of an unexpected quota max-out.
It's usually safe to just delete them all:

    rm -rf /tmp/*

You can also clean up any old, unused virtualenvs with `rmvirtualenv my-old-venv-name`.

