
<!--
.. title: Typing problems international
.. slug: TypingProblemsInternational
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


Unfortunately there is a bug in the JavaScript terminal emulator that provides our web-based consoles -- for certain keyboard layouts, eg. AZERTY on MacOS, it fails to recognise certain characters, like right-bracket.

This seems to happen only for specific languages' keyboard layouts in specific browsers -- Firefox tends to be slightly worse than Chrome. We do have some ideas for a fix, but unfortunately it would only work in Chrome.

If you see the problem in one browser, and you're able to use another (eg. you see it in Firefox, but are able to use Chrome) then that's probably the best solution. If that doesn't work for you, one possibility is to use [SSH](/pages/SSHAccess). This isn't as simple as the web-based consoles, but should give you access to the system (unless you're behind a firewall that doesn't allow SSH, or are using a machine where you can't use SSH, of course).

SSH access to PythonAnywhere is normally only available to paying customers, but if you're having keyboard problems like this, then email us (use the "Send feedback" link above) and we'll switch it on for you.
