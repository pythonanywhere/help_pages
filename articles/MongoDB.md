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
external provider (many of our customers are using [MongoDB Atlas](https://www.mongodb.com/cloud/atlas)).
For best performance, you should provision your server in the AWS `us-east-1`
datacenter if you're using our US-based site at `www.pythonanywhere.com`, or the
`eu-central-1` datacenter if you're using our EU site at `eu.pythonanywhere.com`.

Because this will require non-HTTP external Internet access,
you'll need a paid account.

There is a complete step-by-step tutorial on [our blog](https://blog.pythonanywhere.com/178/).


# Connecting to it.

If you're connecting from a console or a scheduled task, just use the regular
[PyMongo](https://pymongo.readthedocs.io/), creating a `MongoClient`
object with the normal parameters
to specify the server, the username and the password..

If you're connecting from a web app, and you're using Flask, we recommend that
you use the [Flask-PyMongo](https://flask-pymongo.readthedocs.io/en/latest/)
extension, which works well in a multiprocessing environment like websites
on our system.

If you're just using the "raw" PyMongo API, there are a few extra parameters
you need to to add to your call to
`pymongo.MongoClient`:


For pymongo < 4:

    connectTimeoutMS=30000, socketTimeoutMS=None, socketKeepAlive=True, connect=False, maxPoolsize=1


For pymongo >= 4:

    connectTimeoutMS=30000, socketTimeoutMS=None, connect=False, maxPoolsize=1

This handles the bulk of the stuff that would otherwise be handled by Flask-PyMongo
if you were using it.


# Accesslist your IP address for MongoDB Atlas

MongoDB Atlas requires you to provide the IP address of any code that is trying
to connect to your Mongo instance; this can be a bit tricky on PythonAnywhere,
because the precise IP address will depend on the time your code runs, and
whether it's running in a website's code, or in a task, or in a console.

The easiest, solution, though certainly not the most secure, is to accesslist the
CIDR `0.0.0.0/0`, which is a "accesslist" containing every IP address on the Internet.

A more secure solution is to use the MongoDB Atlas API to tell them about new IP
addresses that they should allow to connect.  You can combine that with the
[ipify service](https://www.ipify.org/), which tells you what IP address your
code is using right now, to make your code automatically accesslist the IP it's
running on when it starts up.  The following code (based on code provided by
Nicolas Oteiza and modified by Amitoz Azad) will do that. You just need to replace 
the bits inside the `<>`s:


    import requests
    from requests.auth import HTTPDigestAuth

    def get_public_ip():
        response = requests.get("https://api.ipify.org")
        return response.text

    atlas_group_id = "<your group ID aka project ID -- check the Project / Settings section inside Atlas>"
    atlas_api_key_public = "<your atlas public API key>"
    atlas_api_key_private = "<your atlas private API key>"
    ip = get_public_ip()

    resp = requests.post(
        "https://cloud.mongodb.com/api/atlas/v1.0/groups/{atlas_group_id}/accessList".format(atlas_group_id=atlas_group_id),
        auth=HTTPDigestAuth(atlas_api_public_key, atlas_api_private_key),
        json=[{'ipAddress': ip, 'comment': 'From PythonAnywhere'}]  # the comment is optional
    )
    if resp.status_code in (200, 201):
        print("MongoDB Atlas accessList request successful", flush=True)
    else:
        print(
            "MongoDB Atlas accessList request problem: status code was {status_code}, content was {content}".format(
                status_code=resp.status_code, content=resp.content
            ),
            flush=True
        )


If there are any problems accesslisting your IP address (for example, if the
API key is wrong) then you will find the error messages in the program's output;
for websites, it will be in the server log file (linked from the "Web" page).

