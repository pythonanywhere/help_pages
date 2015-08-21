
<!--
.. title: Embeddable consoles
.. slug: EmbeddedConsoles
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



Want to have a live Python console on your website, like on the [python.org](https://www.python.org) front page? No problem. 

Use an iframe, like this: 

    <iframe style="width: 640; height: 480; border: none;" name="embedded_python_anywhere" src="http://www.pythonanywhere.com/embedded3/"></iframe>


Or use this link for python 2: 

    <iframe style="width: 640; height: 480; border: none;" name="embedded_python_anywhere2" src="http://www.pythonanywhere.com/embedded/"></iframe>


This will spawn a new "anonymous" console for each visitor to your site (unless they have a pythonanywhere account already, and are signed into it, in which case the console will actually run inside their account). 
