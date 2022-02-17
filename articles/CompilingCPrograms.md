<!--
.. title: Compiling C Programs
.. slug: CompilingCPrograms
.. date: 2022-02-17
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

You can't use `apt` or similar package managers to install programs on
PythonAnywhere, because you do not have root access to the machine where your
code runs -- in particular, you can't use the `sudo` command.

However, if you want to install a Linux tool that is written in C into
your home directory, it's often possible.

Specifically, if the tool that you want to install has instructions on how to
compile it from source, and the steps documented by the tool to do that are:

* Get the source (either by downloading it from a link and using `tar` to unpack it, or by using `git clone`
* `cd` into the source directory
* Run `./configure`
* Run `make`
* Run `sudo make install`

...then you can often get it to work by following those steps, but adding
the flag `--prefix=/home/$HOME/.local` to the `./configure` line, and then missing
out the `sudo` on the install line.
