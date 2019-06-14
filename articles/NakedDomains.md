<!--
.. title: Naked domains
.. slug: NakedDomains
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

## What is a naked domain?

When you buy a domain name from a registrar, you become the owner of something
like `yourdomain.com`.  What this means is that you can create entries in the
Domain Name System that end with `yourdomain.com`, like `www.yourdomain.com`,
`api.yourdomain.com`, `ftp.yourdomain.com`, and so on.  In a strict technical
sense, these are also domain names, and the term "naked domain" -- sometimes
also called an "apex domain" -- has been coined to refer to the bit of the
domain name you originally bought -- just the `yourdomain.com` without anything
in front of it.

It's important to know that all of the above are completely different domain names
in a technical sense.  You could in theory have one website on `yourdomain.com`,
another different one on `www.yourdomain.com`, another on `somethingelse.yourdomain.com`,
and so on.

What that means is that if you set up a website at `www.yourdomain.com` on
PythonAnywhere, people will be able to view it if they enter that exact name
into their browser.  If they just enter `yourdomain.com` then they will get
something else -- exactly what they see will depend on how your DNS settings
are configured.   Likewise if you managed to set up a website for
`yourdomain.com`, it would not show up if people typed in `www.yourdomain.com`.

Back in the early days of the Internet, this was unsurprising -- people would
expect to have to enter the address of the web server for the website (and of
the FTP server for the FTP site, and soon).  But nowadays, it's a bit confusing.
Most importantly people see `yourdomain.com` and `www.yourdomain.com` as being
essentially the same thing.


## Your website on `yourdomain.com`

So for a website, you generally want people to be able to visit it by typing in
either of the normal versions of the address, with one with the `www.` at the
start or the one without.  If you put your website on just one of them, some
people will use the other one and get confused when they don't see anything.

What we recommend is that you have the "official" version of your website on
`www.yourdomain.com`, and then set things up so that `yourdomain.com`
automatically redirects people to that official version.

This is better than doing it the other way around because the DNS setup for
naked domains is more complicated and fragile, because you can't use CNAMEs for
them -- there's more information about that in our
[help page about the basics of DNS](/pages/DNSPrimer).

What we very strongly recommend against is having two separate copies of your
website, one at `yourdomain.com` and one at `www.yourdomain.com`.  More about
that later.


## How to set up a redirect?

There are a couple of ways you can do this:

## Solution 1: Use a redirection service

This is the solution we recommend -- it's easiest and cheapest.  If you use a
redirection service:

* When someone goes to `http://yourdomain.com/` they are redirected to
`http://www.yourdomain.com/`
* If they go to `http://yourdomain.com/foo` they are redirected to
`http://www.yourdomain.com/foo`, and so on.

They normally don't support HTTPS, however.  This is generally not a problem
because all you're trying to handle is people typing URLs into a browser.  If
someone types `yourdomain.com` or `http://yourdomain.com`, they'll get your
site.  The only case that won't work is if they type `https://yourdomain.com`,
including the `s` after `http` which pretty much no-one is ever going to do.
However, if you think that people are going to do it for your site, then see the
"HTTPS redirection" section below.

Many domain name registrars/DNS providers provide HTTP redirection as a free
service as part of the domain registration fee, often calling it something
like "web site redirection" or "URL forwarding". If you're using
[GoDaddy](//www.godaddy.com/), you may find
[this post](//webmasters.stackexchange.com/questions/9849/how-to-forward-non-www-to-www-using-godaddy-dns-manager)
useful.

If your registrar doesn't support redirection, lots of people hosting on
PythonAnywhere use the free service from
[WWWizer](http://wwwizer.com/naked-domain-redirect), which has been around for
some time.


### HTTPS redirection

There's also a new free service from
[NakedSSL](https://www.nakedssl.com/) which can handle HTTPS redirection -- that
is, from `https://yourdomain.com` to `https://www.yourdomain.com`, which we
think is unique to them.  Because it's new, we can't recommend it unreservedly,
but they seem pretty solid to us so far :-)


## Solution 2: Set up (and pay for) a separate web app for your naked domain.

This will cost a little more beause you'll need to create two websites inside
PythonAnywhere for it:

* One at `www.yourdomain.com` for the "official" version.
* One at `yourdomain.com` to handle redirections.

The first one will use a normal [CNAME setup](/pages/CustomDomains) to point
the address to the site, and the second will use an A record.
The A record has to be an IP address -- use the one associated with the
`webapp-XXXX.pythonanywhere.com` value that the "Web" tab tells you to use for
your CNAME (you can look this up using command-line tools like `dig` or
`nslookup`).  See our [DNS primer](/pages/DNSPrimer) for more information about
A records.

Once you have the two sites set up, you can set up the WSGI file for the
`www.yourdomain.com` site to show your website, and then use code based on the
template at [this help page](/pages/RedirectWebApp) to do the redirection.

You can also
[add on an HTTPS certificate](https://help.pythonanywhere.com/pages/HTTPSSetup)
for both of them, so that HTTPS will work everywhere.


## Why not just have two copies of the site instead of redirecting?

As we said earlier, we strongly recommend against having two copies of your
website, one at `yourdomain.com` and one at `www.yourdomain.com`.

If you do that, and someone links to
you, they might link to one or the other -- you have no control over which.
This means that the Google pagerank you get from incoming links is split between
the two sites, which means that each one of your sites gets less than half the
pagerank you'd get by having just one canonical version. This will really mess
up how high up you appear in search results -- essentially, you're competing
with yourself for placement. We've also heard that Google give lower ranking to
sites that appear to be copies of other sites (to penalise spammers) -- so it
could be even worse.

All in all, there are no benefits to having two copies of the website, and it
messes up your SEO.
