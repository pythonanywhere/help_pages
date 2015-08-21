
<!--
.. title: LoadDataInfile
.. slug: LoadDataInfile
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->




When trying to get data in mysql, you may see an error a little like this: 

  * `Error Code: 1045 Access denied for user 'myusername'@'%' (using password: YES)`

The newer versions of mysql client block load data by default. You need to pass it in as a command line switch. If you open up a Bash console you can connect the the mysql database manually like so: 

  * `mysql -hmysql.server -umyusername myusername\$default -p --local-infile=1`

"myusername\$default" is the name of the database with the "$" escaped for bash. "--local-infile=1" enables the load data command. You will be prompted for your password. 
