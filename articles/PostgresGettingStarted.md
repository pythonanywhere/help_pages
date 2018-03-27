
<!--
.. title: Getting Started with Postgres
.. slug: PostgresGettingStarted
.. date: 2017-09-07 10:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


## Activate your server

If you haven't activated your postres server yet, see [this page](/pages/Postgres/)

## Create your superuser password

On the **Databases tab**, find the "Postgres Superuser password" form and
enter a password.  Note the instructions re: it being stored in plaintext and
needing to be different from your regular acount password

## Create a database and user for your app

It's a bad idea to use the superuser account in your actual web app -- for
security you want difffernt postgres user accounts for each of your applicatons.

Setting up a new database and user is quite straightforward though.  Open a
**Postgres console** from the databases tab, and then enter some commands like this,
adjusting your username, database name, and password as appropriate:


```sql
CREATE DATABASE myappdb;

CREATE USER myappuser WITH PASSWORD 'a-nice-random-password';

ALTER ROLE myappuser SET client_encoding TO 'utf8';
ALTER ROLE myappuser SET default_transaction_isolation TO 'read committed';
ALTER ROLE myappuser SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE myappdb TO myappuser ;
```

## Make a note of your postgres configuration:

From the **Databases tab**:

* Hostname (eg *myusername-667.postgres.pythonanywhere-services.com*)
* Port (eg *10667*)

From the **Console session just now**

* User (eg *myappuser*)
* Password (eg *a-nice-random-password*)


## Example Configuration for Django:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'myappdb',
        'USER': 'myappuser',
        'PASSWORD': 'a-nice-random-password',
        'HOST': 'myusername-667.postgres.pythonanywhere-services.com',
        'PORT': 10667,
    }
}
```


## Set up regular backups

Do it now!  Read [this article](/pages/RegularPostgresBackups/) for tips.

