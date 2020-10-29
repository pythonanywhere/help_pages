<!--
.. title: How DNS works: a beginner's guide
.. slug: DNSPrimer
.. date: 2019-06-14 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

We sometimes get emails from people who are trying to point their custom domain
at PythonAnywhere so that they can host their website, but are struggling to set
up their DNS settings.  Normally DNS setup is pretty simple, but sometimes
people can get bogged down due to confusing interfaces on their registrar's
site, or complexities in the terminology people use.

The parts of DNS that you need to know about in order to host a website are
actually not all that complicated, but some domain registrars have complicated,
hard-to-understand interfaces.  Either they assume that you understand all of
the technical details about how the whole thing works -- which makes it hard for
first-timers -- or they try to put a simple user-friendly interface on top of
it, but simplify it so much that it's actually harder to use because they're
hiding important stuff from you.

Given that basic DNS stuff really isn't all that hard, we felt that it would be
a good idea to post an explanation, going from the basics up to some slightly
deeper stuff.  This post is written so that if you only want the basics, you can
just read the first part, while if you want a deeper understanding -- either out
of interest, or because your domain registrar has got such a low-level interface
that you need to -- then you can keep reading.

It's worth noting that for most people, you don't need to know any of this stuff
to set up a website on PythonAnywhere, even with a custom domain; it's meant
more as an explanation so that people who do run into problems with their
registrar have the background knowledge they need to solve the problem -- or,
indeed, to explain to the registrar's tech support team what the problem is.
And, of course, it's a bit of light reading for people who are just interested
in this stuff :-)


### The basics: domain names and IP addresses

When a browser wants to connect to `www.yourdomain.com`, it needs to know which
computer on the Internet is hosting that site.   The string `www.yourdomain.com`
is a hostname (technically it's a "fully qualified domain name"), but at the
underlying network layer, all computers are identified by IP addresses, which
are numerical.  So somehow the browser needs to find out which numerical IP
address it should use when it wants to talk to `www.yourdomain.com`.

It does that by asking a DNS server -- in full, a Domain Name System server.
Normally this will be a server that's provided by your ISP or your local network
administator; in general, when your computer joins a network, the details of the
DNS server are part of the information it gets from the router.  So to convert a
hostname to an IP address, the browser makes a system call to the operating
system saying "please get me the IP address for `www.yourdomain.com`", the
operating system sends a message to the DNS server with the same request, and
the DNS server responds with the IP address: something like "23.145.21.243"
(in IP version 4, the version that's currently most widely used, IP addresses
are normally written as four numbers between 0 and 255, separated by dots --
I'll use similar addresses as examples later on).   Now the browser can connect
to the server at that IP address, send it an HTTP message saying "please send me
the contents of the front page for `www.yourdomain.com`", and the server will
respond with the appropriate stuff.

What all this means is that when you want your custom domain to be hosted on
PythonAnywhere, you're essentially setting things up so that all of the DNS
servers across the Internet know what IP address to provide when someone wants
to access your site.   (This, by the way, is why we say that the changes you
make "may take some time to propagate across the Internet" -- it's not just one
central database that needs to be updated; instead, different ISPs will pick up
the change at different times.   A little more about that later.)


### DNS records

The explanation above is, of course, a bit simplified.  The DNS database isn't
just a mapping from hostnames like `www.yourdomain.com` to IP addresses.
Instead, for each "domain name", it can keep a bunch of different types of
records.   I put "domain name" in quotes back there because the technical
meaning of the words here is slightly different to what people normally use it
to mean.   When we normally use the phrase "domain name", we mean something
like "yourdomain.com", "google.com", or "bbc.co.uk".  That is, we mean the
portion of a network address that identifies a particular organisation.  We'd
expect (for example) Google to own the domain name `google.com`, to have a
website at `www.google.com`, and for people who work there to have email
addresses like `alice.jones@google.com`.

But in the technical parlance of DNS, a "domain name" is something a little more
subtle.  [The Wikipedia article](https://en.wikipedia.org/wiki/Domain_name) is
(of course) a good explanation, but a summary is:

* There is a "root" domain called `.`
* There is a subdomain of the root domain called `com.`
* If you buy `yourdomain.com` then you own `yourdomain.com.`, which is is a subdomain of `com.`
* If you create a website at `www.yourdomain.com` then technically you've created a subdomain of `yourdomain.com.` with the name `www.yourdomain.com.`.

(You'll notice that all of the domain names above end with the `.` to represent
the root domain.  Technically domain names always should, but no-one ever
bothers, so I won't use the extra `.` in the rest of this article.)

Basically, any level of the hierarchy is a domain name.  A number of different
kinds of "records" can be associated with a domain name.  The domain
`yourdomain.com` might have various records, and so might `www.yourdomain.com`.
Any domain can have a number of different records, including multiple records
of the same type.

Some examples of record types are:

* A ("Address") records, which are how you specify an IPv4 address like 23.145.21.243.  These tell DNS that if someone wants to treat the domain name as the name of a computer, then this is the IP address they should use.
* MX ("Mail eXchange") records, which specify what email server should be used for a domain.  If someone wants to send email to bob@yourdomain.com, the email systems involved will use the MX record for `yourdomain.com` to work out which computer to deliver it to.
* TXT ("TeXT") records, which are pretty much free-form text and are used for various purposes including verifying senders of email messages.

There are a bunch of others -- NS, SOA, and so on.  But apart from A records
(which you can see are obviously important in the example above where we got the
IP address for a hostname), there's one other interesting kind of record: CNAME.


#### CNAMEs

When a browser (via its operating system) asks its DNS server for the IP address
corresponding to a hostname, the server can respond in a number of different
ways:

* If it doesn't know what the IP address is, it will just return a response saying so, so that the browser can display an appropriate error page.  (For example Chrome will say something like "www.nonexistent.com’s server IP address could not be found.")
* If it has an A record for the hostname, then it will just return the record and the browser will use the IP address contained in it.
* If it doesn't have an A record, but does have a CNAME (abbreviated from "canonical name") record then it will return that.  The CNAME record doesn't contain an IP address; instead, it contains another hostname.  The browser can then send the DNS server a second message, saying "OK, then -- so what's the IP address of *that* hostname" -- and hopefully the response this time will have an IP address.  (Of course, it could just respond with another CNAME record, which would require a third lookup, and so on.)

CNAME records, on the face of it, look like a somewhat roundabout and
inefficient way to do things.  Instead of making one request to get from a
hostname to an IP address, a browser will need to make two or more.  So why is
it that when you create a website with a custom domain on PythonAnywhere, we
ask you to set up a CNAME record to point `www.yourdomain.com` to a hostname
like `webapp-123456.pythonanywhere.com`, rather than just providing you with an
IP address so that you can create an A record?

The answer is that CNAMEs are actually really useful -- and also not all that
inefficient in practice.

The usefulness first: let's imagine you had a website hosted at
`www.yourdomain.com`, and you set up an A record with your registrar to point it
at an IP address that belonged to PythonAnywhere.   Your site would be up and
running, and everything would work fine so long as that IP address was always
the right one for your site.   But if it changed, you'd need to log in to your
registrar again and update it.

But IP addresses sometimes have to change.  Sometimes they [get blocked in
certain countries](https://blog.pythonanywhere.com/163/).  Sometimes a specific
IP address might be subjected to a denial-of-service attack, and be unusable.
Or sometimes we at PythonAnywhere might want to move your site from one IP
address to another simply to balance out load across our cluster of servers.

If you're using a CNAME record, then IP address changes like that are something
you don't need to worry about.  We can update the A records for our own
hostnames, like `webapp-123456.pythonanywhere.com`, because we control the DNS
settings for `pythonanywhere.com` and all of its subdomains.  Because your
website is pointed at us using a CNAME, browsers that want to connect to your
site will start using the new IP address without you needing to do anything.
They'll ask for the IP address of `www.yourdomain.com`, they'll get a CNAME
response saying that it's the same as the one for
`webapp-123456.pythonanywhere.com`, so they'll look up the IP address for that
and will get the correct new address from the A record that comes back.

But we can't update DNS records for your domain -- only you can do that -- so if
you use a A record, when the IP address changes you'll have to update it
yourself every time.   If you happened to be away, or if we don't have
up-to-date contact details for you, it might be some time before you knew about
the problem and were able to fix it.

So what about the inefficiency?  We always make sure that the
`webapp-XXXXXX.pythonanywhere.com` addresses point to an A record rather than
another CNAME, but that's still, in theory, two lookups to go from
`www.yourdomain.com` to an IP address -- one to get the CNAME, and one to get
the IP address from the hostname stored there.
[According to Cloudflare](https://www.cloudflare.com/learning/dns/what-is-1.1.1.1/),
the average ISP has a 70 millisecond round-trip time for queries, so that might
mean that your site would load up 70 milliseconds slower if it needs to do two
queries rather than one.  Not a huge amount of time, but given that research
shows that people are less engaged with slower websites, every millisecond
counts.

The answer here is twofold -- firstly, your computer will generally cache the
results of DNS lookups for some time.  So this extra time will only impact some
hits to your page.  Secondly, many DNS servers are pretty smart -- if someone
asks for a hostname, and the result is going to be a CNAME record, they know
that the next request is likely to be for the CNAME's value -- so they'll attach
the results for that to their response as well.  So, for example, a browser
might say "what's the address for `www.yourdomain.com`?" and the DNS server
would reply "`www.yourdomain.com` has a CNAME pointing to
`webapp-123456.pythonanywhere.com`.  Oh, and by the way,
`webapp-123456.pythonanywhere.com` has an A record pointing to the IP address
1.2.3.4".  The browser can then just use the IP address directly; there's only
one lookup, but the CNAME is fully resolved.

So using CNAME records to point your website at PythonAnywhere means less
maintenance for you, and in general no real performance overhead.

There is one case where CNAMEs can be problematic, though:


#### Naked domains

One problem with CNAMEs is that in general, you can't use them for "naked"
domains.  A naked domain is the domain name that you buy from your registrar,
omething like `yourdomain.com` -- without anything like `www.` in front of it.
For [relatively arcane technical reasons](https://medium.freecodecamp.org/why-cant-a-domain-s-root-be-a-cname-8cbab38e5f5c)
a naked domain can't use a CNAME, only subdomains like `www.yourdomain.com` --
and so if you want `yourdomain.com` without the `www.` to point to
PythonAnywhere, you have to use an A record.

That's why we suggest that if you want your site to be accessible without the
`www.`, you should host it at `www.yourdomain.com`, and then use a redirection
service so that people who visit the address without the `www.` will be
transparently redirected to the address with it.  Most registrars have this
kind of thing built in.  You tell them to do the redirection, and they'll set up
an A record pointing to one of their servers, and that server will do the
redirect when it receives a request -- and because, unlike us, they can update A
records on your behalf, they can fix things if it needs to change.  If your
registrar doesn't support it, there are third-party services you can point to
with an A record you set up yourself.

[See our help pages for details of how to set up a redirect](https://help.pythonanywhere.com/pages/CustomDomains#optional-set-up-a-naked-domain-redirect)
-- we have links to the appropriate documentation for a bunch of popular domain
registrars, and also some links to third-party services if you need to use them.

##### Sidebar: ALIAS records

Some DNS providers support what they call "ALIAS" records.  These are not part
of the DNS standard, but they way they work is that you create a record that
looks a bit like a CNAME -- it maps from a domain name of yours to a hostname.
The way they work internally is that when a client requests the domain, the DNS
provider just does the lookup for the hostname that the domain name points to
internally, and returns what looks like an A record -- kind of like the cached
CNAME example above.  So, for example, a browser might say "what's the address
for `yourdomain.com`?" and the DNS server would see that it had an ALIAS record
for `yourdomain.com` CNAME pointing to `webapp-123456.pythonanywhere.com`, so it
would look up the IP address for `webapp-123456.pythonanywhere.com` and would
reply (bending the truth a little that "`yourdomain.com` has an A record
pointing to the IP address 1.2.3.4".

Their advantage over CNAME records is that they can be created for naked
domains, so you can use one to host a site at `yourdomain.com` on PythonAnywhere
without needing to use an A record.

However, because they are not a part of the DNS standard, we don't officially support
them.  Still, they will in general work, and they're better than using
an A record.


### How to use all of that information

Hopefully by now it should be clear what you need to do when pointing a custom
domain to PythonAnywhere; you log into your domain registrar's website, and find
the place where you set up your DNS configuration.  Once you're there, you set
up a CNAME record to point `www.yourdomain.com` to the
`webapp-XXXXXX.pythonanywhere.com` value shown when you look at your website's
configuration on the "Web" page inside PythonAnywhere.   If there are any other
A or CNAME records for `www.yourdomain.com` then you should delete them (because
having two records for the same hostname will potentially confuse the DNS).
But don't delete any other records -- there may be things like MX records, which
you'll remember are used for email, or "NS" or "SOA" records, which are
low-level DNS stuff that you shouldn't touch without knowing pretty clearly what
you're doing.

Different registrars have different interfaces, but with most of them it's
reasonably easy to find the bit you need once you know what you're looking for.
We also have [some links to the appropriate documentation on the sites of
popular registrars on our help pages](https://help.pythonanywhere.com/pages/CustomDomains#notes-for-specific-dns-providers).

One thing that does sometimes confuse people is that many registrars only
require you to type in the bit that goes before your domain name when specifying
a record -- that is, for `www.yourdomain.com` you would set up a CNAME with a
"name" of `www` and a "value" of `webapp-XXXXX.pythonanywhere.com`.  If you
created one with a "name" of `www.yourdomain.com`, then the CNAME would actually
point the hostname `www.yourdomain.com.yourdomain.com` at PythonAnywhere, which
would be unhelpful :-)

Sometimes people are told by their registrar that instead of setting up a CNAME,
they need to provide a name server (or even two name servers).  Oddly, this
sometimes happens even when the registrar in question really does support
CNAMEs.   Without wanting to call any registrar out in particular, if you are
told that, but your registrar appears on the
[list on our help pages](https://help.pythonanywhere.com/pages/CustomDomains#notes-for-specific-dns-providers)
then the customer service person you're talking to is a little confused, and you
should check out the documentation that we link to.

But some registrars really do not allow you to set up CNAMEs; they require you
to specify name servers.  This can happen, for example, with some country-level
domains.  Explaining what that means is what we'll move on to next.


### Domain registrars versus DNS and name servers

Providing the ability to register domains, and providing the DNS stuff for those
domains are, technically speaking, two different services.   Given that in
general it's pretty pointless to own a domain without being able to associate it
with an IP address so that you can host a website there, most companies that do
domain registration provide both registration and DNS services as a bundle, so
you don't need to know about the separation -- but it is there, and if you find
yourself having to use a registration-only service, you need to know a bit more
about how things work.

The first thing to explain is what a name server is.   Remember that earlier we
said that when a browser wants to connect to `www.yourdomain.com`, it asks its
local DNS server -- the one provided by the ISP -- what the IP address is.
Obviously, the DNS server needs to find the answer somehow.  It might have
cached the DNS records for the hostname you're looking for due to some previous
request, but if this is the first time it's heard about this hostname, it will
have to pass the query on to a different server.  This is the "authoritative
nameserver" for the domain; different domains will have different nameservers
set up for them.   In a normal setup, when you buy `yourdomain.com`, there will
have to be one or more computers somewhere on the Internet who, when asked for
the details of `www.yourdomain.com`, can give the official answer -- a CNAME, an
A record, or whatever.   So if the DNS server belonging to your ISP doesn't know
the IP address for `www.yourdomain.com`, it needs to ask the nameserver that is
authoritative for `yourdomain.com` for the answer.

You might wonder how your ISP's DNS server knows how to find out what those
nameservers are -- how do they know which nameserver is authoritative for
`yourdomain.com`?  The answer is that they ask the nameservers that are
authoritative for "one level up" -- that is, if they want to know which
nameservers are authoritative for `yourdomain.com`, they'll ask the nameservers
that are responsible for `.com` to tell them.  Likewise, if asked "which
nameservers are authoritative for `yourdomain.co.uk`?", they would ask the
nameservers that are authoritative for `.co.uk`, which might first require them
to ask who is authoritative for `.uk` in order to make that query.   (You might
in turn wonder how the whole thing gets bootstrapped -- how the DNS server works
out the nameservers that are authoritative for these top-level domains like
`.com` and `.uk`.  The answer is that there are
[some special servers](https://www.iana.org/domains/root/servers) that handle
that -- that is, servers that are right at the top of the tree, and are
authoritative for the `.` "root" domain we mentioned a while back.)

So -- when you register a domain name with a normal "bundled" registrar like
GoDaddy, they will do three things:

* Register you as the owner of the domain with the organisation who is responsible for keeping track of such things (which will be a different one for each top-level domain -- Verisign for .com, Nominet UK for .uk, and so on)
* Set up one or more of their own nameservers so that they can give authoritative answers to questions about your domain.
* Tell the authoritative nameservers one level up from your domain (that is, the `.com` ones for `yourdomain.com`) that their -- that is, the registrar's -- nameservers are authoritative for your domain.

Once that's done, you're all set -- you can use their web interface to update
your DNS settings, and when you do that they'll pass the changes on to the
appropriate nameservers.

However, if you are using a registrar which doesn't do DNS for you, they won't
do the last two steps.   They'll just register the domain.   They will, however,
have a way to tell the one-level-up nameservers which nameservers are
authoritative for your domain -- but you'll need to provide them with the names
of some servers in order for them to do that.

Setting up your own nameserver is really tricky, but luckily you don't need to
do that.  There are free services out there that can handle all of it for you,
so you just need to sign up with one of them.   They'll provide you with the
addresses of some nameservers that you can then pass on to your registrar, and
a web-based interface so that you can set up all of your DNS records like the
CNAME and so on.   One that consistently get good reports from our users is the
[FreeDNS service from Namecheap](https://www.namecheap.com/domains/freedns/).


### Conclusion

Hopefully that was all reasonably clear.  You now know the basics of how DNS
works, and how it interacts with domain registration.   If you've got any
questions, please drop us a line at
[support@pythonanywhere.com](mailto:support@pythonanywhere.com) -- and
additionally, if you think there are other things that you'd like us to add to
this article, please do let us know!
