<!--
.. title: Conda
.. slug: conda
.. date: 2022-10-06 01:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

# Disclaimer

**Warning: Although it is possible to use `conda` on PythonAnywhere, it's still
an experimental feature.**

Conda is only available in the "haggis" and "innit" system images


# Creating the `.condarc` (optional)

We recommend creating a `conda` configuration file at `~/.condarc` with some
basic setup:

```
# contents of ~/.condarc

auto_activate_base: false
notify_outdated_conda: false
```

This will do 2 things:

  * prevent the automatic activation of the `conda` base environment each time
    you start a Bash console.
  * turn off upgrade notifications, because it is not possible for users
    to upgrade `conda` and attempts to do that will lead to confusing errors.


# Initializing conda

To initialize `conda`, in a Bash console, run:

```
/opt/conda/bin/conda init
```

You will need to start a new Bash console for this to have effect.


# Creating an environment

With conda initialized, you should have a `conda` command available in a Bash
console.  To confirm that it's working, just run it.

As the `base` `conda` environment is read only, you need to create your own
environment to be able to install packages into it.  For example, to create a new
environment called `my_env` with `requests` installed, run:

```
conda create --name my_env requests
```

After a successful run (it might take a while!), you should see an output with
further instructions:

```
# To activate this environment, use
#
#     $ conda activate my_env
#
# To deactivate an active environment, use
#
#     $ conda deactivate
```

By default, environments will be created in `~/.conda/envs/`.


# Caveats and limitations

## Disk quota limitations

Conda environments take a lot of disk space, so creating a new conda environment
may take a substantial part of your disk quota, so it may require a paid account.

A tip: if you want to check how much disk space is used by your `conda`
environments and packages, run `du -hs ~/.conda`.  To learn more about disk
space limitations, read [this help page](/pages/DiskQuota).

To check existing environments, run `conda env list` and to remove an
environment with its packages, run `conda env remove --name my_env` (where
"my_env" is a name of a previously created environment).

## No support for web apps

Currently you will not be able to run a web app in a `conda` environment.
