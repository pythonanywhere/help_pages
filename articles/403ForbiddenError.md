
<!--
.. title: 403 Forbidden error
.. slug: 403ForbiddenError
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->





##Why do I get a "403 Forbidden" or "[Errno 111] Connection refused" error when accessing a website from PythonAnywhere?


Free accounts' internet access goes via a proxy "whitelist". Here is the list of sites currently allowed: 

<https://www.pythonanywhere.com/whitelist/>

We operate this to prevent malicious users from using our site to hack into and spam other websites. **Paid-for accounts don't have this limitation**, because we can connect them to real people. Spammers and criminals prefer to be anonymous, so we figure they're unlikely to sign up for paid accounts here. 

We do allow access to that we think are useful to a large number of our users (all sites that host PyPI modules, for instance). If there is a site that you think we should add to the list of allowed sites, let us know using the "Send feedback" link above. Generally, it will need to be something with a public API. 


###[Errno 111] Connection refused


This error suggests that either the library you're using doesn't support using a proxy, or that it needs to be configured to use a proxy. Have a look at the docs for the library to determine which it is and consider raising an issue with the project about proxy support. 
