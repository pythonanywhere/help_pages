
<!--
.. title: Importing your local database to PythonAnywhere
.. slug: ImportingYourLocalDatabaseToPythonAnywhere
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->





##Importing a local database to PythonAnywhere


Thanks to NicholasMurray in the forums for this! He writes: 

Assuming that you have phpMyAdmin as I had. To backup your MySQL database using PHPMyAdmin just follow a couple of steps: 

  * Open phpMyAdmin. 
  * Select your database by clicking the database name in the list on the left of the screen. 
  * Click the Export link. This should bring up a new screen that says View dump of database (or something similar). 
  * In the Export area, click the Select All link to choose all of the tables in your database. 
  * In the SQL options area, click the right options. 
  * Click on the Save as file option and the corresponding compression option and then click the 'Go' button. A dialog box should appear prompting you to save the file locally 
  * Use the .sql extension 
  * Upload the database backup to your files using the Files tab on the dashboard 
  * Open a database console in the Databases tab on the console and type: 

    use yourusername$yourdatabasename;
    source yourbackupname.sql;


  * Then to view your newly imported tables 

    show tables;


  * Then execute sql as normal 

    select * from yourtablename;
