<!--
.. title: File and Directory Permissions
.. slug: FileAndDirectoryPermissions
.. date: 2025-08-02 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

# Permisssions

It is possible for some OSs and upload mechanisms to create directories in your
PythonAnywhere storage that you cannot use. This is generally because the
permissions on those files or directories are set incorrectly. It is relatively easy to
tell when this has happened and to fix it. In this article, we will cover how
to identify the problem and how to fix it.

The first way that you are likely to notice the issue is when trying to do file
operations on a file or in a specific directory or group of directories and you get a
`Permission denied` error of some sort.

# Introduction to file and directory permissions

Linux uses a permission system to control who can read, write, or execute files
and directories. Every file and directory has three sets of permissions:

- **User (u)**: The owner of the file
- **Group (g)**: Members of the file's group
- **Other (o)**: Everyone else on the system

Each set can have three types of permissions:

- **Read (r)**: View the contents of a file or list the contents of a directory
- **Write (w)**: Modify or delete a file, or add/remove files in a directory
- **Execute (x)**: Run a file as a program, or access files inside a directory

When you run `ls -l`, you'll see permissions displayed as a string like
`-rwxr-xr--`. The first character indicates the type (- for file, d for
directory), followed by three groups of three characters showing user, group,
and other permissions respectively.

For example:
```
-rw-r--r-- 1 username registered_users 1234 Sep 2 15:17 myfile.py
```
This shows a file where the user can read and write (rw-), the group can read
(r--), and others can read (r--).

When permissions are set incorrectly, you'll get `Permission denied` errors
when trying to access files or directories. The following sections show how to
identify and fix these issues.

# File permissions

As an exmaple, I have created a file called `test_file` and purposefully
broken its permissions:

```
$ cat test_file
cat: test_file: Permission denied

```

We can check the permissions on the file like this:

```
$ ls -l test_file
-------r-- 2 username registered_users 4096 Sep  2 15:17 test_file
```

This file has no permissions for `user` and `group`, but does have read for
`root`. There may be other patterns in the first column that show different
permissions.

Whatever the permissions on the file are, you can fix them with the `chmod`
program in a Bash console:

```
chmod u+rw test_file
```

You can also mark a file as executable if you would like to run it directly
from a Bash console or in a Task.

```
chmod u+rwx test_file
```

**Note:** These are simple examples and you can be more specific, but this help
page will not cover the other uses of chmod.

# Directory permissions

As an example, I have created a directory called `test_dir` and purposefully
broken its permissions:

```
$ cat test_dir/some_file
cat: test_dir/some_file: Permission denied

```

We can check the permissions on the directory like this:

```
$ ls -ld test_dir
drw-rw-r-- 2 username registered_users 4096 Sep  2 15:17 test_dir
```

In the above output, we can see that the directory does not have execute
permissions.

If you have a directory that does not have execute permissions, it is easy to
add them like this:

```
$ chmod +x test_dir
```

Now, when we check the permissions on the directory, we can see that it has
execute permissions:

```
$ ls -ld test_dir
drwxrwxr-x 2 glenn registered_users 4096 Sep  2 15:17 test_dir
```

If you have nested directories (like `dir1/dir2/dir3`), you will need to set
the permissions at each level from the top level directory down:

```
$ chmod +x dir1
$ chmod +x dir1/dir2
$ chmod +x dir1/dir2/dir3
```
