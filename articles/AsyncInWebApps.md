
<!--
.. title: Async work in Web apps
.. slug: AsyncInWebApps
.. date: 2017-07-21 11:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


## Doing work asynchronously in web apps

### Web apps are meant to respond quickly

Web apps are supposed to respond quickly to browser requests.  The
request/response cycle, at least in our model, is meant to be fast,
a matter of a few seconds, or better yet a fraction of a second.

For that reason we set a 5-minute timeout on all web workers.  If
they can't respond to a request in under that time, they're assume
to have accidentally hung, and are restarted.


## But what if I want to do some heavy processing?

But you might legitimately have some "slow" work you want to
do in response to a user request.  You may be doing some
number-crunching, or wanting to pull down lots of data from
third party services, and collate it for the user.

## The Async solution: a task queue

The solution is to use some sort of task queue, and complete
the work asynchronously. 

Here's a high-level overview of what a solution could look like
(everyone's requirements are different, so adapt this to your own
neeeds):

* register the user's request for work somewhere by storing
  the details of the request somewhere, eg on the filesystem,
  or in a table in your database

* respond immediately to the user and let them know the request
  is now in state "pending"

* set up an **Always-on task** (if you have a paid account). You can use a
  **Scheduled task** instead, if you don't have a paid account, but your queue
  will only be processed when the scheduled task is scheduled. The job of the
  task is to monitor your task queue (eg the database), and pick jobs off one
  by one. Include some code to update the job status (eg, pending, under way,
  complete...)

* give the user a way of checking on the progress of the job, either
  by asking them to refresh the page, or perhaps setting up an 
  Ajax polling system.


See [our help page on long-running tasks](/pages/LongRunningTasks) for
information on how to set up an "always-on" task to do your async work.


## Don't jump to using async too quickly

It's easy to take this too far.  If all you're doing is wanting to send
the user an email, say, then just doing it synchronously in the request
is probably fine.  A task queue is probably premature optimization at this
point, and if you have performance concerns, you should see how far you can
scale by just adding web workers.

A rule of thumb might be: if your work is taking more than 30 seconds, it's
worth thinking about a task queue.


## FAQ

* *Can I use celery?* -- at the moment the answer is no.  We're working on it.

* *Can I just use threads?* -- we don't support threads in web apps, no

* *What about using a subprocess / multiprocessing?* -- although  you *can* kick
  off subprocesses from web apps, we don't recommend it.  Any subprocesses that
  seem to be hanging around longer than a single request/response cycle are
  assumed to be orphan processes by the system, and are liable to get killed at
  unpredictable times.
