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

> Warning -- this will only work in paid accounts or free accounts created
> before 2026-01-15 (or 2026-01-08 in the EU system), see [this page](/pages/FreeAccountsFeatures) for more details.

## PythonAnywhere Scheduled Tasks

Scheduled tasks provide the ability to run your code periodically at a set time.
To set one up, go to the "Tasks" tab on your
[Dashboard](https://www.pythonanywhere.com/dashboard/). Using the form at the top
of the page:

* If you use a free account created before 2026-01-15 (or 2026-01-08 in the EU
  system), you can set up one task to run at a particular time every day.  The
  task can run for up to two hours.
* In all paid accounts, you can create up to 20 tasks, and they can either run at
  a particular time every day, or every hour at a particular number of minutes
  past the hour.  Each task can run for
  up to 12 hours.  (The limit of 20 tasks is "soft" -- if you need more, within reason,
  then you can contact us to get it raised for your account.)

The details of how to set a task up are below.


## Timing

Set the timing for the task using the fields at the start of the form.


## Specifying what to run: the simple version

The easiest way to specify the code to run is to enter the full path to your
Python script:

```
/home/myusername/myproject/myscript.py
```

If you do that, it will be run using your account's default Python version
(which you can specify on the "System image" tab of the "Account" page).


## More advanced use

If what you enter into the form is not a path to a Python script, the scheduler
will treat it as a Bash command to run.  This makes it possible to configure
things to run in a more detailed way:


### Using a different Python version

For example, if your default
Python version is 3.10, but you want to run the script with 3.9, then you could
just schedule this Bash command:

```
python3.9 /home/myusername/myproject/myscript.py
```

### Passing in command-line arguments

If your script takes command-line arguments, you can pass them in.  When doing
this, you'll need
to specify the Python command to use, so you could use an explicit version like
in the example above, but you can also specify the default Python version just
by using the `python` command:

```
python /home/myusername/myproject/myscript.py arg1 arg2 arg3
```


### Using a virtualenv

Bash commands can be comprised of several sub-commands, which can be run in
sequence by separating them with `&&`, so you could run a script using the
virtualenv called `myenv` like this:

```
source virtualenvwrapper.sh && workon myenv && python /home/myusername/myproject/myscript.py
```

Alternatively, you can use path to the `python` executable from the virtualenv.
To get the path, run `which python` command in a Bash console, *when the venv is
activated*.  Then use this path in the task's command, like:

```
/path/to/venv/bin/python /home/myusername/myproject/myscript.py
```

### Running non-Python scripts

If you have a script that is written in a different language to Python, you
can schedule it so long as Bash recognises it as executable.  There are two
things you need to do to achieve that:

1. Include a ['hashbang'](https://en.wikipedia.org/wiki/Shebang_(Unix)) at the
   start of the file to tell Bash which interpreter to us.  For example, if your script is written in Ruby,
   the very first line would be `#!/usr/bin/ruby`
2. Make sure that has execute permission.  You can use the Bash `chmod` command
   for that -- for example:

```
chmod +x /home/myusername/myproject/myscript.rb
```

(At a rather meta level, you could also schedule a Bash script that way by specifying
`/bin/bash` in the hashbang.)


## Common issues

### Make sure you take account of the working directory

This can easily trip you up -- if you access another file in your script (that is, you
open it for reading or writing -- not if you `import` code from it), you need to
remember that the working directory of your script won't necessarily be the directory
where the script is running.  This is particularly prone to happening with SQLite
databases.

So, for example, if you have a script in
`/home/yourusername/some_directory/myscript.py`, and you normally run it by starting
bash and running this:

    cd ~/some_directory
    python3.10 myscript.py

...then you might have some hidden assumptions about the working directory in the
script, which would mean that it would work when you run it like that from
bash, but not when scheduled. Perhaps you do something like this inside it:

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

(Don't forget to `import os` at the top of your file if you use that code!)

