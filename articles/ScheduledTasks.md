
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





##PythonAnywhere Scheduled Tasks


Go to the [Schedule](https://www.pythonanywhere.com/schedule/) tab on your [Dashboard](https://www.pythonanywhere.com/dashboard/). From there you can set up tasks to run daily at a particular time of day, or — for paying customers — hourly at a particular number of minutes past the hour. It's rather like a simple version of Unix's cron utility. 

If you specify a .py file to run, then it will normally be run using Python 2.7. If you want to use a different version of Python, put a "hash-bang" line at the start of the file — for example, starting your file with: 

       1 #!/usr/local/bin/python3.3



...will make it run using Python 3.3. 

You can also schedule non-Python files to be run, using the same hash-bang syntax to specify which interpreter to use — eg. #!/bin/bash. Non-Python files must be set up with execute permissions to be run from the scheduler. To do this, start a bash console and run chmod +x your-file. 


###Stopping scheduled tasks from running too often


If you want only one instance of a scheduled task to be running at any particular time, you can use a lock file to only run a script if it is not already running. See the [LongRunningTasks](/help/pages/LongRunningTasks) page. 
