
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

## Bug classes we're not really interested in

* "I can run code on your servers" - Yup. That's our business.

* Self XSS - If you can execute XSS-style attacks against your own account by
  uploading a file and then loading it in the browser, that's not particularly
  interesting to us.

* Auto-pwnage - "If I run this code it does something bad to my
  account/files/web apps"

* Problems on sites we host for our users -- sites at, eg, *username.pythonanywhere.com*
  are not written by us (but if you can find contact details on those sites, you
  are welcome to contact their owners directly).  Please only report vulnerabilities
  for www.pythonanywhere.com.

* Attacks that assume a users' login session has already been compromised.  If an attacker has
  access to a logged-in session by a user, we pretty much consider that "game over" already,
  since the attacker already has full access to all the users' files and data etc.
  So the fact that the attacker may be able to, eg, brute force an email reset
  as well, isn't something we consider a serious additional security risk.

* We do not pay bug bounties for these "bugs".


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


##

Send reports to support@pythonanywhere.com
