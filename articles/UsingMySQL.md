
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





##Using MySQL in PythonAnywhere


To start using MySQL, you'll need to go to the MySQL tab on your [dashboard](https://www.pythonanywhere.com/dashboard/), and set up a password. You'll also find the connection settings (host name, username) on that tab, as well as the ability to create new databases. 

You can start a new MySQL console to access your databases from this tab too, or alternatively you can open a MySQL shell with the following command from a bash shell or ssh session: 

    mysql -u USERNAME -h HOSTNAME -p


The USERNAME is the username you use to log in to PythonAnywhere and the HOSTNAME is on your Databases tab. 

To access a MySQL database from Python 2.6 or 2.7, just `import MySQLdb`. 


###MySQL with Django


To configure Django to access a MySQL database on PythonAnywhere, you need to do this in your settings file: 

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


###MySQL with Django tests


When you run Django tests that use the database, Django tries to create a database called test_&lt;original database name&gt; and that will fail because Django does not have permissions to create a new database. To run Django tests on PythonAnywhere, add a `TEST_NAME` key to your database definition in settings.py. Like this: 

    DATABASES = {
        'default': {
            'TEST_NAME': '<your username>$test_<your database name>',
             ...


We suggest you use a form like `<your username>$test_<your database name>`. Create this database from the PythonAnywhere Databases tab and Django will happily use it and run your tests. 


###MySQL with Python 3


If you're using MySQL with Python 3, you need to install a module. If you're not using a virtualenv, run: 

    $ pip3.4 install --user mysqlclient


If using a virtualenv: 

    $ workon my-virtualenv
    (my-virtualenv)$ pip install mysqlclient


...once that's completed, then the same imports/Django settings/etc as for Python 2.x will work. 


###Handling connection timeout errors


If you're seeing unexpected 'disconnected' errors, it may be due to our connection timeouts. We set a 5-minute timeout on database connections, so you'll want to handle unexpected disconnects, either manually with some sort of try/except, or, if you're using an ORM, by setting a timeout on the longevity of workers in your connection pool. SQLAlchemy has a pool_recycle argument, for example: <http://docs.sqlalchemy.org/en/rel_0_9/core/pooling.html#setting-pool-recycle>
