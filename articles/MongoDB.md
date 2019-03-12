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

Many of our customers are using [mLab](https://mlab.com/) and [MongoDB Atlas];
for best performance, you should provision your server in the AWS us-east-1
datacenter.


# Connecting to it.

If you're connecting from a console or a scheduled task, just use the regular
[PyMongo](https://api.mongodb.com/python/current/), creating a `MongoClient`
object with the normal parameters
to specify the server, the username and the password..

If you're connecting from a web app, there are a few extra parameters to add:

    connectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True, connect=False, maxPoolsize=1

These are necessary to make it work without threads in a multiprocessing environment.

# Whitelisting your IP address for MongoDB Atlas

MongoDB Atlas requires you to provide the IP address of any code that is trying
to connect to your Mongo instance; this can be a bit tricky on PythonAnywhere,
because the precise IP address will depend on the time your code runs, and
whether it's running in a website's code, or in a task, or in a console.

However, they do provide an API to tell them about new IP addresses that they
should allow to connect, so you can combine that with the
[ipify service](https://www.ipify.org/), which tells you what IP address your
code is using right now, to make your code automatically whitelist the IP it's
running on when it starts up.  Nicolas Oteiza has kindly provided us with code
to do that; you just need to
[install the ipify module](https://help.pythonanywhere.com/pages/InstallingNewModules/) and then use this,
replacing the bits inside the `<>`s:


    import requests
    from requests.auth import HTTPDigestAuth
    from ipify import get_ip

    base_url = "https://cloud.mongodb.com/api/atlas/v1.0"
    GROUP_ID = '<your-group-or-project-id>'
    whitelist_ep = "/groups/" + GROUP_ID + "/whitelist"
    url = '{}{}'.format(base_url, whitelist_ep)

    ip = get_ip()

    r =requests.post(
        url,
        auth=HTTPDigestAuth('<your-mongo-user-name>', '<your-api-key>'),
        json=[{'ipAddress': ip, 'comment': '<your-comment>'}]  # the comment is optional
    )



