
<!--
.. title: Migating Web2py from SQLite to MySQL
.. slug: MigatingWeb2pyFromSQLiteToMySQL
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->




*From PythonAnywhere user mjbeller [in the forums](https://www.pythonanywhere.com/forums/topic/1288/#id_post_8992)*

I've been using web2py and sqlite for both prototyping and the first version of an application. For both performance and scalability, I need to move to MySQL. Over the past week I've experimented with several options and here's what worked for me (and hope this helps others) ...

The web2py book describes two methods:

  * [export/import all data using CSV files](<http://web2py.com/books/default/chapter/29/06/the-database-abstraction-layer#CSV--all-tables-at-once->)
  * [copy between databases using script cpdb.py](<http://web2py.com/books/default/chapter/29/06/the-database-abstraction-layer?search=cpdb#Copy-data-from-one-db-into-another>)

The web2py user group highlights two other options:

  * [sqlite .dump and mysql migration](http://www.realpython.com/blog/python/web2py-migrating-from-sqlite-to-mysql/#.Ulm3xmTTXCU)
  * [Mariano/Alan Etkin experimental script](https://groups.google.com/d/msg/web2py-developers/QxeJNByj6qc/cpBHsa1ymUkJ)

I couldn't get cpdb to work except for a simple model. I'm still learning both python and web2py and couldn't debug the script but believe it has something to do with the sequence and dependencies between tables (I have about 12 tables with numerous foreign keys). This is also true of using sqlite .dump and mysql migrate (and I also felt this bypassed web2py which requires a fake_migrate and preferred an option "within" web2py since I'm also learning MySQL at the same time).

The experimental script seemed straightforward but

1. I wasn't sure how to execute the script with both DAL's simultaneously and
2. the primary advantage over CSV export/import is the retention of the source row id's (which isn't needed if you start with a new database schema - see my comments below).

In the end, I used the following procedure using web2py CSV export/import to move my production sqlite db to mysql (which only took about 7 minutes to execute after learning/testing/experimenting with the various options) ...

1. Export all data in CSV format
    1. open console and navigate to the web2py folder
    1. start web2py in interactive console mode with:
        * `python web2py.py -S your_app_name -M –P`
    1. export data in csv format with
        * `db.export_to_csv_file(open('your_app_name_export.csv', 'wb'))` [this stores the file in the root of the web2py directory]
    1. exit web2py interactive console mode with `exit()`
2. Prepare web2py application for new database and create new database
    1. in console, navigate to application folder
    1. backup existing SQLite database (and corresponding .table files) with:
        * `cp -r databases databases_bak`
    1. create empty databases folder with:
        * `rm -r databases; mkdir databases`

    1. change DAL connection string in app to:
        * `db = DAL('mysql://user_name:password@user_name.mysql.pythonanywhere-services.com/database_name')` [for pythonanywhere, the database_name is in the form user_name$database_name]
    1. create new empty mysql database schema (from control panel in pythonanywhere or mysql command prompt)

3. Generate database tables and load data
    1. start web2py in interactive console mode with:
        * `python web2py.py -S your_app_name -M –P` [this will execute the models and generate the mysql database tables and the .table files in the database directory]
    1. import data in csv format with:
        * `db.import_from_csv_file(open('your_app_name_export.csv', 'rb'))`
        * `db.commit() # this is missing from some of the other instructions but is required`
    1. exit web2py interactive console mode with:
        * `exit()`

4. Celebrate!

If you start with a new empty database, all record id's will be the same as the source database (and all foreign key references are maintained). If the database had previous transactions, the new data will maintain all foreign key references but the id's will not match the source data (which is only important if there are any code or external references to specific id's as Alan pointed out in his posts).
