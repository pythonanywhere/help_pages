<!--
.. title: How do I copy and paste from PythonAnywhere consoles?
.. slug: CopyAndPaste
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

In consoles, copy and paste should work pretty much like it does in any editor.
There's one exception: right now, it's not possible to copy/paste in Safari 10
on Macs.  Chrome and Firefox work fine on all operating systems that we've
tried.

To copy text, just select it and hit Ctrl-C (Command-C on a Mac). If the
highlight marking the selection disappears, that's normal and it means it's
worked.

To paste, use Ctrl-V (Command-V on a Mac).

If you're on Linux, you should also find that the middle-click paste buffer
works just fine.


##Multiple lines

Pasting multiple lines works fine in both Firefox and Chrome.

Copying multiple lines works fine in Chrome, but in Firefox it sometimes ends up
munging everything onto a single line when you paste it again.


##How to send ^C or ^V to the console

To send the actual Ctrl-C (^C) character to the console, just hit Control-C as
usual when you have nothing selected.  Ctrl-C will only do a copy action when
you have console text selected.

To send a Ctrl-V (^V), use Ctrl-Shift-V instead.
