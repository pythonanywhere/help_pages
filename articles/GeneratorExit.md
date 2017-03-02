<!--
.. title: GeneratorExit errors
.. slug: GeneratorExit
.. date: 2017-03-02
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Sometimes you may see errors like this in your PythonAnywhere website's error log:

    2017-02-16 13:09:32 Thu Feb 16 13:09:32 2017 - uwsgi_response_writev_headers_and_body_do(): Broken pipe [core/writer.c line 287] during GET / (10.0.0.14)
    2017-02-16 13:09:32 ERROR:root:IOError: write error
    2017-02-16 13:09:32 ERROR:root:Error running WSGI application
    2017-02-16 13:09:32 ERROR:root:GeneratorExit

You can generally ignore this specific error, unless you're getting very large
numbers of them (eg. more than one per ten hits to your website).

What it means is that a browser disconnected from your site while it was trying
to send data back.  This happens every now and then for every site -- the
Internet is never 100% reliable (especially if people are connecting to your
site from mobile devices or over unreliable wifi), so people get disconnected
and you see an error like that.

It only indicates a real problem if you see a lot of them, because that can mean
that your site is running really slowly, and people are getting impatient and
clicking away, or closing the browser tab, while it's in the process of sending
pages back to them.
