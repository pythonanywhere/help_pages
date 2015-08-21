
<!--
.. title: How to get your code in and out of PythonAnywhere
.. slug: FTP
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



Whether it's uploading your code once and for ever, or downloading your code to move somewhere else, or trying to keep your local dev environment in sync with PythonAnywhere, we're keen to help you get code in and out. Try out the solutions below, and remember we're always here to help! The "Send feedback" button is just a short click away... 


##Can I use FTP / Filezilla?


The short answer is that you cannot use FTP or Filezilla unless you have a paying account. But don't despair! There are other, mostly better ways of getting your code in and out of PythonAnywhere


##Using a code sharing site like GitHub or BitBucket


The best way is to use a source code control system (or VCS) like Git, mercurial or subversion. You can then "push" your code up to [GitHub](https://github.com/) or [Bitbucket](https://bitbucket.org/), and then "pull" it down to PythonAnywhere, or push from PythonAnywhere to Bitbucket or [GitHub](//www.github.com/). You also get all the benefits of using a version control system, the ability to go back to older versions of files, etc. 

Follow the instructions on either Github ("[create a repo](https://help.github.com/articles/create-a-repo)") or Bitbucket ("[Bitbucket 101](https://confluence.atlassian.com/display/BITBUCKET/Bitbucket+101)"), both of which have excellent documentation, for how to get started. 

On PythonAnywhere, use a **Bash Console**, and you'll be able to access `git` (or `hg` or `svn`) and [clone your repository](/pages/ExternalVCS), and push and pull. You can also generate an SSH keypair using `ssh-keygen`. 

If you want to clone all of your [GitHub](//www.github.com/) repositories, you might want to take a look at Bede Kelly's [cloneall](https://asciinema.org/a/10136). 


##Uploading a zip file


The alternative is to compress your project folder on your own PC, and upload it using the **Files tab**. Then, open a **Bash console** to run `unzip` to decompress the zipfile you've uploaded. 

If your file is too large to easily upload, you may have to split it up into chunks and stitch them back together afterwards. Split the files locally into 50mb files: 

  * `split -b 50m huge_file`

Upload them to PythonAnywhere, then get them back together with: 

  * `cat file1 file2 file3 > huge_file_on_pythonanywhere`


##SFTP (paying accounts only)


You can use SFTP, which is a form of FTP-over-SSH. This is restricted to paying users only. Use your normal username and password and connect to ssh.pythonanywhere.com. 

From the command-line, use `sftp <username>@ssh.pythonanywhere.com`. 

Filezilla also supports SFTP; just use `ssh.pythonanywhere.com` as the server (if you're entering it into the box at the top of the main screen, you'll need to specify SFTP there too, like this: `sftp://ssh.pythonanywhere.com`.) 


##Rsync (paying accounts only)


Similarly, to send a file or directories from your local machine to your pythonanywhere console, run the following code from your local machine: 

  * `rsync -avzhe ssh <LOCAL_FILE_PATH> <USER_NAME>@ssh.pythonanywhere.com:<DESTINATION_DIRECTORY>`

To grab a file (or directories) from your pythonanywhere account to your local machine, run the following from your local machine: 

  * `rsync -avzhe ssh <USER_NAME>@ssh.pythonanywhere.com:<PYTHONANYWHERE_FILE_PATH> <LOCAL_DIRECTORY>`

If you have a another server somewhere, you could also rsync between that and PythonAnywhere. PythonAnywhere will only listen to port 443, but to configure your own server to listen on say 2220 or whatever port for an incoming ssh connection: 

  * `rsync -ravzhe 'ssh -p 2220' <DIR_PATH_ON_PYTHONANYWHERE> <USER_NAME>@<YOUR_SERVER>:<DESTINATION_PATH>`
