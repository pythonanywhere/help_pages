
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

1. Install ipython / jupter into your virtualenv

        :::bash
        workon my-virtualenv-name  # activate your virtualenv, if you haven't already
        pip install jupyter


2. Now run the kernel "self-install" script:

        :::bash
        ipython kernelspec install-self --user

  You can safely ignore all the DeprecrationWarnings.This will create a
  kernelspec for your virtualenv and tell you where it is:

        :::
        [InstallNativeKernelSpec] Installed kernelspec pythonX in /home/username/.local/share/jupyter/kernels/pythonX

  Where pythonX will match the version of Python in your virtualenv.


3. Copy the new kernelspec somewhere useful. Choose a `kernel_name` for your new
   kernel that is not `python2` or `python3` or one you've used before and then:

        :::bash
        mkdir -p ~/.ipython/kernels
        mv ~/.local/share/jupyter/kernels/pythonX ~/.ipython/kernels/<kernel_name>

4. Open up `~/.ipython/kernels/<kernel_name>/kernel.json`
  and change the name of the kernel that IPython shows you to something useful:
  change the JSON key called `display_name` to be a name that you like. Also
  double-check that the python interpreter in the `argv` entry is the one from
  your virtualenv.

        :::json
        {
          "display_name": "my-virtualenv kernel",
            "language": "python",
            "argv": [
              "/home/harry/.virtualenvs/my-virtualenv-name/bin/python2.7",
            "-m",
            "ipykernel",
            "-f",
            "{connection_file}"
            ]
        }


5. You should now be able to see your kernel in the IPython notebook menu:
   `Kernel -> Change kernel` and be able so switch to it (you may need to
   refresh the page before it appears in the list). IPython will remember
   which kernel to use for that notebook from then on.

