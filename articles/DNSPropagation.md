<!--
.. title: DNS Propagation
.. slug: DNSPropagation
.. date: 2019-06-13 17:43:00 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

# How DNS works

We have a blog post that describes a little about how DNS works
[here](https://blog.pythonanywhere.com/175/). It's a great place to start if
you're confused and don't know what's going on with your custom domain.

# How to check if your CNAME is properly set up

`dig` is a tool that can be used to talk to the DNS system to get information
about a domain name. We have it installed on PythonAnywhere, so you can run it
from a Bash console.

Here is a sample run and its output. We'll explain specific parts of it later.

    $ dig www.mydomain.com

    ; <<>> DiG 9.10.3-P4-Ubuntu <<>> www.mydomain.com
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 38590
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 4096
    ;; QUESTION SECTION:
    ;www.mydomain.com.        IN      A

    ;; ANSWER SECTION:
    www.mydomain.com. 60 IN   CNAME   webapp-12345.pythonanywhere.com.
    webapp-12345.pythonanywhere.com. 60    IN      A       35.173.69.207

    ;; Query time: 25 msec
    ;; SERVER: 127.0.0.1#53(127.0.0.1)
    ;; WHEN: Thu Jun 13 16:46:46 UTC 2019
    ;; MSG SIZE  rcvd: 113
    
    
The most important part of this is the piece labeled "ANSWER SECTION". This
shows how the DNS system is handling your domain. Since www.mydomain.com is a
correctly configured CNAME, it points to webapp-12345.pythonanywhere.com (the
first line of the section). Another important part of the "ANSWER SECTION" is
the number before the IN in the first line. It is the TTL (or Time-to-Live) of
the DNS record. Every DNS record has a TTL and that determines how long a
machine will cache a result for in seconds. In the example above it would
take at least 1 minute for a change to become visible. A TTL of 3600 would take
at least an hour.

Things that could be wrong:
* No "ANSWER SECTION": The domain does not exist in the DNS system.

# See also:

* [Custom Domains](/pages/CustomDomains/)
* [Naked Domains](/pages/NakedDomains/)
