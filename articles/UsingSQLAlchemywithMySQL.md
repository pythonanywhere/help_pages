
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




SQLAlchemy needs to some extra arguments to work on PythonAnywhere: 

    engine = create_engine('mysql+mysqldb://...', pool_recycle=280)


The RDS service disconnects clients after 5 minutes (300s), so we need to set the `pool_recycle` to something lower than that, or you'll occasionally see disconnection errors in your logs. 
