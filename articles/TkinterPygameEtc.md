
<!--
.. title: Can I install/use Tkinter? (or Pygame, or QT, the turtle module, or other GUI libraries...)
.. slug: TkinterPygameEtc
.. date: 2018-02-12 11:35:28 UTC
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


# Can I install Tkinter? or Pygame?

Tkinter and Pygame are what we call "GUI toolkits", in the sense that they
help you to build Python apps that write graphics to your desktop screen (GUI
= graphical user interface).

The problem is that PythonAnywhere is a server-side, or "headless"
environment, which means it doesn't have access your GUI. When you run code on
PythonAnywhere, it runs on our servers, and it doesn't have any way to talk
directly to your local display and be able to display graphics on it.

The way we interact with your computer is using a web browser, either to
display an interactive console (so the output is all text-based), or to create
a web application (which uses HTML, CSS and JavaScript to display visual
information and create use interfaces)



# A package I'm installing needs Tkinter

What if a package you're installing needs Tkinter?  Something that doesn't
seem to be immediately related to GUI stuff?

Examples might include `Scipy/Numpy`, or `Matplotlib`

Perhaps you're seeing errors like this:

```
No module named _tkinter

No module named Tkinter

_tkinter.TclError: no display name and no $DISPLAY environment variable
```

The answer is that some packages *assume* that you're running in a GUI environment, even when you don't, strictly speaking, need one.  But there are usually workarounds for this.

See [this link for configuring matplotlib to not use tkinter](/pages/MatplotLibGraphs)


# What about turtle?

[Turtle](https://docs.python.org/3.6/library/turtle.html#module-turtle) is a
great fun graphics package, particularly for teaching programming by drawing
pictures, but unfortunately, for the reasons above, it won't work on
PythonAnywhere.

But we often recommend our friends at [trinket.io](https://trinket.io)
instead;  they've built a cool browser-based version of Python that
does support turtle.  It's great for beginners!

