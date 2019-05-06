<!--
.. title: Setting the timezone
.. slug: SettingTheTimezone
.. date: 2019-05-06 13:23:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

## How to specify the timezone for your code

The server time is always UTC, but you can change which timezone your code runs
with by using the TZ environment variable.  For example, if you are on the
US East Coast, you can add this to your .bashrc file:

    export TZ="America/New_York"

...then code you run in consoles and scheduled/always-on tasks will run with
New York time.  For websites, you need to do something similar at the top of the
WSGI file:

    import os
    os.environ["TZ"] = "America/New_York"

For the correct specification strings for other timezones, check out
[this Wikipedia page](https://en.wikipedia.org/wiki/List_of_tz_database_time_zones)