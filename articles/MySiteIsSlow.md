
<!--
.. title: Why is my site slow?
.. slug: MySiteIsSlow
.. date: 2017-12-22 12:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


There's nothing more annoying than a slow website!  OK, there's lots of things.
But a slow website is annoying for sure.  Especially when it's one you've built
yourself!  Here's a few tips on fixing that problem...


## Start by measuring: What is slow?

The first steps in debugging a slow site is to figure out exactly *which* parts are slow:

* The network transit time?
* The webapp itself?
* The database?
* The filesystem?
* Interactions with 3rd party services?
* Busy loops?
* Something else?


## Deriving network transit time using developer tools in your browser, plus your access log

The best place to measure the total time taken from start to finish for your site is by
looking in the "developer tools" control panel in your browser.

* **TIP**: _In Chrome and Firefox, you can open up dev tools with the shortcut "Ctrl+Shift+i"._

Head over to the "network" tab and see how long requests are taking to make the full
round-trip to your site.

Next, open up your **access log** from the Web tab on PythonAnywhere.  In there, you'll see that
the total *response time* is logged for each request.  That's the total time taken from the moment
our servers see the request come in from the user, to the moment we send them back a response.

    141.101.98.XXX - - [22/Dec/2017:12:16:24 +0000] "GET / HTTP/1.1" 200 5300 "-" "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:58.0) Gecko/20100101 Firefox/58.0" "81.136.198.183, 141.101.98.208" response-time=0.035

* **TIP**: _The total time from dev tools minus the response time from the access log = the network transit time_

It takes of the order of 100-200ms each way for packets to cross the Internet, so somewhere between 200ms and 400ms
is probably the best you're going to get for a site.  Our servers are on the East coast of the USA, so the further
away from there you are, the longer it will take.


## Adding print debugs to your code

Assuming you've determined it's the actual webapp that's slow, and not the Internet -- so, perhaps your webapp
is taking several seconds to respond to each request?  -- a few print statements sprinkled through your code
should help you determine what actual parts of your code are being slow.

Here's an example:

```python
from datetime import datetime

def my_view_function(request):
    print('{timestamp} -- request started'.format(timestamp=datetime.utcnow().isoformat())
    # rest of your code as before

    print('{timestamp} -- request started'.format(timestamp=datetime.utcnow().isoformat())
    return resposne


At the very least, you'd want some prints at the beginning and end of your views, then perhaps also:

* inside any for-loops
* before and after any database queries
* before and after anything that reads or writes from the filesystem
* before and after any external API calls or calls to third-party services

```


## Common sources of slowness


### Not enough workers

One webapp worker can only deal with one request at a time.  If you have lots of concurrent users, or if each page has lots of different static assets, then you may need to upgrade to get more workers


### The filesystem

Due to the distributed nature of our network filesystem, reading and writing to files on PythonAnywhere can be quite slow


### SQLite

Closely related to the above - because SQLite uses the filesystem, it can be quite slow on PythonAnywhere.  In addition, there are know problems with using SQLite on a network filesystem when you have multiple processes / workers all trying to use the database at the same time.  That's why we recommend you never use SQLite in a production webapp


* **TIP**: _Switch to MySQL or Postgres for a speedup_


###  Busy loops in your code

You don't need to be an expert in big-O notation to be able to guess that loops, particularly nested loops, can get slower an slower.  Look out for anything like this in your code:


```python
def my_view_function(request):
    things = get_things_from_db()
    for thing in things:
        for widget in thing.widgets:
            for attribute in widget.properties:
                if attribute.id == request['attribute_id']
                    return widget
```

There are three nested for loops in there!  If you have lots of things and lots of widgets and lots of attributes, that could take a very long time to complete.


* **TIP**: _Wherever you can, try to offload busy loops to the database.  The databse can search for things faster than you can in Python_


### third party services, API calls, etc

If your webapp has to make calls to third party services, that can be a cause of slowdown.


### Web scraping (particularly with Selenium)

If your webapp needs to scrape third party sites in order to retrieve data for your users, that can be very slow -- particularly if you're spinning up a real web browser with [Selenium](/pages/Selenium/).

Switch to using an [async task queue](/pages/AsyncInWebApps/) instead.


### Machine learning, number crunching, big data

If you're trying to do big number crunching, like machine learning analysis, again that's something you probably want to do asynchronously rather than directly inline in your webapp code.

Again, see this article on [moving work out of your webapp to an async task queue](/pages/AsyncInWebApps/) instead.




