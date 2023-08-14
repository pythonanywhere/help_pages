
<!--
.. title: Kinds of databases
.. slug: KindsOfDatabases
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

## Databases available

There are three databases built in to PythonAnywhere:

* MySQL, which is available for every user
* SQLite, which is also available for everyone, but runs a bit slowly on our system -- we
  recommend you only use it for testing or for scripts that don't do a lot of processing.
* [Postgres](/pages/Postgres) in available in paid plans only, as an add-on.

We're considering adding built-in support for MongoDB and Redis in the future --
if you're interested in it (or something else entirely), let us know!

### Connecting to external databases

If you have a paid plan, you can connect to databases outside PythonAnywhere.  This
means that you can get, say, a Redis instance from [Redis](https://redis.com/),
a MongoDB instance from [mLab](https://mlab.com/)
(check out [this help page](/pages/MongoDB) for some hints about that), or a
[Microsoft SQL Server](/pages/MSSQLServer) instance from
[Azure](https://azure.microsoft.com/), and connect to it from your code.  If the
provider you choose has the option to place your database in a specific Amazon Web
Services Availability Zone, then putting it in:

- `us-east-1`, if your account is on our **US** branch (you log in via [www.pythonanywhere.com](https://www.pythonanywhere.com))
- `eu-central-1`, if your account is on our **EU** branch (you log in via [eu.pythonanywhere.com](https://eu.pythonanywhere.com))

will put it very close to our servers and give the best performance.
