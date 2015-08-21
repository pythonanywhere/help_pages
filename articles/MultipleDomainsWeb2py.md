
<!--
.. title: Multiple domains with Web2py
.. slug: MultipleDomainsWeb2py
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->




There is some potential for confusion because there are slightly different definitions of "app" here. 

  * For PythonAnywhere, an "app" means a Python WSGI application that works for one domain 
  * For Web2py, an "app" is an semi-independent module that lives inside a single [Web2Py](//www.web2py.com/) WSGI host. 

So, in the web2py world, one web2py folder can contain multiple applications, and each of them might be a totally different website for a different domain. 

In PythonAnywhere, we usually expect your different domains to be different apps that live in different folders. 

But it is possible to set up multiple domains on PythonAnywhere, which all talk to a single web2py installation, which then has multiple web2py applications for each domain. Then you can set up all the web2py apps you want via the web2py interface. 

Start by setting up one domain with the web2py wizard on the PythonAnywhere web tab. 

Then, for each additional domain name, you need to set up another PythonAnywhere web app from the web tab. This time though, you should choose "manual configuration". Then, go and edit your WSGI file. You should make it into a copy of the WSGI file for the first web2py application, so that both domains point at the same web2py installation. Then the web2py routes.py should work. 
