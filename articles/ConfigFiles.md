
<!--
.. title: Config files (dotfiles)
.. slug: ConfigFiles
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

## What are config (dotfiles)?

In a Linux environment, config files (often called dotfiles because they
begin with a dot, like `.bashrc`) are user-specific files that configure
various aspects of the system and applications (such as `vim` or
`ipython`). They customize shell behavior (e.g., Bash), environment
variables, aliases, and application settings, making it easy to personalize
the user experience across sessions.

Dotfiles are stored in your home directory (`/home/<username>`) and are
read by the system or programs during startup to automatically apply your
preferences.

By default, we place the following config files in your home directory:

```shell
.bashrc
.gitconfig
.profile
.vimrc
```

You’ll also find a `.ipython` directory that stores configuration for the
IPython shell, which you can use from a Bash console.

In addition, there’s a `.pythonstartup.py` script that is used to run your
Python code from the in-browser editor. We recommend not modifying this
file unless you know exactly what you're doing, as it may affect how your
scripts are executed.

What are these files for?

- `.bashrc` – Executed when you start a new Bash console. Commonly used for
  defining aliases, functions, and other shell customizations.
- `.profile` – Executed when the system runs your code (e.g., in a
  scheduled task). It's mainly used when a non-Bash shell is the
  default. If `.bash_profile` is also present, it typically overrides
  .profile.
- `.gitconfig` – Stores your global Git configuration (e.g., username,
  email, aliases).
- `.vimrc` – Configuration for the Vim editor, available in your account
  via Bash console.


## Can I edit the config files?

Yes, you can edit your dotfiles using the in-browser editor or from the
Bash shell.

**However**, as a rule of thumb, you should **not** modify, delete, or add
dotfiles unless you’re confident about what you’re doing. If you'd like to
experiment, we strongly recommend creating a backup of each file
first. That way, you can roll back your changes if something stops working.


## Frequent issues 

A common and tricky issue occurs when users create a custom
`~/.bash_profile`, which by default overrides `~/.profile`.

Our default `~/.profile` contains a single line:

```shell
source ~/.bashrc
```

This line ensures that your `.bashrc` is loaded when the system starts a
shell to run your code (e.g., in scheduled tasks).

Inside `.bashrc`, you'll find another important line:

```shell
source /etc/bashrc
```

This loads a non-editable system-wide config file (`/etc/bashrc`) which
includes critical environment settings, such as the `PATH`. Without these
settings, your shell environment might fail to locate key executables like
`python3.12`, causing your scripts to fail with errors such as `command not
found`.

If your custom `~/.bash_profile` does not include a call to source `~/.bashrc`,
it can break your environment and prevent scheduled tasks from running
correctly.
