
<!--
.. title: RAM limits
.. slug: RAMLimit
.. date: 2017-04-18 18:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Because system RAM is one of the most scarce resources on the PythonAnywhere servers,
we limit your processes to a maximum in-memory size of 3GB.  This is a *per-process*
limit, not a system-wide one, so if you have larger memory needs, you may be able
to do the processing you need by running multiple smaller processes.

If a process goes over the memory limit, it will be killed.  You will normally
get an email about this, unless you have previously unsubscribed from our
tarpit emails, or from all communications from us.
