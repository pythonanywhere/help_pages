<!--
.. title: How many per second hits can my site handle?
.. slug: HowManyHitsCanMySiteHandle
.. date: 2021-06-05 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

The answer to this question is a little involved, because it depends on two things: how long your
code takes to handle each request, and how many worker processes you have handling
those requests.

Free accounts have one worker process handling their requests; paid accounts have
more.  For example, a Hacker account has two, a Web Dev account has three separate
workers for each of its two sites, and other account types have different amounts.
You can also customize the number -- so, for example, with a custom plan you could
have all of the normal features for a Hacker account, but upgrade to having (say)
five worker processes for your website.

It's important to understand that having multiple of worker processes doesn't change
how long your own code takes to run -- instead, it means that there are multiple
copies of your code running, which means that you can handle more simultaneous
requests.


## What happens when a request comes in to your site

Each request that comes in to PythonAnywhere is put onto a queue for the particular
site it has been sent to.  Your worker processes spend their time watching the queue for incoming requests.
When one arrives, a worker will pick it up, run your code to handle the request
and produce a response, and then return the response.  Then it will go back to
watching the queue.

This means that under normal operation, each request will be handled pretty much
in the amount of time that your code takes to run -- there is a tiny overhead for
the request going onto the queue and coming off it, but that's less
than a millisecond so you're unlikely to be able to measure it.

So if, say, your code takes 0.2 seconds to handle a typical
request, then one worker can handle 5 requests/second, two workers can handle 10/second,
and so on.


## What if you have more requests coming in than your workers can handle

Let's say that you take 0.2 seconds to handle a request and have two workers, but
then 50 requests come in within one second.  What will happen is that they will
all wind up on the queue.  The worker processes will then clear them down, between them handling
each one in turn at a rate of ten per second, so it will be five seconds before they
are all cleared.

For most sites, most of the time, this is OK.  Traffic to websites tends to be "spiky",
with long periods of few requests, followed by occasional batches of lots of requests
in quick succession.  So you might get occasional slowdowns, but it's unlikely anyone
will notice.

But obviously, if you exceed the number of requests that your worker processes can
handle for a sustained time, you'll wind up with requests piling up in the queue.
When that happens, people will see the site suddenly slow down, and eventually the
queue will fill up and they will start getting error messages (specifically, with
the error code "502-backend").

So it's important to make sure that you have enough workers to handle your traffic.


## How to estimate how many workers you need

Because this is all dependent on how long your code takes to run, the first thing
is to find out what that is!  If you look at your site's access logs, you'll see
one line for each request to the site.  At the end of each line, there is a response-time
field -- that is the number of seconds it took for the system to respond to that request,
so you can use that.

It's worth noting that what you need is the average time taken --
that will depend on which views are accessed most.  For example, if you have 9 views that
take 0.1 seconds, but one that takes 5 seconds, the average would depend on the relative
frequency that each one is hit.  If the slow view is hit rarely, it won't matter
as much as if would if it was hit frequently.

But by looking at the logs, you can come to at least a rough idea of how long your
code takes.

One warning, though -- make sure that the time slice in the log that you are looking
at is not a time during which your site was overloaded with requests.  This is because
the response time logged includes any time a request spend queued up waiting for a worker.
So if the site overloaded, the time will not be an accurate reflection of how long
your code took to run.  However, if you choose a time when things were relatively
quiet, you'll get good numbers.

Once you have that number, you can run the calculation above in reverse.  If your
code takes 0.2 seconds on average to handle a request, then one worker can handle 5
requests per second, and if you need to be able to handle 15 requests a second at
peak times of the day, that means you need three workers.


## How to find out if your workers were all busy at a particular time.

If you're looking at your logs and seeing a time when your site was slow, or if
people who use your site have contacted you to ask why it was slow at a particular
time, then sometimes it can be hard to find out whether that was because your workers
were overloaded by the number of requests, or if it was some other factor.

At present, the best way to find out if it was due to an overload is to ask us
by email at [support@pythonanywhere.com](mailto:support@pythonanywhere.com).  We do keep metrics showing how many workers
were available for each site in a database from which we can extract reports for you.
At some time in the future we'll find a way to expose this on the "Web" page to make
things a bit easier!


## Any questions?

Hopefully the above will clarify how to work out how many workers you need for your
site, but if you have any questions or suggestions on how to make things easier to
understand, just let us know via email at [support@pythonanywhere.com](mailto:support@pythonanywhere.com).







