<!--
.. title: Using MySQL
.. slug: UsingMySQL
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

To start using MySQL, you'll need to go to the MySQL tab on your
[dashboard](https://www.pythonanywhere.com/dashboard/), and set up a password.
You'll also find the connection settings (host name, username) on that tab, as
well as the ability to create new databases.

You can start a new MySQL console to access your databases from this tab too, or
alternatively you can open a MySQL shell with the following command from a
bash console or ssh session:

    :::bash
    mysql -u USERNAME -h HOSTNAME -p 'USERNAME$DATABASENAME'


In this:

* The `USERNAME` is the username you use to log in to PythonAnywhere
* The `HOSTNAME` is on your Databases tab
* The `'USERNAME$DATABASENAME'` is the full name of your database, which comprises
  your username, then a dollar sign, then the name you gave it.  The single quotes
  around it are important!  If you don't put them in there, bash will try to interpret
  the `$DATABASENAME` as an [environment variable](http://tldp.org/LDP/Bash-Beginners-Guide/html/sect_03_02.html),
  which will lead to an error saying `ERROR 1044 (42000): Access denied for user 'USERNAME'@'%' to database 'USERNAME'`

When you run the command, it will prompt you for a password -- use the one you
entered on the Databases tab.


## Accessing MySQL from Python

The appropriate libraries are installed for all versions of Python that we
support, so if you're not using a virtualenv, to access a MySQL database
just `import MySQLdb`.

If you *are* using a virtualenv, you'll need to install the correct package
yourself.  Start a bash console inside the virtualenv, then:

For Python 2.7

    pip install mysql-python

For Python 3.x

    pip install mysqlclient



## MySQL with Django


To configure Django to access a MySQL database on PythonAnywhere, you need to do
this in your settings file:

    :::python
    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.mysql',
            'NAME': '<your_username>$<your_database_name>',
            'USER': '<your_username>',
            'PASSWORD': '<your_mysql_password>',
            'HOST': '<your_mysql_hostname>',
        }
    }


Again, you can get the username and hostname details from the "Databases" tab.


## MySQL with Django tests


When you run Django tests that use the database, Django tries to create a
database called *test_&lt;original database name&gt;* and that will fail because
Django does not have permissions to create a new database. To run Django tests
on PythonAnywhere, add a `TEST` key to your database definition in
`settings.py`. Like this:

    :::python
    DATABASES = {
        'default': {
             ...
            'TEST': {
              NAME: '<your username>$test_<your database name>',

More info here: https://docs.djangoproject.com/en/1.10/ref/settings/#test

We suggest you use a form like `<your username>$test_<your database name>`.
Create this database from the PythonAnywhere Databases tab and Django will
happily use it and run your tests.


## MySQL with web2py
To use MySQL with web2py, you'll need to change your DAL constructor:

    :::python
    db = DAL('mysql://<your_username>:<your_mysql_password>@<your_mysql_hostname>/<your_database_name>')


## Handling connection timeout errors


If you're seeing unexpected 'disconnected' errors, it may be due to our
connection timeouts. We set a 5-minute timeout on idle database connections, so
you'll want to handle unexpected disconnects, either manually with some sort of
try/except, or, if you're using an ORM, by setting a timeout on the longevity
of workers in your connection pool. SQLAlchemy has a pool_recycle argument,
for example: <http://docs.sqlalchemy.org/en/rel_0_9/core/pooling.html#setting-pool-recycle>


## Backup and restore

See [this article on mysqldump](/pages/MySQLBackupRestore).
