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

## Make sure that you went through Custom Domains help page

If you have trouble coupling your domain with website on PythonAnywhere be sure
you went through our [Custom Domains help page](/pages/CustomDomains/). If you
still experience problems we prepared a set of solutions for the most common ones
and a background information to help you understand how DNS works.

## yourdomain.com is not www.yourdomain.com

You need to give special treatment to your naked domain. It is handled
differently then subdomains. As it is a common source of confusion we have a
[separate help page](/pages/NakedDomains/) dedicated to that problem.

## We were unable to find a CNAME for your domain.

If you see "We were unable to find a CNAME for your domain." message but your
website loads normally it usually mean that your name server provider (usually
it happens for Cloudflare using [CNAME Flattening](/pages/NakedDomains/)) sets redirection in a way that
makes us unable to identify a CNAME. It's fine.

## How to check if your CNAME is properly set up

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

## How DNS works

We have also a [a seperate help page](/pages/DNSPrimer/) that describes a little
about how DNS works. It's a great place to start if you're confused and don't
understand what's really going on with your custom domain.

## Still having trouble?

If you want to [contact us](mailto:support@pythonanywhere.com) remember to attach a screenshots of your DNS configuration.

