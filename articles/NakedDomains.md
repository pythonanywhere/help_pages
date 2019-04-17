
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





## CNAMEs and "naked" domains


When you're setting up a web application at PythonAnywhere and want to have it
running on your own domain, we ask you to set up a CNAME record with your DNS
provider.

The problem is, CNAMEs don't work if you don't have anything in front of the
domain name -- that is, you can have a CNAME for `www.yourdomain.com`, or
`somethingelse.yourdomain.com`, but not for just `yourdomain.com`. This is a
limitation of the way DNS works.

But understandably lots of people want their users to be able to just go to
`http://yourdomain.com/` and get the site. There are two ways to do this:

## Solution 1: Use a redirection service

A redirection service makes it so that when someone goes to
`http://yourdomain.com/` they are redirected to `http://www.yourdomain.com/`,
or if they go to `http://yourdomain.com/foo` they are redirected to
`http://www.yourdomain.com/foo`, and so on. This is the best solution, and many
domain name registrars/DNS providers support it, often calling it something
like "web site redirection" or "URL forwarding". If you're using
[GoDaddy](//www.godaddy.com/), you may find
[this post](//webmasters.stackexchange.com/questions/9849/how-to-forward-non-www-to-www-using-godaddy-dns-manager)
useful.

If your registrar doesn't support redirection, many users have recommended
the free service from [WWWizer](http://wwwizer.com/naked-domain-redirect), which
has been around for some time; there's also a new, also free, service from
[NakedSSL](https://www.nakedssl.com/) which can handle HTTPS redirection -- that
is, from `https://yourdomain.com` to `https://www.yourdomain.com`, which we
think is unique to them.



## Solution 2: Set up (and pay for) a separate web app for your naked domain.

You'll need to create an additional entry on the web tab for the naked domain,
and then use an A record for `yourdomain.com` instead of a CNAME.

The A record has to be an IP address -- use the one associated with the
`webapp-XXXX.pythonanywhere.com` value that the "Web" tab tells you to use for
your CNAME (you can look this up using command-line tools like `dig` or `nslookup`.)

 This is a much worse solution, but if you can't set up the redirection service
then it might be the only way.


## Why prefer redirection?

There are three reasons why the redirection setup is much better:

1. If your webapp uses a CNAME, then we at PythonAnywhere can much more
  easily load-balance it. We control the DNS for `*.pythonanywhere.com`
  (obviously) so if your DNS settings say that your domain is wherever
  `webapp-XXXX.pythonanywhere.com` is, when we change our DNS for
  `webapp-XXXX.pythonanywhere.com` then your website will automatically follow.

2. If you use the A record setup, then you essentially have two copies of your
  site on the Internet, one at `www.yourdomain.com` and one at
  `yourdomain.com`. If someone links to you, they might link to one or the
  other -- you have no control over which. This means that the Google pagerank
  you get from incoming links is split between the two sites, which means that
  each one of your sites gets less than half the pagerank you'd get by having
  just one canonical version. This will really mess up how high up you appear in
  search results -- essentially, you're competing with yourself for placement.
  We've also heard that Google give lower ranking to sites that appear to be
  copies of other sites (to penalise spammers) -- so it could be even worse.

3. You will need to set up a separate web app on the PythonAnywhere "Web" tab
 to match the naked domain. Every different domain needs its own web app so
  that our servers can forward HTTP requests based on the domain they request; so
  www.yourdomain.com and yourdomain.com need two different web apps. You can
  still point the two entries at the same codebase -- the easiest way is probably
  to use "Manual Config", and then copy across the relevant lines from the WSGI
  file of your existing web app...

## Are there any reasons to use the extra webapp instead?

The main reason is that a redirection service only works for `http`.  It can't work
for `https` (because to do that, the third party service would need your ssl
cert and key).  So someone that manually types in `https://` plus your domain
won't be redirected to your site.

We tend to advise people that this isn't a problem, because if someone just types
the naked domain into their browser, the browser will default to using http, and
that will be picked up by the redirection service.  SO the only people you'd have
to worry about are those that manually bother to type `https://` plus your naked
domain, or people who explicitly create a hyperlink somewhere on the Internet
with `https` plus your naked domain.


Related:  [how to redirect http to https](/pages/ForcingHTTPS/)

