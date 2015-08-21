
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





##The problem with "naked" domains


When you're setting up a web application at PythonAnywhere and want to have it running on your own domain, we ask you to set up a CNAME record with your DNS provider. 

The problem is, CNAMEs don't work if you don't have anything in front of the domain name -- that is, you can have a CNAME for `www.yourdomain.com`, or `somethingelse.yourdomain.com`, but not for just `yourdomain.com`. This is a limitation of the way DNS works. 

But understandably lots of people want their users to be able to just go to `http://yourdomain.com/` and get the site. There are two ways to do this: 

  1. Use a redirection service so that when someone goes to `http://yourdomain.com/` they are redirected to `http://www.yourdomain.com/`, or if they go to `http://yourdomain.com/foo` they are redirected to `http://www.yourdomain.com/foo`, and so on. This is the best solution, and many domain name registrars/DNS providers support it, often calling it something like "web site redirection" or "URL forwarding". If you're using [GoDaddy](//www.godaddy.com/), you may find [this post](//webmasters.stackexchange.com/questions/9849/how-to-forward-non-www-to-www-using-godaddy-dns-manager) useful. We've also had one user recommend <http://wwwizer.com/naked-domain-redirect>. 
  1. Use an A record for `yourdomain.com` and a CNAME for `www.yourdomain.com`. The A record has to be an IP address -- use the one associated with `yourusername.pythonanywhere.com`. This is a much worse solution, but if you can't set up the redirection service then it might be the only way. 

There are three reasons why the redirection setup is much better: 

  1. If your webapp uses a CNAME, then we at PythonAnywhere can much more easily load-balance it. We control the DNS for `*.pythonanywhere.com` (obviously) so if your DNS settings say that your domain is wherever `yourusername.pythonanywhere.com` is, when we change our DNS for `yourusername.pythonanywhere.com` then your website will automatically follow. 
  1. If you use the A record setup, then you essentially have two copies of your site on the Internet, one at `www.yourdomain.com` and one at `yourdomain.com`. If someone links to you, they might link to one or the other -- you have no control over which. This means that the Google pagerank you get from incoming links is split between the two sites, which means that each one of your sites gets less than half the pagerank you'd get by having just one canonical version. This will really mess up how high up you appear in search results -- essentially, you're competing with yourself for placement. We've also heard that Google give lower ranking to sites that appear to be copies of other sites (to penalise spammers) -- so it could be even worse. 
  1. You will need to set up a separate web app on the PythonAnywhere "Web" tab to match the naked domain. Every different domain needs its own web app so that our servers can forward HTTP requests based on the domain they request; so www.yourdomain.com and yourdomain.com need two different web apps. You can still point the two entries at the same codebase -- the easiest way is probably to use "Manual Config", and then copy across the relevant lines from the WSGI file of your existing web app... 
