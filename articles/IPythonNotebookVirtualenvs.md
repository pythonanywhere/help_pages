
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

# Using a virtualenv in an IPython notebook

You can use a [virtualenv](/pages/VirtualenvsExplained) for your IPython notebook. Follow the following steps:

1. Install the ipython kernel module into your virtualenv

        :::bash
        workon my-virtualenv-name  # activate your virtualenv, if you haven't already
        pip install ipykernel


2. Now run the kernel "self-install" script:

        :::bash
        python -m ipykernel install --user --name=my-virtualenv-name

    Replacing the `--name` parameter as appropriate.

3. You should now be able to see your kernel in the IPython notebook menu:
   `Kernel -> Change kernel` and be able so switch to it (you may need to
   refresh the page before it appears in the list). IPython will remember
   which kernel to use for that notebook from then on.

