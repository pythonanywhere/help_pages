
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





###Can I use matplotlib to generate graphs from my data?


Yes you can, and your graphs will be saved as an image file in your directory. 

The block of code below gives you an example of how you would do this: 

       1     import matplotlib
       2     import matplotlib.pyplot as plt
       3 
       4     fig = plt.figure()
       5     ax = fig.add_subplot(111)
       6     ax.plot(range(100))
       7 
       8     fig.savefig('graph.png')



`graph.png` will then show up in your home directory. Simply put, wherever you might normally use `plt.show()` to display your graph on screen you should use `fig.savefig('your_graph.png')` to save it as an image file instead. 

Once you've done that, you can view the graph from your browser using a URL like this: `http://www.pythonanywhere.com/user/your-username/files/home/your-username/graph.png`
