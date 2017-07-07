
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

    :::python
    import logging
    import socket
    import sys
    from my_module import my_long_running_process

    lock_socket = None  # we want to keep the socket open until the very end of
                        # our script so we use a global variable to avoid going
                        # out of scope and being garbage-collected

    def is_lock_free():
        global lock_socket
        lock_socket = socket.socket(socket.AF_UNIX, socket.SOCK_DGRAM)
        try:
            lock_id = "my-username.my-task-name"   # this should be unique. using your username as a prefix is a convention
            lock_socket.bind('\0' + lock_id)
            logging.debug("Acquired lock %r" % (lock_id,))
            return True
        except socket.error:
            # socket already locked, task must already be running
            logging.info("Failed to acquire lock %r" % (lock_id,))
            return False

    if not is_lock_free():
        sys.exit()

    my_long_running_process()


**Note** -- due to some scaling issues, we're currently having to limit the max duration of scheduled tasks.  Free users are limited to one hour, and paying users are limited to 6 hours.  So this means, if you are a paying user, you should use an hourly task.  For free users, unfortunately, this solution currently won't work.  We are working on it!

