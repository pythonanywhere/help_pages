
<!--
.. title: Database character sets
.. slug: DatabaseCharacterSets
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->





###Setting up character sets in MySQL on PythonAnywhere


By default, PythonAnywhere creates your databases with the MySQL default character set/collation settings -- these are: 

  * Character set: latin1 
  * Collation: latin1_swedish_ci 

If you want to store non-latin characters in your database (eg. Cyrillic) then you'll need to change its character set and collation settings, firstly on your database and then secondly on each table. To do this, start a MySQL console, then run the following command (replacing `databasename` with your database's name, of course): 

    ALTER DATABASE databasename CHARACTER SET utf8 COLLATE utf8_general_ci;


Then, for each table run this: 

    ALTER TABLE tablename CHARACTER SET utf8 COLLATE utf8_general_ci;
