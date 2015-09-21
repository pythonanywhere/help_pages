
<!--
.. title: What are "CPU seconds"?
.. slug: WhatAreCPUSeconds
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



With every PythonAnywhere account, you get a number of CPU-seconds included each month.
This applies to all code run through our in-browser consoles, and in your scheduled tasks.
It does not currently apply to your web apps.

A CPU-second is one second of full-power usage on a CPU with approximately 3 Amazon Compute Units
(which means double what they [define here](//aws.amazon.com/ec2/instance-types/) as
"equivalent CPU capacity of a 1.0-1.2 GHz 2007 Opteron or 2007 Xeon processor").
Your code only uses up CPU seconds while it's actually busy. If your code isn't
using any CPU power (maybe it's not running, or it's waiting for input or for a
web request to return) then it's not using any CPU seconds.

If you use up all of your included CPU seconds, don't worry! You can always buy
more — and even if you don't, your processes will still run, in the tarpit.

Tarpitted processes run at a lower priority than users who haven't hit their
limit yet, but they get any spare capacity that we have on our server cluster,
unless they're using gigabytes of RAM.

Here's [more info about the tarpit](https://www.pythonanywhere.com/tarpit/).
