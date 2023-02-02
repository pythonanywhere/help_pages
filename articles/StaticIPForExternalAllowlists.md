
<!--
.. title: Static IPs for external allowlists
.. slug: StaticIPForExternalAllowlists
.. date: 2017-09-08 18:44 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

## The issue

Some external services that you might want to connect to from your
PythonAnywhere code use IP allowlisting as a security measure.  For example,
if you have a Microsoft SQL Server on Azure, the normal configuration would
require that you enter the specific IP addresses of all machines that will
connect to it into the server's configuration.

This can cause problems when you try to connect from code running on
PythonAnywhere.  The actual IP address associated with running code is not fixed
-- your code can run on one of many different servers, with no fixed IP address.

## The solutions

### Using an HTTP proxy

Some companies can provide you with a private HTTP proxy with a static IP
address.  If all you need the static IP for is HTTP/HTTPS (and not, for example,
MySQL or ODBC), then this is a good and reasonably priced solution.
Here's one example: [BestProxyAndVPN](http://www.bestproxyandvpn.com).

Do note, though, that you'll need to configure your code to use the proxy.


### Statica

If you need to do non-HTTP requests, like ODBC or MySQL, another product that several customers
have used successfully [Statica](https://www.quotaguard.com/static-ip/) from
QuotaGuard.  They provide a kind of static-IP-as-a-service.  You rent the IP
address from them, and they provide a wrapper script that you can use to run
your code, which tunnels all access to external IPs from that code over a proxy
on that IP address.  One caveat if you're connecting to an MS SQL server
database: it appears to work well with pymssql, but not with pbodbc.

### Dynamically-changing your allowlisted IPs.

If you have some kind of API that allows you to allowlist specific IPs using a
side-channel (eg. if your database is on Amazon Web Services, then you can
use boto) then you could write a bit of code that gets the current IP where your
code is running, for example by using `requests` to access
[IPify](https://www.ipify.org/), and then allowlist the IP address dynamically
when your script starts up.


### The excessive allowlist

If all else fails, you can consider allowlisting all of Amazon's us-east-1
datacenter.   We really don't recommend this, though -- there are a *lot* of IP
addresses in their range, the servers could be rented out to hackers who are
trying to get into databases like yours, and anyway the list is subject to
change.   Still, if you decide to go for this option, here's a link to
[the IP ranges list](http://docs.aws.amazon.com/general/latest/gr/aws-ip-ranges.html).
