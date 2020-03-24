<!--
.. title: Using Flask's send_file function with BytesIO
.. date: 2020-03-24 17:19:00 UTC+00:00
.. slug: FlaskSendFileBytesIO
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Flask's send_file function provides an optimised way to send a file from your
web app. However, if you pass it a `BytesIO` object, you may get one of the
following errors:

    SystemError: <built-in function uwsgi_sendfile> returned a result with an error set
    
    io.UnsupportedOperation: fileno

    
    
This happens because the server software that we use to manage your web apps
assumes that anything that is passed to it through that mechanism is an actual
file on the disk. This is not correct behavior according to the WSGI
specification and they have a fix in development that we will deploy at some
point after it is released.

In the meantime, you can work around this with code like this:

    :::python
    from io import BytesIO
    from flask import Flask, Response
    from werkzeug import FileWrapper
    
    app = Flask(__name__)
    
    @app.route('/')
    def hello_world():
        b = BytesIO(b"blah blah blah")
        w = FileWrapper(b)
        return Response(w, mimetype="text/plain", direct_passthrough=True)
        
    
This uses the built-in Flask FileWrapper, which does support in-memory
file-like objects and avoids the use of the server's optimisation that does not
work.
