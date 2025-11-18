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

* SQLite, which is available for everyone.  As it relies on the file system, it runs a bit slower on the cloud -- we
  don't recommend it as a production database.
* [MySQL](/pages/UsingMySQL), which is available on all paid accounts and [free accounts created before 2026-01-15](/pages/FreeAccountsFeatures).
* [Postgres](/pages/Postgres) in available in paid plans only, as an add-on.

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
