
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
        [InstallNativeKernelSpec] Installed kernelspec pythonX in /home/username/.local/share/jupyter/kernels/pythonX

    Where pythonX will match the version of Python in your virtualenv.

2. Copy the new kernelspec somewhere useful. Choose a `kernel_name` for your new
    kernel that is not `python2` or `python3` or one you've used before and then:

        :::bash
        mkdir -p ~/.ipython/kernels
        mv ~/.local/share/jupyter/kernels/pythonX ~/.ipython/kernels/<kernel_name>

3. If you want to change the name of the kernel that IPython shows you, you
    need to edit `~/.ipython/kernels/<kernel_name>/kernel.json` and change the
    JSON key called `display_name` to be a name that you like.

4. You should now be able to see your kernel in the IPython notebook menu:
    `Kernel -> Change kernel` and be able so switch to it. IPython will remember
    which kernel to use for that notebook from then on.



