
<!--
.. title: How to get the IP addresses of clients for your web app
.. slug: WebAppClientIPAddresses
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



Web apps on PythonAnywhere are load-balanced across a cluster of machines. This means that when you access the `remote_addr` field, which is where the client IP address normally goes, you'll get the internal IP address of the load-balancer. 

Our loadbalancer puts the real IP address that we received the request from into the X-Real-IP header, which you can access like this in Flask: 

        request.headers['X-Real-IP']


...and like this in Django: 

        request.META.get('HTTP_X_REAL_IP')


(Other web frameworks will be similar) 

We also pass along the `X-Forwarded-For` header, which contains a comma-separated list of IP addresses which *should* be a list of all proxies that have handled the client's request, with the client's IP address first and the one we received it from last. However, you should note that the data in that header isn't guaranteed -- malicious or broken clients or proxies anywhere between the client and your web app can put anything they want in there. The only thing we at PythonAnywhere can guarantee is the last item on the list, which will be the IP address of the machine our load-balancer received the request from. 
