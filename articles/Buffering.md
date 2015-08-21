
<!--
.. title: Buffering
.. slug: Buffering
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->




Some background knowledge: 

When a request is sent from your browser to your webapp on PythonAnywhere, it actually goes to a loadbalancer, which receives and processes your request using a nginx reverse proxy, which figures out and forwards the request along to one of the servers that your webapp(s) is running on. 

That server receives and processes the request using its own nginx reverse proxy and passes it to uWSGI. Within uWSGI, since there are multiple webapps, there is the uWSGI emperor which passes the request over to the uWSGI vassal, which then gives it to one of many worker, which is running a special PythonAnywhere wrapper subprocess. 

This is where we do stuff like try to catch errors for you that say setting django or flask debug=True still cannot catch, put it nicely into your error log, and show you an error page that tells you to go read your logs etc. Only then does it get to your actual code. 

**tl;dr: your traffic goes through some jumps behind the scene and nginx buffers the response unless specified otherwise.**

To get everything to flush, 

1. give your responses headers `headers['X-Accel-Buffering'] = 'no'`

2. have a `'\n'` at the end of the string you are yielding because python also buffers till end of line. 
