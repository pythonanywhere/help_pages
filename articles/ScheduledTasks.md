
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


## Make sure you take account of the working directory

This can easily trip you up -- if you access another file in your script (that is, you
open it for reading or writing -- not if you `import` code from it), you need to
remember that the working directory of your script won't necessarily be the directory
where the script is running.  This is particularly prone to happening with SQLite
databases.

So, for example, if you have a script in
`/home/yourusername/some_directory/myscript.py`, and you normally run it by starting
bash and running this:

    cd ~/some_directory
    python3.6 myscript.py

...then you might have some hidden assumptions about the working directory in the
script, which would mean that it would work in when you run it like that from bash, but not when scheduled.
Perhaps you do something like this inside it:

    with open("my_data_file.txt", "r") as f:
        data = f.read()

This code will try to find the file `my_data_file.txt` inside the program's working
directory -- that is, the directory you used `cd` to get to when you ran it from
bash.  But in a scheduled task, the working directory might be different -- perhaps
it's just `/home/yourusername`.

The best solution to this is to be explicit about the directory containing the data file
when you `open` it in your script.  So, if the data file will *always* be in the same
directory as your script, then this code changes the above example to make that explicit:

    script_directory = os.path.dirname(os.path.abspath(__file__))
    data_file = os.path.join(script_directory, "my_data_file.txt")
    with open(data_file, "r") as f:
        data = f.read()



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

