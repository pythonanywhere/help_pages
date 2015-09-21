
<!--
.. title: Using tornado
.. slug: UsingTornado
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->




[Tornado](//www.tornadoweb.org/) is a Python web framework and asynchronous networking library. You can write Tornado web apps on PythonAnywhere, but you won't be able to use all of Tornado's features.

PythonAnywhere web applications are connected to clients (ie. users' web browsers) using a protocol called WSGI. WSGI is designed for traditional web apps, where the client makes a request to the server for a specific resource, and is given the resource. Each request for a new page (or image, or other file) is made in a different request, and there is no way for the server to push data to the client.

Tornado, however, is optimised for asynchronous communication with client web browsers -- that is, a client opens a connection, but then the connection is kept open and the server can push data back to the client. This doesn't work with WSGI, so it doesn't work on PythonAnywhere.

However, if you're using Tornado as a web framework and don't care about the asynchronous stuff, you can use it on PythonAnywhere. Here's a step-by-step guide:

  * Go to the "Web" tab
  * Create a new web app, using the "Manual configuration" option.
  * Edit the WSGI file (there should be a link when you get the "All done" message on the web tab)
  * Replace the code in the WSGI file with this:

        :::python
        import tornado.web
        import tornado.wsgi

        class MainHandler(tornado.web.RequestHandler):
            def get(self):
                self.write("Hello from Tornado")

        application = tornado.wsgi.WSGIApplication([
            (r"/", MainHandler),
        ])


Visit your app, and you should get the results you expect.

For more information about Tornado and WSGI, check out [this page in the Tornado docs](//www.tornadoweb.org/en/stable/wsgi). One thing to keep an eye out for -- in their example, they create a WSGI server to serve up the Tornado app:

    :::python
    server = wsgiref.simple_server.make_server('', 8888, application)
    server.serve_forever()


**Don't** do that on PythonAnywhere -- it will break your web app completely.
