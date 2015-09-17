
<!--
.. title: File editor
.. slug: FileEditor
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->





##The file editor


PythonAnywhere's built-in file editor allows you to edit your files with syntax highlighting and, for Python, simple pyflakes-based error-checking.

When you want to run your code, you can use the "Save and run" button at the top right. This uses Python 2.7 by default; if you want to use a different version, you can use what's known as a "hashbang" in the very first line of your file. You start with the characters #!, and then the path to the interpreter you want, eg:

    :::python
    #!/usr/local/bin/python3.3
    print("Hello, World")
