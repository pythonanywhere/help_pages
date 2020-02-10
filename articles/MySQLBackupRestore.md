
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

We'll need to arm ourselves with 2 pieces of information, both of which you can find on the **Databases tab** from your PythonAnywhere dashboard.

- the **hostname** of your mysql server.  You can find this on the "Databases" tab, it's usually something like `yourusername.mysql.pythonanywhere-services.com`

- the **full name of the database** you want to back up.  These usually follow the naming convention `yourusername$dbname`  -- so the full name includes your username, and the character "$"

Armed with these two, you should open up a **Bash console**, and then run the following command:

```bash
cd
mysqldump -u yourusername -h yourusername.mysql.pythonanywhere-services.com 'yourusername$dbname'  > db-backup.sql
```

> The 'single-quotes' around the database name are required, because of the '$' character in the full database name.

> You'll notice that we're not entering a password for the database.  That's because your password is automatically saved by the pythonanywhere system to a file at `~/.my.cnf`.


The ***db-backup.sql*** file will then be available in your home folder (via the
*Files* tab), where you can download it to a safe place.


## Restoring from a backup file

If you later need to restore, run the following command:

```bash
mysql -u yourusername -h yourusername.mysql.pythonanywhere-services.com 'yourusername$dbname'  < db-backup.sql
```

Be aware that this will completely delete any existing data in the database though! 


## Scheduling the backup as a task

To automate the backup process, you  can run it daily or hourly via the **Schedule** tab.

Simply copy and paste the `mysqldump` command-line from above, and paste it into a new scheduled task entry.

You could also add a task that then uploads the dump file to an off-site server
using `rsync` or `scp`, but that's up to you!


