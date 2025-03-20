<!--
.. title: What is a virtualenv, and why would I use one?
.. slug: VirtualenvsExplained
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

A virtualenv is way to create an isolated Python environment with specific installed
packages inside it.

When you run your code normally -- as a website, a scheduled
task, or in any other way -- it doesn't run in a virtualenv, but in the
*system environment*.

But with appropriate setup, it can run in a virtualenv.  When you do that, the
running code will only see the specific packages that are installed in that env.

This means that you can have different virtualenvs for different uses.  For example,
if you had two websites, they could each use a different virtualenv so that they
could use different packages.  If one website needed Flask version
3.10.0, and another needed version 4.0.0, you could run both inside the same
PythonAnywhere account by making them use different virtualenvs with the appropriate
versions installed.

You don't need to use virtualenvs to run your code on PythonAnywhere -- indeed,
when you're getting started, it's best not to, and to use the system environment instead.  We have a lot of
[useful packages pre-installed](https://www.pythonanywhere.com/batteries_included/),
so you can just use them.  Doing that has the advantage that unlike virtualenvs,
the packages in the system environment don't use up any of your disk space.

But if you start needed extra modules that are not pre-installed, or if you want
to manage which specific versions of different packages you're using, they're a good idea.

Here's how to use them in various parts of PythonAnywhere:

  * Websites:
    * [General advice for virtualenvs in websites](/pages/Virtualenvs)
    * [Virtualenvs for Django specifically](/pages/VirtualEnvForNewerDjango)
  * [How to use them in an Jupyter Notebook](/pages/IPythonNotebookVirtualenvs)
  * [Using them in always-on tasks](/pages/AlwaysOnTasks#using-virtualenvs-in-always-on-tasks)
  * [Using them in scheduled tasks](/pages/ScheduledTasks#using-a-virtualenv)
  * [Specifying a virtualenv to be used when running from the editor](/pages/SaveAndRunPythonVersion)
