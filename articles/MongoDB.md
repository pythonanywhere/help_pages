<!--
.. title: Using MongoDB on PythonAnywhere
.. slug: MongoDB
.. date: 2018-04-06 18:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


# Getting a MongoDB server

We don't provide Mongo servers ourselves, so you'll need to get one from an
external provider.  Because this will require non-HTTP external Internet access,
you'll need a paid account.

Many of our customers are using [mLab](https://mlab.com/); for best performance,
you should provision it in the AWS us-east-1 datacenter.

# Connecting to it.

If you're connecting from a console or a scheduled task, just use the regular
[PyMongo](https://api.mongodb.com/python/current/), creating a `MongoClient`
object with the normal parameters
to specify the server, the username and the password..

If you're connecting from a web app, there are a few extra parameters to add:

    connectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True, connect=False, maxPoolsize=1

These are necessary to make it work without threads in a multiprocessing environment.
