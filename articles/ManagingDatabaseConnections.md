
<!--
.. title: Managing database connections
.. slug: ManagingDatabaseConnections
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



A couple of different problems can occur if your app isn't managing its database connections carefully: 


## Dealing with OperationalError 1226, User has exceeded the max_user_connections resource


Are you having trouble with problems like this: **OperationalError: (1226, "User '&lt;username&gt;' has exceeded the 'max_user_connections' resource (current value: X")**? 

If you're seeing this problem consistently, it means that you have several,
simulateneous processes that are all holding on to their database connections
and are stuck, refusing to release them. This shouldn't happen in the normal,
day-to-day operation of a web application, so it means something is wrong: some
part of your code isn't cleaning up its database connections properly. 

Make sure you're using a well known ORM (like Django's, or SQLAlchemy), and
make sure its options for connection pooling and clean-up are well set. 

If you're managing database connections yourself manually, make sure that you
close connections tidily after each use, even if there's an error -- for
example, consider using `try/finally`, and put a `connection.close()` into the
`finally` clause... 


## Dealing with OperationalError 2006, 'MySQL server has gone away' and 2013, 'Lost connection to MySQL server during query'

Are you having trouble with problems like this:
**OperationalError: (2006, 'MySQL server has gone away')**? 
Or **(2013, 'Lost connection to MySQL server during query')**

Our databases have a 300-second (5-minute) timeout on inactive connections.
That means, if you open a connection to the database, and then you don't do
anything with it for 5 minutes, tnen the server will disconnect, and the
next time you try to execute a query, it will fail.


### 1. configure your ORM

Some Python frameworks have object relationship managers (ORMs) that manage a
pool of database connections for you. If you're using an ORM (like Django's
or SQLAlcheny) then you need to configure it to automatically expire/recycle
connections at 300 seconds.

Django does this by default.  SQLAlchemy needs a little extra help,
by setting `pool_recycle` to 280.  [More info here](/pages/UsingSQLAlchemywithMySQL/).


### 2. handle errors manually

If you're not using an ORM, you need to handle errors manually. MySQLdb
specifically does not manage the connections and will error if you try to reuse
a stale connection. One that has closed or expired. You need to explicitly
check for this error case and handle it. 

Even if you are using an ORM, under certain circumstances, it won't automatically
recycle connections for you (this might happen if you have some long-running task
that opens a connection at the beginning for example).


#### Handling errors manually for MysqlDB:

Below is some example code from a [stackoverflow answer](//stackoverflow.com/questions/207981/how-to-enable-mysql-client-auto-re-connect-with-mysqldb)

```python
import MySQLdb

class DB:
  conn = None

  def connect(self):
    self.conn = MySQLdb.connect()

  def query(self, sql):
    try:
      cursor = self.conn.cursor()
      cursor.execute(sql)
    except (AttributeError, MySQLdb.OperationalError):
      self.connect()
      cursor = self.conn.cursor()
      cursor.execute(sql)
    return cursor

db = DB()
sql = "SELECT * FROM foo"
cur = db.query(sql)
# wait a long time for the Mysql connection to timeout
cur = db.query(sql)
# still works
```


#### Anticipating errors in Django

If you have some code that waits a long time in between database queries,
then calling `connection.close()` will anticipate any problems with the
server timeout:

```python
from django.db import connection

make_a_database_query()

call_function_that_takes_a_long_time()

# if this last takes longer than 5 mins
# then the next db function might error so

# call connection.close to get a new connection:
connection.close()
make_another_query()
```


