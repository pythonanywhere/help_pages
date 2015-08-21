
<!--
.. title: Long running tasks
.. slug: LongRunningTasks
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->




PythonAnywhere consoles can run for a long time, but we do occasionally have to bounce our servers for maintenance. So, while you can usually keep a console program running for a long time, you will occasionally find it resets itself. 

If you want to keep a process running more or less permanently, or have it restart automatically, the best solution is to use a scheduled task, which runs once an hour or once a day, and either (re)launches the job if it's not running, or just quits if it is already running. 

You'll need to start by making sure your job is resilient to being terminated unexpectedly -- make it save its data every so often, and make sure it is able to resume work wherever it is left off. 

Then you just need some way of checking whether the process is running. We often use a socket for these cases. Your process opens the socket while it runs, and if it ever exits, it will release it automatically. Then it's easy to check on, with code like this: 

       1     import logging
       2     import socket
       3     import sys
       4     from my_module import my_long_running_process
       5 
       6     lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
       7     try:
       8         lock_id = "my-username.my-task-name"   # this should be unique. using your username as a prefix is a convention
       9         lock_socket.bind('\0' + lock_id)
      10         logging.debug("Acquired lock %r" % (lock_id,))
      11     except socket.error:
      12         # socket already locked, task must already be running
      13         logging.info("Failed to acquire lock %r" % (lock_id,))
      14         sys.exit()
      15     
      16     my_long_running_process()
