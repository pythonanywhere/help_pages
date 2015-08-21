
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



The [web2py scheduler](//web2py.com/book/default/chapter/04#Scheduler-%28experimental%29) is a way to process asynchronous jobs from web2py. The way to get it running on PythonAnywhere is to use a **Scheduled Task**, which runs once a day. 

*(This is the usual [long-running tasks hack](/help/pages/LongRunningTasks) on PythonAnywhere -- because we can't guarantee to keep a process running forever, the workaround is to have a scheduled task that runs periodically, and restarts the task if it's died, or just quits if it sees it's already running.)*

Here's some example code -- you'll need to adapt this to match your own web2py apps' names: 

       1 #/usr/bin/env python
       2 import os
       3 import socket
       4 import subprocess
       5 import sys
       6 filename = os.path.abspath(__file__)  # we use this to generate a unique socket name
       7 
       8 try:
       9     # we use a local socket as a lock. 
      10     # it can only be bound once, and will be released if the process dies
      11     socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM).bind('\0' + filename)
      12 except socket.error:
      13     print("Failed to acquire lock, task must already be running")
      14     sys.exit()
      15 
      16 subprocess.call(["python", "web2py/web2py.py", "-K", "my_web2py_app_name"])



Save that code to a file in your home folder, it doesn't matter where, and then set it to run as a scheduled task -- once a day, or even once an hour if you have a paying account. For example, if you save it to */home/yourusername/run-web2py-scheduler-for-myapp.py*, you can just enter that full path as the scheduled task. 
