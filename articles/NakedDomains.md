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
People see `yourdomain.com` and `www.yourdomain.com` as being
essentially the same thing.


## Your website on `yourdomain.com`

So for a website, you generally want people to be able to visit it by typing in
either of the normal versions of the address -- the one with the `www.` at the
start, or the one without.  If you put your website on just one of them, some
people will use the other one and get confused when they don't see anything.

What we recommend is that you have the "official" version of your website on
`www.yourdomain.com`, and then set things up so that `yourdomain.com`
automatically redirects people to that official version.  The rest of this
page explains how to do that last step.

This is better than doing it the other way around because the DNS setup for
naked domains is more complicated and fragile, because you can't use CNAMEs for
them -- there's more information about that in our
[help page about the basics of DNS](/pages/DNSPrimer).  (If you're completely
set on using a naked domain, we recommend that you use an ALIAS record rather
than an A record to point to it -- however, that's not officially supported as
either part of the DNS specification or by us, so only do that if you really
know what you're doing -- if you're new to this, then use the
`www.yourdomain.com` address.)

What we very strongly recommend against is having two separate copies of your
website, one at `yourdomain.com` and one at `www.yourdomain.com`.  More about
that later.


## How to set up a redirect?

There are a couple of ways you can do this:

## Solution 1: Use a redirection service

This is the solution we recommend -- it's normally easiest and cheapest,
especially because most domain registrars offer it as part of your registration.

If you use a redirection service:

* When someone goes to `http://yourdomain.com/` they are redirected to
`http://www.yourdomain.com/`
* If they go to `http://yourdomain.com/foo` they are redirected to
`http://www.yourdomain.com/foo`, and so on.

Things get a little more complex with HTTPS -- it's easy to set up a redirect
that goes *to* an `https://` URL, but ones that come *from* an HTTPS URL are
not supported by all redirection services.

This is normally not a problem,
because all you're trying to handle is people typing URLs into a browser.  If
someone types `yourdomain.com` or `http://yourdomain.com`, they'll get your
site.  The only case that won't work is if they type `https://yourdomain.com`,
including the `s` after `http`, which pretty much no-one is ever going to do.

But there's one exception to this: if you're using a domain that is on the
[HSTS preload list](https://en.wikipedia.org/wiki/HTTP_Strict_Transport_Security).
With those, even if someone explicitly typed `http://yourdomain.com`
into their browser, the browser would rewrite it to `https://yourdomain.com` and
try to go there.  Some top-level domains (TLDs) that enforce this are `.android`, `.app`, `.bank`, `.dev`,
and `.foo`, but there are many more and it's likely that others will appear in
the future.  So if (for example) you have `yourdomain.android` you'll need to
handle redirects from `https://yourdomain.android` to `https://www.yourdomain.android`.

So, with all that said, which redirection service should you use?  Most domain
providers offer it as a free service as part of your domain registration:

  * [Gandi](https://docs.gandi.net/en/domain_names/common_operations/web_forwarding.html) offer both HTTP and HTTPS redirects.
  * [GoDaddy](https://uk.godaddy.com/help/forward-a-domain-12123) offer HTTP-only redirects.
  * [NameCheap](https://www.namecheap.com/support/knowledgebase/article.aspx/385/2237/how-to-redirect-a-url-for-a-domain) offer HTTP-only redirects.

> If you are using a different registrar, searching for "forward naked domain" plus
> the name of your registrar will probably find the appropriate help page.

If you're using Gandi, you're fine -- you can set up a redirect that's both
HTTP and HTTPS, and everything will work.  Likewise if you're using a registrar
that's not listed above, that *does* offer redirects from HTTPS URLs.

If you're using a registrar that doesn't support redirects from HTTPS, you're
probably still fine, for the reasons mentioned above -- unless your domain is an
HSTS one.

If you're on `.dev`, or need redirects from `https://yourdomain.com` for some other
reason, and your registrar doesn't support it, you'll need to use a third-party
provider.  A good option is [NakedSSL](https://www.nakedssl.com/), though unfortunately
they charge for the service.  Or alternatively, you could migrate your domain
to another registrar that provides it for free, like Gandi.


## Solution 2: Set up (and pay for) a separate web app for your naked domain.

This will cost a little more because you'll need to create two websites inside
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
