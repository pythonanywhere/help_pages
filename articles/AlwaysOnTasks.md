<!--
.. title: Always-on tasks
.. slug: AlwaysOnTasks
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

> Warning -- this will only work in paid accounts

PythonAnywhere consoles can run for a long time, but we do occasionally have to
bounce our servers for maintenance. So, while you can usually keep a console
program running for a long time, you will occasionally find it resets itself.

If you want to keep a process running more or less permanently, or have it
restart automatically, and you have a **paid** account, the best solution is to use
what we call an "Always-on task".

To create one, go to the Tasks page, and look near the bottom -- you'll see a
table that looks like this:

<img alt="Always-on tasks table" src="/always-on-tasks-table.png" class="bordered-image">

To set up an always-on task, you just need to enter the full command to run
it into the input field -- for example,

    python3.10 /home/yourusername/a-directory/a-script.py

-- and click "Create".  It will appear in the table
below, with a state of "Starting".   You can refresh the table using the icon
near the top right, and you'll see that after a while it goes into a "Running"
state.

<img alt="Always-on tasks table" src="/always-on-task-running.png" class="bordered-image">

The program will continue to run, apart from during system maintenence.  If it
crashes for any reason -- even if there's a hardware failure on the machine where
it is running -- it will be automatically restarted.   Additionally, if you go
into the [tarpit](https://www.pythonanywhere.com/tarpit/) due to using up all of
your CPU seconds for the day, your task will be stopped and then restarted -- it
will then stop/start again when your CPU allowance is renewed the following day.

You can view the logs for the task with the first button in the "Actions"
column; the next button allows you to edit it, the next to pause (or unpause) it,
and the last one deletes it.


## Using virtualenvs in always-on tasks

If you want to use a virtualenv for your task, there are two possibilities:

### If you use virtualenvwrapper

Virtualenvwrapper is the system that provides the `mkvirtualenv` and `workon`
commands, so if you used the former to create your virtualenv and use the latter
when you want to do stuff using it, you can use them for your always-on task
too.   Let's say that your virtualenv is called `my-env` and you want to run the
script located at `/home/yourusername/something/script.py` -- the command to do
that in the always-on task "command" input would be this:

    workon my-env && python /home/yourusername/something/script.py


### If you use the venv module

If you use Python 3's built-in `venv` module -- that is, you did something like
this to create it:

    python3.10 -m venv my-env

...and you use this to activate it:

    source /home/yourusername/my-env/bin/activate

...then you can use the same command to activate it before running it.
Let's say that your virtualenv is called `my-env` and you want to run the
script located at `/home/yourusername/something/script.py` -- the command to do
that in the always-on task "command" input would be this:

    source /home/yourusername/my-env/bin/activate && python /home/yourusername/something/script.py


## Debugging always-on tasks

### The task gets stuck in "Starting"

If the task gets stuck in a "Starting" state, it is likely that it's crashing
as soon as it starts up.  The easiest way to work out why is to look at the task
log -- you can access that from the first button in the "Action" column.

If the error you see in the log is something like "permission denied", it's
probably because you've entered the path to a Python script in the "Command"
field instead of a command.   Remember, you need to specify

    python3.10 /path/to/script.py

...rather than

    /path/to/script.py

(Of course, if you're familiar with Unix, you can also `chmod` your script to
make it executable and add an appropriate hashbang.)

### Stuff that you print doesn't appear in the log

If you're printing stuff out in an always-on task, it might not appear in the
log in a timely fashion.  This is because when Python is sending print output
to something that is not a console -- for example, a file -- it keeps it in a
buffer, and only flushes it out to the real output when the buffer gets full.

This means that you'll get no output, and then a bunch of output in one go,
which isn't very helpful for debugging!

The solution is to force Python to flush the output buffer after each print.

In ***both Python 2 and 3*** you can launch the intepreter with an `-u` option:

    python3.10 -u /path/to/script.py

Alternatively, you can achieve that in code; in ***Python 3***, you simply add
`flush=True` to your `print` statements -- for example, you would replace

    print("Entering the main run loop")

...with this:

    print("Entering the main run loop", flush=True)

In ***Python 2***, it's a little more long-winded.  First, you need to add

    import sys

...at the start of any files where you're printing stuff, and then after each
print statement, add a new line with this:

    sys.stdout.flush()

### The log file doesn't update without refreshing the page in the browser

The log file for always-on tasks is just a static page, so you need to refresh
the page in order to see changes.   If you want to track things more dynamically,
you can tail the logfile in a Bash console.  The first step is to identify the
filename; you can do that by looking at the URL when you're viewing it.   For
example, if you see the URL

    https://www.pythonanywhere.com/user/aotdemouser/files/var/log/alwayson-log-837.log

...then the log file path is `/var/log/alwayson-log-837.log`.   To get a
dynamically updated view of what's in that log file, start a bash console and
run this command:

    tail -f /var/log/alwayson-log-837.log





