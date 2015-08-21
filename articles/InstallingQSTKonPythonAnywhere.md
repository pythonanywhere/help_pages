
<!--
.. title: Installing QSToolKit on PythonAnywhere
.. slug: InstallingQSTKonPythonAnywhere
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



QSToolKit (QSTK) is a Python-based open source software framework designed to support portfolio construction and management. We are building the QSToolKit primarily for finance students, computing students, and quantitative analysts with programming experience. You should not expect to use it as a desktop app trading platform. Instead, think of it as a software infrastructure to support a workflow of modeling, testing and trading. 

You can install it on even a free PythonAnywhere account if you follow these instructions. All the below commands need to be entered into a Bash console. 

Step 1: Download QSTK using the command. 

    wget http://pypi.python.org/packages/source/Q/QSTK/QSTK-0.2.6.tar.gz 


Step 2: Extract the tarball using the command. 

    tar -xzvf QSTK-0.2.6.tar.gz 


Step 3: Move to the QSTK directory created now. 

    cd QSTK-0.2.6 


Step 4: Install QSTK once you have all the dependencies using the command. 

    python setup.py install --user 


Step 5: Testing the Installation was correct, please run the following commands. Please read the output to check if everything looks okay. 

    cd Examples
    python Validation.py
