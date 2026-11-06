
<!--
.. title: MySQL Certificate Verification
.. slug: MySQLCertificateVerification
.. date: 2026-11-06 00:00:00 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


## Certificate verification for MySQL

If you want to use certificate or CA verification for connections to your MySQL
server, you will need to get a certificate bundle from Amazon and use the
correct hostname for the connection.

## The certificate bundle

AWS publish certificate bundles for their MySQL servers
[here](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.SSL.html#UsingWithRDS.SSL.CertificatesDownload)

You will need the `US East (N. Virginia)` if you are on our US servers and
`Europe (Frankfurt)` if you are on our EU servers.

## The correct hostname

The hostnames that we provide on your Databases page are conveniece CNAMEs and
not the actual hostname of the server. For the certificate or CA verification
to work, you need to use the real address of the MySQL server. You can find it
using `dig`:

```bash
dig your_username.mysql.pythonanywhere-services.com
```

In the ANSWER section of the output, you will see something like this:

```
;; ANSWER SECTION:
your_username.mysql.pythonanywhere-services.com. 60 IN CNAME users-mysql-X.machines.pythonanywhere-services.com.
users-mysql-X.machines.pythonanywhere-services.com. 60 IN CNAME live-users-db-X.something.us-east-1.rds.amazonaws.com.
live-users-db-X.something.us-east-1.rds.amazonaws.com. 5 IN CNAME ec2-5-205-14-3.compute-1.amazonaws.com.
ec2-5-205-14-3.compute-1.amazonaws.com. 21600 IN A 5.205.14.3
```

The address that you will need to use is the one that looks like the 3rd one in
this example: `live-users-db-X.something.us-east-1.rds.amazonaws.com`

***Note:*** If your database is migrated or upgraded to a new version on MySQL,
you will need to look up the new address and use that instead.
