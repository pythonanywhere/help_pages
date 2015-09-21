
<!--
.. title: How to run the web2py scheduler on PythonAnywhere
.. slug: Web2pyScheduler
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



The [web2py scheduler](//web2py.com/book/default/chapter/04#Scheduler-%28experimental%29)
is a way to process asynchronous jobs from web2py. The way to get it running on
PythonAnywhere is to use a **Scheduled Task**, which runs once a day.

This is the usual [long-running tasks hack](/pages/LongRunningTasks) on
PythonAnywhere -- because we can't guarantee to keep a process running forever,
the workaround is to have a scheduled task that runs periodically, and restarts
the task if it's died, or just quits if it sees it's already running.

Here's some example code -- you'll need to adapt this to match your own web2py
apps' names:

    :::python
    #/usr/bin/env python
    import os
    import socket
    import subprocess
    import sys
    filename = os.path.abspath(__file__)  # we use this to generate a unique socket name

    try:
        # we use a local socket as a lock.
        # it can only be bound once, and will be released if the process dies
        socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM).bind('\0' + filename)
    except socket.error:
        print("Failed to acquire lock, task must already be running")
        sys.exit()

    subprocess.call(["python", "web2py/web2py.py", "-K", "my_web2py_app_name"])



Save that code to a file in your home folder, it doesn't matter where, make
it executable using a bash console like this:

    :::bash
    chmod +x /path/to/your.file


...and then
set it to run as a scheduled task -- once a day, or even once an hour if you
have a paying account. For example, if you save it to
`/home/yourusername/run-web2py-scheduler-for-myapp.py`, you can just enter that
full path as the scheduled task.
