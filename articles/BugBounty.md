
<!--
.. title: Bug Bounty
.. slug: BugBounty
.. date: 2016-11-28
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


PythonAnywhere offers a bounty for responsibly disclosed bugs. We determine the
payout depending on the severity and impact of the submitted bug. We only pay
out on the first report of a particular issue, so it's best if you contact us
first to see whether we're already working on something.


## Scope

Please only report vulnerabilities for:

* `www.pythonanywhere.com` and `eu.pythonanywhere.com` -- please note that these are two instances of the same site, so a bug reported against one of them counts as a bug against the other.  We will not pay a bounty for a bug on `eu.pythonanywhere.com` if a bounty has already been paid for the same bug on `www.pythonanywhere.com`, and vice versa
* `blog.pythonanywhere.com`
* `help.pythonanywhere.com`

As we are a web-hosting company, our users may have created websites that have bugs using our platform.
These might be hosted at URLs like *username.pythonanywhere.com*.
Do not report bugs in those sites to us;  if you can find contact details on the sites, you
are welcome to contact their owners directly.


## Bug classes we're not really interested in

* "I can run code on your servers" - Yup. That's our business.

* Self XSS - If you can execute XSS-style attacks against your own account by
  uploading a file and then loading it in the browser, that's not particularly
  interesting to us.

* Auto-pwnage - "If I run this code it does something bad to my
  account/files/web apps"

* Attacks that assume a users' login session has already been compromised.  If an attacker has
  access to a logged-in session by a user, we pretty much consider that "game over" already,
  since the attacker already has full access to all the users' files and data etc.
  So the fact that the attacker may be able to, eg, brute force an email reset
  as well, isn't something we consider a serious additional security risk.



## Bug classes we're interested in

* General XSS, CSRF etc. - Can you get a user that is logged in to PythonAnywhere to do
  something malicious to their own account by e.g. having them follow a link?

* Cross-user exploits - Can you do something bad to another user on PythonAnywhere
  from your account? Unless you're a teacher doing something malicious to your
  students - there's an explicit trust relationship, there.

* Information leakage - Can you learn something private (see their files,
  access account information) about another user/account registered on
  PythonAnywhere?

* We pay USD 50-100 for bug reports with low severity or need a very
  complicated and unlikely sequence of events to be exploited. We pay USD
  100-500 for bugs that are more directly exploitable. We only pay out bug
  bounties to the first report (not subsequent reports of the same bug).


## Bug classes we're very interested in

* Session/cookie hijacking

* OS-level privilege escalation in consoles, web apps and scheduled tasks

* Sandbox escape in consoles, web apps and scheduled tasks

* We may pay upwards of USD 1000 for high severity bugs.


## Reporting

Send reports to [support@pythonanywhere.com](mailto:support@pythonanywhere.com).
