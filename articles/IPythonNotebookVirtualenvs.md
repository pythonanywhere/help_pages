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

**Note: these instructions will only work if you're on our most recent [system image](/pages/ChangingSystemImage)**

You can use a [virtualenv](/pages/VirtualenvsExplained) for your IPython notebook.
Follow these steps:

1. For the version of Python that you want in your virtualenv, get the version
   of the jupyter package

    so for example, if you want to use Python 3.6, run the following and note the version:

        :::bash
        pip3.6 show jupyter

2. Install the package with the appropriate version into your virtualenv:

        :::bash
        workon my-virtualenv-name  # activate your virtualenv, if you haven't already
        pip install jupyter==<jupyter version from above>

3. If you're on the Haggis system image, run the following:

        :::bash
        ipython kernel install --name "venv-name" --user

    The name that you give to the kernel can be anything as long as it only
    contains ASCII letters and numbers and these separators: - . _ (hyphen,
    period, and underscore)


4. You should now be able to see your kernel in the IPython notebook menu:
   `Kernel -> Change kernel` and be able to switch to it (you may need to
   refresh the page before it appears in the list). IPython will remember
   which kernel to use for that notebook from then on.

**Note: ** For this to work, your virtualenv must be in the standard
virtualenv directory. That is ~/.virtualenvs
