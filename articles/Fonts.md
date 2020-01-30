
<!--
.. title: Fonts
.. slug: Fonts
.. date: 2020-01-30 15:35:28 UTC+00:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->





## Fonts in rendered output

Some packages (like matplotlib and bokeh, for example) use the fonts that are
installed on the operating system to render their output and so there may be
cases where the fonts in your output do not look the way you expect.

There are already a large number of fonts installed on PythonAnywhere. You can
see a list of them by running

    :::bash
    fc-list : family style spacing
    
    
in a Bash console. The name in front of the colon on each line is the name that
you can use to load and use the font in your program.

If you want to use a particular font or a custom one, you can install TrueType
fonts for your account.


## Installing TrueType fonts

* Copy the *.ttf files that define the font into ~/.fonts
* Run

        :::bash
        fc-cache -f -v
    
    
    in a Bash console
    
* The new font should be available so that you can use it.
    

