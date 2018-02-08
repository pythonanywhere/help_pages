
<!--
.. title: Scheduled tasks
.. slug: ScheduledTasks
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



## PythonAnywhere Scheduled Tasks


Go to the Tasks tab on your
[Dashboard](https://www.pythonanywhere.com/dashboard/). From there you can set
up tasks to run daily at a particular time of day, or — for paying customers —
hourly at a particular number of minutes past the hour. It's rather like a
simple version of Unix's cron utility.


## Scheduling Python scripts to run 

You can just enter the full path to your file, eg

```
/home/myusername/myproject/myscript.py
```

And it will be run using the scheduler's default Python version (currrently Python 2.7)


## Specifying another Python version

If you want to use a different version of Python, put a "hashbang" line at the
start of your file — for example, starting your file with:

    :::bash
    #!/usr/bin/python3.6

...will make it run using Python 3.6.  (the advantage of
doing it this way is that the "run" button in the editor
also takes into account hashbangs).


Alternatively, you can explicitly specify the python executable to use in the scheduled tasks page, so, instead of


```
/home/myusername/myproject/myscript.py
```

Use


```
python3.6 /home/myusername/myproject/myscript.py
```



## Using a virtualenv

See the article called [How do I run a scheduled task inside a virtualenv](/pages/VirtualEnvInScheduledTasks)



## Non-Python scripts

Non-Python scripts will have to have executable permissions set; to do this, run the following
command from a bash console

    :::bash
    chmod +x /path/to/your.file

Then use the same hash-bang syntax to specify which interpreter to 
use — eg. #!/bin/bash. 



## Stopping scheduled tasks from running too often

If you want only one instance of a scheduled task to be running at any
particular time, you can use a lock file to only run a script if it is not
already running. See the [LongRunningTasks](/pages/LongRunningTasks) page.

