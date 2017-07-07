
<!--
.. title: Installing virtualenvwrapper if you need to
.. slug: InstallingVirtualenvWrapper
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



*If you see a `command not found` error when trying to run `mkvirtualenv`, here's how to fix it.*

We install virtualenvwrapper for all new users by default. If you've got an older pythonanywhere account, it's easy to install virtualenvwrapper:

    :::bash
    echo '' >> ~/.bashrc && echo 'source virtualenvwrapper.sh' >> ~/.bashrc
    source virtualenvwrapper.sh


Once you've added the virtualenvwrapper command to your `.basrhc`, mkvirtualenv and all the other tools will be available in all your bash consoles.
