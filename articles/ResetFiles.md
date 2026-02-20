<!--
.. title: Reset all Files
.. slug: ResetFiles
.. date: 2026-02-20
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

If you want to reset your files to the way they were when you first created
your PythonAnywhere account, follow the instructions below.

## Delete all files

In a Bash console run:

```bash
rm -rf ~/*
rm -rf ~/.*
rm -rf /tmp/*
```

Once those have completed, start a new console and that will re-create the
default files.
