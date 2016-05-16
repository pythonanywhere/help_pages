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

If you want to run a scheduled task in a virtualenv, specify the full path to the virtualenv python inside your task's command-line.

So, eg, instead of:

```
/home/myusername/myproject/mytask.py
```

Use

```
/home/myusername/.virtualenvs/myvenv/bin/python /home/myusername/myproject/mytask.py
```

If you need to make sure there's only one copy of your task running at a time, see the [long-running tasks article](/pages/LongRunningTasks/)

