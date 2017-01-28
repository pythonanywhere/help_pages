
<!--
.. title: Using Selenium on PythonAnywhere
.. slug: selenium
.. date: 2017-01-28 13:35:28 UTC
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

In brief: PythonAnywhere, being a server environment, doesn't have a "display"
for selenium to open a browser onto.  But you can use a virtual display using a
tool called 
[Xvfb](http://en.wikipedia.org/wiki/Xvfb)
(or
[pyVirtualDisplay](http://pypi.python.org/pypi/PyVirtualDisplay)).
We currently only support the **Firefox** web browser.


## Using pyvirtualdisplay

From a Python script, there's a nice library called *pyvirtualdisplay*
that you can use to start up your Xvfb virtual display directly from
Python.

The main thing to remember is that you need to start it before you
invoke selenium, and that you need to be careful to tidy-up at the
end of your script, and shut down both selenium and your display.

* **NOTE**: *If you fail to close your display at the end of you script,
it will keep running in the background, eating up your CPU quota*


```python
from pyvirtualdisplay import Display
from selenium import webdriver

display = Display(visible=0, size=(800, 600))
display.start()

try:
    # we can now start Firefox and it will run inside the virtual display
    browser = webdriver.Firefox()
    browser.get('http://www.google.com')
    print browser.title #this should print "Google"

finally:
    # tidy up
    browser.quit()
    display.stop() # ignore any output from this.
```


## Using xvfb-run from the command-line (or for scheduled tasks)

If you're running your selenium scripts from the command line or for scheduled
tasks, there's an even easier way to start up your Xvfb display, `xvfb-run`:

Just precede your normal call to Python with `xvfb-run -a`:

    xvfb-run -a python3.5 /home/myusername/myfolder/myscript.py


## Firefox only

Due to some constraints imposed by our current sandboxing model, the
only browser we currently support is **Firefox v17.0**.  That is quite
an old version, but it works for most sites.

Chrome, PhantomJS, and others are not supported.


## Paid account may be required

Free users are currently restricted to a 
[whitelist](https://www.pythonanywhere.com/whitelist/)
of sites.  If you want to use Selenium to talk to a site
that's not on the list, you'll need to upgrade to a paid
account.


