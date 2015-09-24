
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

You **can** use a virtualenv for your IPython notebook. Follow the following steps:

1. From within your virtualenv, run

        :::bash
        ipython kernelspec install-self --user

    This will create a kernelspec for your virtualenv and tell you where it is:

        :::
        [InstallNativeKernelSpec] Installed kernelspec kernel in /home/username/.local/share/jupyter/kernels/kernel

2. Copy the new kernelspec somewhere useful:

        :::bash
        mkdir -p ~/.ipython/kernels
        mv ~/.local/share/jupyter/kernels/kernel ~/.ipython/kernels

3. You should now be able to see your kernel in the IPython notebook menu:
    `Kernel -> Change kernel` and be able so switch to it. IPython will remember
    which kernel to use for that notebook.


