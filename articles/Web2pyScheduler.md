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

The [web2py scheduler](//web2py.com/books/default/chapter/29/4#web2py-Scheduler)
is a way to process asynchronous jobs from web2py.  You can run it in a paid
account without problems on PythonAnywhere; it's a bit less useful in a free
account.


## In a paid account

The way to get it running on PythonAnywhere in a paid account is to use an
[Always-on task](https://help.pythonanywhere.com/pages/AlwaysOnTasks).

Just create one on the "Tasks" page, with the following command:

```bash
cd ~; python web2py/web2py.py -K my_web2py_app_name
```

You should replace `my_web2py_app_name` with the actual app name, and if you've
installed Web2py in a directory different to `web2py` in your home directory,
you'll need to change that too.


## In a free account

Unfortunately there's no good way to make it work in a free account, because
you don't have access to always-on tasks.

