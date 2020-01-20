
<!--
.. title: Using a virtualenv in an IPython notebook
.. slug: IPythonNotebookVirtualenvs
.. date: 2015-09-24 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

<!--
NOTE: this help page should mirror FT #5065.  If you change it, change the test.
-->


You can use a [virtualenv](/pages/VirtualenvsExplained) for your IPython notebook.
Follow these steps:

1. For the version of Python that you want in your virtualenv, get the versions
   of the following packages that are installed by default:
    * tornado
    * ipykernel
    * prompt-toolkit
        
    so for example, if you want to use Python 3.6, run the following and note the versions:

        :::bash
        pip3.6 show tornado
        pip3.6 show ipykernel
        pip3.6 show prompt-toolkit

2. Install the packages with the appropriate versions into your virtualenv:

        :::bash
        workon my-virtualenv-name  # activate your virtualenv, if you haven't already
        pip install tornado==<tornado version from above>
        pip install ipykernel==<ipykernel version from above>
        pip install prompt-toolkit==<prompt-toolkit version from above>
        
    so, for example, if the versions shown were 6.0.3, 5.1.3 and 2.0.10 respectively, run:
    
        :::bash
        workon my-virtualenv-name
        pip install tornado==6.0.3
        pip install ipykernel==5.1.3
        pip install prompt-toolkit==2.0.10
    
    **Note: ** The order in which the packages are installed is important. Make
    sure you install prompt-toolkit last.

3. You should now be able to see your kernel in the IPython notebook menu:
   `Kernel -> Change kernel` and be able to switch to it (you may need to
   refresh the page before it appears in the list). IPython will remember
   which kernel to use for that notebook from then on.
        
**Note: ** For this to work, your virtualenv must be in the standard
virtualenv directory. That is ~/.virtualenvs 
