<!--
.. title: Global State and Web Apps
.. slug: GlobalStateAndWebApps
.. date: 2021-10-20 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

There are a few problems that we see on PythonAnywhere that relate to using
global state in a web app. Here are some examples:

* Information read from a database or file is only updated when the web app is reloaded
* Data for one user is being seen by another user
* Data from a user is being lost between requests

To understand what is causing these problems, we need to understand a little
about how PythonAnywhere web apps are loaded and run.

## How web apps are run on PythonAnywhere
When a web app is started (or reloaded), the code that defines the web app is
executed and then separated into the number of workers for the web app. Each
worker is a separate process that is isolated from the other workers. 

A web worker is a process that handles requests that are send to your web app.
Each worker handles only one request at a time. Free accounts have one worker
per web app and paid accounts will have 2 or more.

Now let's look at each of the problems above. We will use Flask in our example
code for simplicity, but the same principles apply for other frameworks.

### Information read from a database or file is only updated when the web app is reloaded.
Here is an example Python file:

    :::python
    import module

    x = module.read_value()

    app.route("/get_y")
    def get_y():
        y = module.read_value()
        return y

    app.route("/get_x")
    def get_x():
        return x


If this file was loaded into a web app (by importing it), the import statement
and the assignment to x would be executed every time the web app was reloaded
(and not again while the web app was running). The code in the function
`get_y` would be executed each time a user makes a request to `/get_y`. For this
example, let's assume that `module.read_value` returns a different value every
time it is called.

Since the line that gets the value for x is not in a function, it will only be
executed once - when the web app is reloaded, so x will not change until the
web app is reloaded again. Therefore, every request to `/get_x` will
return the same value until the web app is reloaded, and then it will return a
different value until the next reload.

However, the line that reads the value for y is in the view function `get_y`, so
it will not be executed when the app is reloaded. It will be executed every
time a user accesses `/get_y`, so users that access `get_y` will see a new
value on every request.

#### What to do about it
Make sure that you have decided which data needs to be updated on each request
and which data needs to be constant between reloads and then place the code
that reads each of those types of data into the appropriate place.

### Data for one user is being seen by another user
Here's another example. In this example, the 2 functions `view` and `add` are view
functions that will display the items in `the_list` to a user or allow them to
add items to it.

    :::python
    the_list = []

    app.route("/view")
    def view():
        return the_list

    app.route("/add/<item>")
    def add(item):
        the_list.append(item)
        return the_list

When the web app is reloaded, `the_list` will be set to an empty list. Every
time a user accesses `/add`, an item will be added to `the_list` and `the_list` (with
the new item in it) would be shown to them. Since `the_list` was created when the
web app was loaded and every request adds an item, all users see the same list
of items.

#### What to do about it
Most web frameworks will include some way to identify different users (or just
browser sessions). They range in complexity from simple sessions all the way
up to the fully implemented user management framework that is built in to
Django. The particular choice of what to use will depend on your application.

### Data from a user is being lost between requests
Up until now, we've been only considering what happens within a single worker.
For this one, we need to start thinking about other workers. If the previous
example was run in a web app with 2 workers, then there would actually be 2
different versions of `the_list` - one in each worker. Every time a user added
an item, it would go into one of them, but not the other. It is also entirely
possible for a user to add an item to one `the_list` and then, when they go to
view it, they could see the other one. This happens because each request to a
web app is handled separately and the user can be directed to any of the workers
on any request.

#### Why does this not happen locally?
The development servers that are built in to most web frameworks run in a
single process, so there is only ever one copy of `the_list` in that one
process.

#### What to do about it
If you have data that needs to be consistent between requests, you will need to
use some way of storing it that is outside of the worker process. The most
common solution is to use a database to store the data and then make sure that
you get the newly updated data on every request:


    :::python
    app.route("/view")
    def view():
        the_list = get_list_from_database()
        return the_list

    app.route("/add/<item>")
    def add(item):
        save_item_in_the_list_table(item) 
