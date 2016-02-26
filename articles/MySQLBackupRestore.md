
<!--
.. title: Backing up (and restoring) MySQL databases
.. slug: MySQLBackupRestore
.. date: 2016-02-26 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

To back up your MySQL database, you can use the `mysqldump` command-line tool.

## Backing up a database using mysqldump

We'll need to arm ourselves with 3 pieces of information, all three of which you can find on the **Databases tab** from your PythonAnywhere dashboard.

- the **hostname** of your mysql server.  You can find this on the "Databases" tab, it's usually something like `yourusername.mysql.pythonanywhere-services.com`

- the **full name of the database** you want to back up.  These usually follow the naming convention `yourusername$databasename`  -- so the full name includes your username, and the character "$"

- the **password** for your database.  This is set via the databases tab.  If you've set it already, you've probably noted it down somewhere in your web app settings files, an you can also retrieve it from a file called *.my.cnf* in your home folder.

Armed with these three, you should open up a **Bash console**, and then run the following command:

```bash
cd
mysqldump -u yourusername -h yourusername.mysql.pythonanywhere-services.com -p 'yourusername$databasename'  > db-backup.sql
```

You will then be prompted to enter your password.

**TIP**: the 'single-quotes' around the database name are required, because of the '$' character in the full database name.


The *db-backup.sql* file will then be available in your home folder (via the
*Files* tab), where you can download it to a safe place.


## Restoring from a backup file

If you later need to restore, run the following command:

```bash
mysql -u yourusername -h yourusername.mysql.pythonanywhere-services.com -p 'yourusername$databasename'  < db-backup.sql
```

Be aware that this will completely delete any existing data in the database though! 

