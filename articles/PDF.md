
<!--
.. title: PDF and other document-wrangling tools on PythonAnywhere
.. date: 2016-05-13 11:35:28 UTC+01:00
.. slug: PDF
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

So you need to read or write PDFs?  Or maybe convert some HTML to PDF, or the
other way round?  Or read Word documents and extract text from them?  Hopefully
PythonAnywhere already has a tool preinstalled which can help.

This isn't a comprehensive guide, but here a few pointers:


## Python packages in our Batteries included:

Try doing a search for "pdf" on the [PythonAnywhere "Batteries Included" list of Python modules](https://www.pythonanywhere.com/batteries_included/)

A couple of tips:

* "pdftk" will only work in consoles, websites, always-on and scheduled tasks
  -- **not** from Jupyter notebooks or over SSH.

* We also have "weasyprint" installed, which is meant to have PDF capabilities


## Preinstalled binaries

Open a **Bash console** and run:

```
ls /usr/bin/*pdf*
```

You should see a whole bunch of potentially useful binaries which  you can call out to.

![](/pdf_tools_in_bash.png)

We also have **Abiword** installed, and it has some command-line options for converting word documents and others.  Check out this [article about using abiword at the command-line](http://www.aboutlinux.info/2005/08/use-abiword-to-convert-filetypes-on.html) for example.

If you find something useful, let us know!  [support@pythonanywhere.com](support@pythonanywhere.com)

