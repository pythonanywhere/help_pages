<!--
.. title: Troubleshooting DNS
.. slug: TroubleshootingDNS
.. date: 2019-06-13 17:43:00 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

If you're having trouble connecting your domain with your website on PythonAnywhere,
make sure you have been through our [Custom Domains help page](/pages/CustomDomains/).
If after that you are still experiencing problems, we've prepared a set of
solutions for the most common ones and some background information to help you
understand how DNS works.

## `yourdomain.com` is not `www.yourdomain.com`

This is the cause of about 80% of problems with DNS setup :-)

Technically speaking those two addresses are completely different things -- you
could have one website on one, and a completely different one on the other.  You should
set up your website on `www.yourdomain.com` and then set up `yourdomain.com` to
redirect to `www.yourdomain.com` as a separate step.

The name of your website on the "Web" page inside PythonAnywhere needs to be
an exact match for the address that people use to visit it, so in all but the most
unusual cases it *should* include the `www`.  So if right now you just have
`yourdomain.com` there instead of `www.yourdomain.com`, then use the "pencil" icon next
to the name to edit it, add the missing `www.`, and your site may start working
right away!

For more details about `yourdomain.com` vs `www.yourdomain.com`, check out our
[separate help page about "naked" domains](/pages/NakedDomains/).


## "We were unable to find a CNAME for your domain" -- but the site works!

If you see "We were unable to find a CNAME for your domain." message but your
website loads normally and appears to be running the code you have configured on
PythonAnywhere, it usually mean that your name server provider (usually
it happens for Cloudflare using CNAME Flattening) sets redirection in a way that
makes us unable to identify a CNAME. It's fine.

But if you're not seeing your website when you visit it, read on...


## How to check if your CNAME is properly set up

`dig` is a tool that can be used to talk to the DNS system to get information
about a domain name. We have it installed on PythonAnywhere, so you can run it
from a Bash console.

Here is a sample run for a correctly-configured domain, and its output. We'll
explain specific parts of it later.

    $ dig www.yourdomain.com

    ; <<>> DiG 9.10.3-P4-Ubuntu <<>> www.yourdomain.com
    ;; global options: +cmd
    ;; Got answer:
    ;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 38590
    ;; flags: qr rd ra; QUERY: 1, ANSWER: 2, AUTHORITY: 0, ADDITIONAL: 1

    ;; OPT PSEUDOSECTION:
    ; EDNS: version: 0, flags:; udp: 4096
    ;; QUESTION SECTION:
    ;www.yourdomain.com.        IN      A

    ;; ANSWER SECTION:
    www.yourdomain.com. 60 IN   CNAME   webapp-12345.pythonanywhere.com.
    webapp-12345.pythonanywhere.com. 60    IN      A       35.173.69.207

    ;; Query time: 25 msec
    ;; SERVER: 127.0.0.1#53(127.0.0.1)
    ;; WHEN: Thu Jun 13 16:46:46 UTC 2019
    ;; MSG SIZE  rcvd: 113

The most important part of this is the piece labeled "ANSWER SECTION". This
shows how the DNS system is handling your domain.

Since `www.yourdomain.com` is a
correctly configured CNAME, it points to `webapp-12345.pythonanywhere.com` (the
first line of the section).  The second line shows what IP address that
ultimately resolves to.

Another important part of the "ANSWER SECTION" is
the number before the IN in the first line. It is the TTL (or Time-to-Live) of
the DNS record. Every DNS record has a TTL and that determines how long a
machine will cache a result for in seconds. In the example above it would
take at least 1 minute for a change to become visible. A TTL of 3600 would take
at least an hour, and so on.  So if the number there is high, and you've only
waited a few minutes for the DNS changes to take effect, you may need to wait
longer.

If there is no "ANSWER SECTION", it means that the website address does not exist in the
DNS system -- generally that means that you haven't set up the CNAME correctly.
The most common cause of this is that the "name" of the CNAME record is wrong.
Some registrars require that you enter `www.yourdomain.com`
for the "name" of the CNAME; other registrars only want `www`.  If you enter `www.yourdomain.com` into
the settings for a registrar that only wants `www`, then they will interpret it as a CNAME
record for `www.yourdomain.com.yourdomain.com`, which obviously won't work.  You can check if
this has happened by running `dig www.yourdomain.com.yourdomain.com` -- if that comes
back with a correct CNAME setup like the one above, then edit your CNAME record on
your registrar's site, so that the name is just `www`.

If there is an "ANSWER SECTION", you might find that instead of having a CNAME it has something
like this:

    www.yourdomain.com.	275	IN	A	1.2.3.4

-- the important bit being that it says "A" where the previous example had "CNAME",
followed by some numbers instead of `webapp-12345.pythonanywhere.com`.
If this happens, it's because there's an A record rather than a CNAME set up for
your domain.  Check your DNS setup on your registrar's page -- a common cause of
this kind of thing is if you have set up the CNAME correctly for
`www.yourdomain.com`, but your registrar had
previously set up an A record for the same address -- the A record overrides
the CNAME.  Be careful before changing anything here -- if you have an A record
that is not for `www.yourdomain.com`, it's probably OK.  But if there is one for
that host name, then you should delete it, wait for the change to propagate,
and see if that fixes it.


## How DNS works

We have also a [a separate help page](/pages/DNSPrimer/) that describes a little
about how DNS works. It's a great place to start if you're confused and don't
understand what's really going on with your custom domain.


