<!--
.. title: Supported Python versions on PythonAnywhere
.. slug: PythonVersions
.. date: 2024-08-12 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Which versions of Python you have available to you depends on the
system image that your account uses.  You can see which one that is on
the "System Image" tab of the "Account" page.

The system image is essentially the
version of the operating system that your code runs under, and is set when
you initially create your account, but you can
[change it to a more recent one](/pages/ChangingSystemImage) later on.

Here are the current system images, and the Python versions that each one
supports:

|             | 2.7 | 3.5 | 3.6 | 3.7          | 3.8 | 3.9 | 3.10 | 3.11 | 3.12 | 3.13 |
|-------------|-----|-----|-----|--------------|-----|-----|------|------|------|------|
| glastonbury | X\* | X\* | X   | X            | X   | X   |      |      |      |      |
| haggis      | X\* |     | X\* | X            | X   | X   | X    |      |      |      |
| innit       |     |     |     | X\* &dagger; | X\* | X   | X    | X    | X    | X    |

\* there are no pre-installed packages for these Python versions, but you can
use them for your code; we recommend installing the packages you need using a
[virtualenv](/pages/VirtualenvsExplained).

&dagger; there's an extra restriction for [virtualenvs on Python 3.7 on the "innit" system image](/pages/Python37VirtualenvOnInnit)