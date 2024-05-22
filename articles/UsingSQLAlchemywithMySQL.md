<!--
.. title: Using SQLAlchemy with MySQL
.. slug: UsingSQLAlchemywithMySQL
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

SQLAlchemy is a really useful ORM/connection manager that makes it much easier
to connect to databases from your code, especially if you're writing a website
using a framework with no built-in database management tools -- for example, if
you're using Flask.

## Connecting to MySQL using SQLAlchemy

SQLAlchemy expects a URI to tell it how to connect to the MySQL database.  This
is of the format

```python
"mysql+mysqldb://{username}:{password}@{hostname}/{databasename}"
```

...where the `{username}` is the one shown on the "MySQL" tab of the databases
page inside PythonAnywhere, the `{password}` is the one you specified on that
tab, the `{hostname}` is also the one from that tab, and the `{databasename}` is
the name of one of your databases -- don't forget that the database name starts
with your username, then a dollar sign, and then the part of the name that you
specified when you created it.


## Configuring SQLAlchemy

One particular setting that you need to get right if you're using it is the
`pool_recycle`.  This tells SQLAlchemy how long a database connection can be
left unused before it should be discarded; it's important because connections
get closed on the server side if they're inactive for more than a specific amount
of time -- 300 seconds on PythonAnywhere.  If you try to use a connection that
has been closed that way, you'll get an error like this:

```
2013, 'Lost connection to MySQL server during query'
```

### How to configure Flask-SQLAlchemy

If you're using Flask-SQLAlchemy, you need to specify the `pool_recycle` setting
when you initialise the `SQLAlchemy` object.  For example:

```python
    db = SQLAlchemy()
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle' : 280}
    db.init_app(app)
```

Or

```python
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle' : 280}
    db = SQLAlchemy(app)
```

For older versions (before version 2.4.0), you use slightly different configuration:

```python
    app.config["SQLALCHEMY_DATABASE_URI"] = SQLALCHEMY_DATABASE_URI
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 280
    db.init_app(app)
```

### Using SQLAlchemy directly

If you're using SQLAlchemy directly, you configure it like this:

    :::python
    engine = create_engine('mysql+mysqldb://...', pool_recycle=280)


## Using Flask-SQLAlchemy outside view functions in websites

Sometimes you will continue to get connection errors when using Flask-SQLAlchemy in a
website even when you've set `pool_recycle` correctly.  They can look like the
one above, or they can look like this:

```
sqlalchemy.exc.OperationalError: (mysql.connector.errors.OperationalError) MySQL Connection not available.
```

The most common cause
of this is if you are accessing the database from outside a view function.

The problem is caused by the way websites are loaded up on PythonAnywhere.  When
a website’s code is started, we spin up one process for it, which loads up all
of your code, doing all of the imports and so on.  As as side-effect, this will
run all code that is outside view functions.

Once that’s done, and the code is all loaded, we fork off the multiple worker
processes that handle incoming requests to your site.

What that means is that if you do some DB access through SQLAlchemy outside your
views, a connection to the database will be created before the fork, and then
each forked process will have a copy of the same connection.  Then, if multiple
processes try to use that connection, they’ll interfere with each other and
you’ll get a connection error.

The best solution to this is simply to not access the database from code outside
view functions.

However, a hack that should work if you really need to access the DB while your
code is starting up is to do this afterwards:

```python
db.session.close()
db.get_engine(app).dispose()
```




