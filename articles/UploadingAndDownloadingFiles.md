<!--
.. title: How to get your code in and out of PythonAnywhere
.. slug: UploadingAndDownloadingFiles
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

Whether it's uploading your code once and for ever, or downloading your code to
move somewhere else, or trying to keep your local dev environment in sync with
PythonAnywhere, we're keen to help you get code in and out. Try out the
solutions below, and remember we're always here to help! The "Send feedback"
button is just a short click away...


## The file upload button

If you just want to upload one file, and it's smaller than 100MiB in size, you
can just upload it on the "Files" page -- look for the orange button.   Similarly,
your can download files using the button next to the filename.

This is useful for quick updates, but less good if you want to transfer multiple files
-- for example, all of the code for a website.


## Using a code sharing site like GitHub or BitBucket

The very best way to manage your code files is to use a source code control system (or VCS) like Git,
Mercurial or Subversion. You can then "push" your code up to
[GitHub](https://github.com/) or [Bitbucket](https://bitbucket.org/), and then
"pull" it down to PythonAnywhere, or push from PythonAnywhere to Bitbucket or
GitHub. You also get all the benefits of using a version
control system, the ability to go back to older versions of files, etc.

Follow the instructions on either GitHub ("[create a
repo](https://help.github.com/articles/create-a-repo)") or Bitbucket
("[set up a repository](https://confluence.atlassian.com/get-started-with-bitbucket/set-up-a-repository-861178557.html)"), both
of which have excellent documentation, for how to get started.

On PythonAnywhere, use a **Bash Console**, and you'll be able to access `git`
(or `hg` or `svn`) and [clone your repository](/pages/ExternalVCS), and push
and pull. You can also generate an SSH keypair using `ssh-keygen`.

If you want to clone all of your [GitHub](//www.github.com/) repositories, you
might want to take a look at Bede Kelly's
[cloneall](https://asciinema.org/a/10136).


## Uploading a zip file

An alternative that you can use in a free account is to compress your project folder on your own PC, and upload
it using the **Files** page. Then, open a **Bash console** to run `unzip` to
decompress the zipfile you've uploaded.

If your file is too large to upload -- that is, more than 100MiB -- you will have to split it up into
chunks and stitch them back together afterwards. Split the files locally into
50mb files, for example by using this command in Bash (if you're using Linux
or the "Git Bash" tools on Windows), or in a Terminal on a Mac:

    split -b 50m huge_file

...or by using a tool like [GSplit](https://www.gdgsoft.com/gsplit) on a Windows
machine.

Upload them to PythonAnywhere, then get them back together with:

    cat file1 file2 file3 > huge_file_on_pythonanywhere

The process for downloading multiple files is just the same, but in reverse.


## SFTP (paying accounts only)

If you have a paid account, you can use SFTP, which is a form of FTP-over-SSH.

The SSH server for your account depends on which one of our sites you signed up
to:

* If you're using our global, US-hosted site at `www.pythonanywhere.com`, then the
  SSH server's hostname is `ssh.pythonanywhere.com`
* If you're using our EU-hosted site at `eu.pythonanywhere.com`, then the
  SSH server's hostname is `ssh.eu.pythonanywhere.com`

Use your normal username and password and connect; note that the username
is **case-sensitive** (also, see [this help page](/pages/SSHAccess) to get more information about SSH on PythonAnywhere).

To use SFTP, from the command-line, use `sftp <username>@<ssh server hostname>`.

For a graphical user interface, [Filezilla](https://filezilla-project.org/) also supports SFTP; just use `ssh.pythonanywhere.com` or `ssh.eu.pythonanywhere.com` as the server
(if you're entering it into the box at the top of the main screen, you'll need
to specify SFTP there too, like this: `sftp://<ssh server hostname>`.)

[WinSCP](https://winscp.net/eng/index.php) is also a good option if you want to
use SFTP from a Windows machine.

**NOTE:** If your `.bashrc` outputs *anything* to the console when you connect,
the SFTP connection will not work. SFTP from the command line will give you an
error like this: `Received message too long 1651664225` and Filezilla will give
an error like `Connection timed out after 20 seconds of inactivity`.


## Rsync (paying accounts only)

Paid accounts can also use the `rsync` command; run the following command on your local machine:

    rsync -avzhe ssh <LOCAL_FILE_PATH> <USER_NAME>@<SSH SERVER HOSTNAME>:<DESTINATION_DIRECTORY>

...where `SSH_SERVER_HOSTNAME` is as described in the "SFTP" section above.

To grab a file (or directories) from your pythonanywhere account to your local
machine, run the following from your local machine:

    rsync -avzhe ssh <USER_NAME>@<SSH SERVER HOSTNAME>:<PYTHONANYWHERE_FILE_PATH> <LOCAL_DIRECTORY>

If you have a another server somewhere, you could also rsync between that and
PythonAnywhere. PythonAnywhere will only listen to port 22, but to configure
your own server to listen on say 2220 or whatever port for an incoming ssh
connection:

    rsync -ravzhe 'ssh -p 2220' <DIR_PATH_ON_PYTHONANYWHERE> <USER_NAME>@<YOUR_SERVER>:<DESTINATION_PATH>
