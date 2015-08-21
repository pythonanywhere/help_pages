
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


##Dealing with OperationalError 1226, User has exceeded the max_user_connections resource


Are you having trouble with problems like this: **OperationalError: (1226, "User '&lt;username&gt;' has exceeded the 'max_user_connections' resource (current value: X")**? 

If you're seeing this problem consistently, it means that you have several, simulateneous processes that are all holding on to their database connections and are stuck, refusing to release them. This shouldn't happen in the normal, day-to-day operation of a web application, so it means something is wrong: some part of your code isn't cleaning up its database connections properly. 

Make sure you're using a well known ORM (like Django's, or SQLAlchemy), and make sure its options for connection pooling and clean-up are well set. 

If you're managing database connections yourself manually, make sure that you close connections tidily after each use, even if there's an error -- for example, consider using `try/finally`, and put a `connection.close()` into the `finally` clause... 


##Dealing with OperationalError 2006, 'MySQL server has gone away'


Are you having trouble with problems like this: **OperationalError: (2006, 'MySQL server has gone away')**? 

Some Python frameworks have object relationship managers (ORMs) that manage a pool of database connections for you. Other libraries do not. MySQLdb specifically does not manage the connections and will error if you try to reuse a stale connection. One that has closed or expired. You need to explicitly check for this error case and handle it. 

Below is some example code from a [stackoverflow answer](//stackoverflow.com/questions/207981/how-to-enable-mysql-client-auto-re-connect-with-mysqldb)

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
