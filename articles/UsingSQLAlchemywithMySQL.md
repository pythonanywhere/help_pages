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

MySQL servers close connections if they have been inactive for more than a specific
amount of time -- for the servers on PythonAnywhere, that's set to 5 minutes (300
seconds).  If you're using SQLAlchemy to pool your connections,
and it tries to use one that was left unused for that long, then you'll get an
error -- normally something like this:

    2013, 'Lost connection to MySQL server during query'

The good news is that the developers of SQLAlchemy have added configuration
settings that you can use so that it will discard connections that are old
enough to have timed out.  If you set that to a number smaller than 300, and
everything should work fine; we recommend 280 seconds, just to allow for a margin
of error.

If you're using SQLAlchemy directly, you configure it like this:

    :::python
    engine = create_engine('mysql+mysqldb://...', pool_recycle=280)

If you're using the Flask-SQLAlchemy plugin, then for recent versions you
configure it like this:

    :::python
    app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {'pool_recycle' : 280}
    db.init_app(app)

For older versions (before version 2.4.0), you use slightly different configuration:

    :::python
    app.config["SQLALCHEMY_POOL_RECYCLE"] = 280
    db.init_app(app)

