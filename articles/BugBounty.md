
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

* `www.pythonanywhere.com` and `eu.pythonanywhere.com` -- please note that these
  are two instances of the same site, so a bug reported against one of them counts
  as a bug against the other.  We will not pay a bounty for a bug on `eu.pythonanywhere.com`
  if a bounty has already been paid for the same bug on `www.pythonanywhere.com`,
  and vice versa.

* `blog.pythonanywhere.com`

* `help.pythonanywhere.com`

* `integration.pythonanywhere.com`

As we are a web-hosting company, our users may have created websites that have bugs using our platform.
These might be hosted at URLs like *username.pythonanywhere.com*.
Do not report bugs in those sites to us;  if you can find contact details on the sites, you
are welcome to contact their owners directly.


## Out of scope -- do not report these as vulnerabilities

PythonAnywhere is a hosting platform. Users are intentionally allowed to run
code and publish arbitrary content, including files, HTML, JavaScript, and web
applications. We do not generally inspect or sanitize user-hosted content before
serving it.

**Content is not private merely because it contains sensitive information.** If
users place files, credentials, tokens, source code, or other data in a publicly
served location, or configure their web apps to return that data, public access
is the expected result of their configuration. It is not a PythonAnywhere
vulnerability.

A report is out of scope if all of the following are true:

1. The reporter controls the affected PythonAnywhere account or web app.
2. The reporter uploaded, created, published, or configured the exposed content.
3. No other user's account, private data, or authenticated PythonAnywhere
   session is affected.

This remains out of scope even if the published content is sensitive, executes
JavaScript, downloads a file, reveals credentials placed in it, or could be
dangerous if another person chose to use it.

Examples that are **not vulnerabilities and are not eligible for a bounty**:

* Uploading a file to your own public web app and then accessing it without
  authentication.
* Publishing secrets or credentials through your own web app.
* Hosting arbitrary HTML or JavaScript on your own web app.
* Uploading malicious content and then opening or executing it yourself.
* Running code that damages or exposes your own account, files, databases, or
  web apps.
* Self-XSS, including attacks that require you to paste code into your own
  browser console.
* Demonstrating that code can run on PythonAnywhere; running user code is a core
  feature of the service.

The important question is not "can this content be reached from the Internet?"
It is "did PythonAnywhere expose data or capabilities across a boundary that the
affected user did not make public?"

Other reports that are out of scope include:

* Attacks that assume that accounts need to have unique email addresses. We
  allow multiple accounts to have the same email address.

* Attacks that assume a users' login session has already been compromised.  If an attacker has
  access to a logged-in session by a user, we pretty much consider that "game over" already,
  since the attacker already has full access to all the users' files and data etc.
  So the fact that the attacker may be able to, eg, brute force an email reset
  as well, isn't something we consider a serious additional security risk.

* Attacks where the victim is student of the attacker - there's an explicit 
  trust relationship, there.


## Bug classes we're interested in

* General XSS, CSRF etc. -- Can an attacker cause a different logged-in
  PythonAnywhere user to do something malicious, for example by getting them to
  follow a link or visit a page? Self-XSS and attacks that require the victim to
  paste code into their browser console are out of scope.

* Cross-user exploits -- Can you do something bad to another user on PythonAnywhere
  from your account? Unless you're a teacher doing something malicious to your
  students - there's an explicit trust relationship, there.

* Information leakage -- Can you learn something private (see their files,
  access account information) about another user/account registered on
  PythonAnywhere?


## Bug classes we're *very* interested in

* Session/cookie hijacking.

* OS-level privilege escalation in consoles, web apps, Jupyter notebooks and scheduled/always-on tasks.

* Sandbox escape in consoles, web apps, Jupyter notebooks and scheduled/always-on tasks.



## Reporting

Send reports to [bugbounty@pythonanywhere.com](mailto:bugbounty@pythonanywhere.com).

The most important part of a report is a clear, complete, step-by-step description
of what we need to do to reproduce the issue. Include any required account setup,
configuration, requests, commands, and expected results. We should be able to
follow the steps without having to guess or ask for missing details.

All reports must be accompanied by a proof of concept that we can reproduce. It
must demonstrate actual exploitation of the reported vulnerability, rather than
only describing a theoretical issue.

### Required security-boundary statement

Every report must answer these questions:

1. Which account or user is the victim?
2. Is the victim different from the reporter?
3. What private data or capability becomes accessible?
4. Which PythonAnywhere access-control or isolation boundary is bypassed?
5. Does the proof of concept require the victim to upload, publish, paste,
   execute, or open attacker-supplied content?

If the only affected account is yours, or the reported data was published
through a web app or public file location that you control, the report is
self-pwnage and is out of scope. Reports that do not identify a crossed security
boundary may be closed without further investigation.


## Payouts

* We only pay out bug bounties to the first report (not subsequent reports of the same bug).
* We pay US$50-100 for bug reports that we deem low severity, or which need a very
  complicated and unlikely sequence of events to be exploited.
* We pay US$100-500 for bugs that we deem more serious, and are directly exploitable.
* We may pay upwards of US$1000 for bugs that we deem very high severity.
* Payouts are made by PayPal, and you are responsible for any fees you incur receiving the payout.

## Not a bugs - common source of security researchers confusion

* Users can create multiple accounts with one email.
