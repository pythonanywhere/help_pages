
<!--
.. title: Using a virtualenv in an IPython notebook
.. slug: IPythonNotebookVirtualenvs
.. date: 2015-09-24 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

<!--
NOTE: this help page should mirror FT #5065.  If you change it, change the test.
-->


You can use a [virtualenv](/pages/VirtualenvsExplained) for your IPython notebook.
Follow these steps:

1. Install the ipython kernel module into your virtualenv:

        :::bash
        workon my-virtualenv-name  # activate your virtualenv, if you haven't already
        pip install tornado==4.5.3
        pip install ipykernel==4.8.2

2. You should now be able to see your kernel in the IPython notebook menu:
   `Kernel -> Change kernel` and be able to switch to it (you may need to
   refresh the page before it appears in the list). IPython will remember
   which kernel to use for that notebook from then on.
