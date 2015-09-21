
<!--
.. title: CherryPy on PythonAnywhere
.. slug: UsingCherryPy
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



[CherryPy](//www.cherrypy.org/) has its own built-in server, but that won't work well on PythonAnywhere. In order to use [CherryPy](//www.cherrypy.org/), you need to make it serve through WSGI and link that up to the PythonAnywhere web-serving infrastructure. Here is a simple [CherryPy](//www.cherrypy.org/) application that will run well on PythonAnywhere:

  * Create a "Manually configured" web app * Edit the wsgi file so it looks something like this:

        :::python
        import sys
        sys.stdout = sys.stderr

        import atexit
        import cherrypy

        cherrypy.config.update({'environment': 'embedded'})

        if cherrypy.__version__.startswith('3.0') and cherrypy.engine.state == 0:
            cherrypy.engine.start(blocking=False)
            atexit.register(cherrypy.engine.stop)

        class Root(object):
            def index(self):
                return 'Hello World!'
            index.exposed = True

        application = cherrypy.Application(Root(), script_name='', config=None)


to use it for your own app, just replace the Root class with your own in the script.

Note that to use cherrypy with Python3, you will need to install it first. Run `pip3.4 install --user cherrypy` if you are not using a virtualenv.
