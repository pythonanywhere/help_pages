
<!--
.. title: 400 Bad Request error from Django
.. slug: Django400BadRequest
.. date: 2016-03-09 13:53:04 UTC+00:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Are you looking at an error message from a Django application that says

    400 Bad Request


Unfriendly huh?   It's a common django problem though (as you'll see from a 
[quick google search](https://www.google.com/?q=django+400+bad+request),
and the answer is that you need to set the `ALLOWED_HOSTS` setting in your
*settings.py* (or switch `DEBUG` back to True)

More info in the [django documentation](https://docs.djangoproject.com/en/1.9/ref/settings/#allowed-hosts)

