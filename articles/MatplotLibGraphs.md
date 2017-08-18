
<!--
.. title: MatplotLib graphs
.. slug: MatplotLibGraphs
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->





## Can I use matplotlib to generate graphs from my data?


Yes you can, and your graphs will be saved as an image file in your directory.

The block of code below gives you an example of how you would do this:

    :::python
    import matplotlib
    matplotlib.use("Agg")
    import matplotlib.pyplot as plt

    fig = plt.figure()
    ax = fig.add_subplot(111)
    ax.plot(range(100))

    fig.savefig("graph.png")



`graph.png` will then show up in your home directory. Simply put, wherever you
might normally use `plt.show()` to display your graph on screen you should use
`fig.savefig('your_graph.png')` to save it as an image file instead.


Once you've done that, you can view the graph from your browser using a URL
like this:
`http://www.pythonanywhere.com/user/your-username/files/home/your-username/graph.png`


## What do do if you're seeing errors about Tkinter

Make sure to include the `matplotlib.use("Agg")` line from the example above --
that's the bit that sets the "backend" that matplotlib uses to draw graphics.
Tkinter is the default, but it won't work on PythonAnywhere.  Agg works fine...

