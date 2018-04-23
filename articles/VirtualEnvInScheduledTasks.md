<!--
.. title: Using a virtualenv in a scheduled task
.. slug: VirtualEnvInScheduledTasks
.. date: 2016-05-16 11:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

## The simple case: without environment variables

If you want to run a scheduled task in a
[virtualenv](/pages/VirtualenvsExplained), and you're not using the virtualenvwrapper postactivate
script to set environment variables, you just need to specify the full path to
the virtualenv python inside your task's command-line.

So, eg, instead of:

```
/home/myusername/myproject/mytask.py
```

You would use

```
/home/myusername/.virtualenvs/myvenv/bin/python /home/myusername/myproject/mytask.py
```

If you need to make sure there's only one copy of your task running at a time,
see the [long-running tasks article](/pages/LongRunningTasks/)


## The more complicated case, with environment variables

If you *are* using the postactivate script to set environment variables, the
command is a little more complicated.   Instead of `/home/myusername/myproject/mytask.py`, you
need to use a command like this:

    source virtualenvwrapper.sh && workon myvirtualenv && python /home/myusername/myproject/mytask.py
