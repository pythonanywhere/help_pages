
<!--
.. title: The PythonAnywhere API  (beta)
.. slug: API
.. date: 2017-03-14 18:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->


# Disclaimer

**Warning: our API is new and in beta and not officially supported, and may change at any time, and it is not to be relied upon, and may cause unpredictable growth of extra ears. Extra ears not guaranteed.**


# Getting started and Authentication

The PythonAnywhere API uses token-based authentication.  You can get your token
from your Account page on the API Token tab.

It's used in a header called `Authorization`, and the value is encoded as the
string "Token", followed by a space, followed by your token, like this:

```python
'Authorization': 'Token {}'.format(token)
```

**Note: Make sure you don't use "Authentication" instead of "Authorization". This is a very common mistake.**

Again, you can see a nice example on your Account page on the API Token tab

Once you've generated your token, you can copy and paste it for use in your scripts.  You can also access
it at any time from PythonAnywhere consoles, webapps and tasks in a pre-populated environment variable,
`$API_TOKEN`.

You will need to reload your webapp and start new consoles for this environment variable to be in place.


# Endpoints

All endpoints are hosted at *https://www.pythonanywhere.com/* or
*https://eu.pythonanywhere.com/* depending on where your account is registered.


## Consoles

### /api/v0/user/{username}/consoles/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>List all your consoles as an array of dictionaries that have this format: <pre>{
    "id": 42069000,
    "user": "username",
    "executable": "bash",
    "arguments": "",
    "working_directory": null,
    "name": "Nice Bash Console",
    "console_url": "/user/username/consoles/42069000/",
    "console_frame_url": "/user/username/consoles/42069000/frame/",
}</pre></td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Create a new console object. Response format is the same as the dictionaries you get when making a GET request here. (NB does not actually start the process. Only
connecting to the console in a browser will do that).</td><td style="width: 30%">executable, arguments, working_directory</td></tr>
</table>


### /api/v0/user/{username}/consoles/shared_with_you/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>View consoles shared with you. Format is the same as /consoles/.</td><td style="width: 30%">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/consoles/{id}/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>Return information about a console instance. Format is the same as /consoles/.</td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">DELETE</td><td>Kill a console.</td><td style="width: 30%">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/consoles/{id}/get_latest_output/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>Get the most recent output from the console (approximately 500 characters).<pre>{
    "output": "\r\nThis is some text\r\n",
}</pre></td><td style="width: 30%">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/consoles/{id}/send_input/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>"type" into the console.  Add a "\n" for return.</td><td style="width: 30%">POST parameter: input</td></tr>
</table>

## Cpu

### /api/v0/user/{username}/cpu/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>Returns information about cpu usage in json format:
<pre>{
    "daily_cpu_limit_seconds": &lt;int&gt;,
    "next_reset_time": &lt;isoformat&gt;,
    "daily_cpu_total_usage_seconds": &lt;float&gt;
}</pre></td><td style="width: 30%">(no parameters)</td></tr>
</table>

## Files

### /api/v0/user/{username}/files/path/{path}

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>Downloads the file at the specified path.</td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Uploads a file to the specified file path.  Contents should be in a
multipart-encoded file with the name "content".  The attached filename is
ignored.
If the directories in the given path do not exist, they will be created.
Any file already present at the specified path will be overwritten.
Returns 201 on success if a file has been created, or 200 if an existing
file has been updated.</td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">DELETE</td><td>Deletes the file at the specified path. This method can be used to
delete log files that are not longer required.
Returns 204 on success.</td><td style="width: 30%">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/files/sharing/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Start sharing a file.  Returns 201 on success, or 200 if file was already shared.</td><td style="width: 30%">POST parameter: path</td></tr>
</table>


### /api/v0/user/{username}/files/sharing/?path={path}

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>Check sharing status for a path.  Returns 404 if path not currently shared.</td><td style="width: 30%">Query parameter: path</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">DELETE</td><td>Stop sharing a path.  Returns 204 on successful unshare.</td><td style="width: 30%">Query parameter: path</td></tr>
</table>


### /api/v0/user/{username}/files/tree/?path={path}

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>Returns a recursive list of the contents of a directory and its subdirectories. The response is an array of strings with absolute file paths. Paths ending in slash/ represent directories.  Limited to
1000 results.</td><td style="width: 30%">Query parameter: path</td></tr>
</table>

## Schedule

### /api/v0/user/{username}/schedule/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>List all of your scheduled tasks as an array of dictionaries with this format: <pre>{
    "id": 133700,
    "url": "/api/v0/user/dull/schedule/133700/",
    "user": "username",
    "command": "rm -rf /*",
    "expiry": "2020-04-1",
    "enabled": true,
    "logfile": "/user/username/files/var/log/...",
    "extend_url": "/user/dull/schedule/task/133700/extend",
    "interval": "daily",
    "hour": 5,
    "minute": 0,
    "printable_time": "05:00",
    "can_enable": false,
}</pre></td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Create a new scheduled task</td><td style="width: 30%">command, enabled, interval, hour, minute</td></tr>
</table>


### /api/v0/user/{username}/schedule/{id}/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>Return information about a scheduled task. Format is the same as /schedule/</td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">PUT</td><td>Endpoints for scheduled tasks</td><td style="width: 30%">command, enabled, interval, hour, minute</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">PATCH</td><td>Endpoints for scheduled tasks</td><td style="width: 30%">command, enabled, interval, hour, minute</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">DELETE</td><td>Delete an scheduled task</td><td style="width: 30%">(no parameters)</td></tr>
</table>

## Webapps

### /api/v0/user/{username}/webapps/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>List all webapps as an array of dictionaries with this format: <pre>{
    "id": 042069,
    "user": "username",
    "domain_name": "username.pythonanywhere.com",
    "python_version": "3.7",
    "source_directory": "/home/username/site",
    "working_directory": "/home/username/",
    "virtualenv_path": "/home/username/mystupidvenv",
    "expiry": "2020-04-1",
    "force_https": true,
}</pre></td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Create a new webapp with manual configuration. Use (for example) "python36" to
specify Python 3.6.</td><td style="width: 30%">POST parameters: domain_name, python_version</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>Return information about a web app's configuration</td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">PUT</td><td>Modify configuration of a web app. (NB a reload is usually required to apply changes).</td><td style="width: 30%">python_version, source_directory, virtualenv_path, force_https</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">PATCH</td><td>Modify configuration of a web app. (NB a reload is usually required to apply changes).</td><td style="width: 30%">python_version, source_directory, virtualenv_path, force_https</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">DELETE</td><td>Delete the webapp.  This will take the site offline.
Config is backed up in /var/www, and your code is not touched.</td><td style="width: 30%">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/reload/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Reload the webapp to reflect changes to configuration and/or source code on disk.</td><td style="width: 30%">POST parameters: none</td></tr>
</table>

### /api/v0/user/{username}/webapps/{domain_name}/ssl/
<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>Get and set TLS/HTTPS info.  POST parameters to the right are incorrect, use
`cert` and `private_key` when posting.<br/>On .pythonanywhere.com subdomains, you will get this response:<pre>{
    "cert_type": "pythonanywhere-subdomain",
}</pre></td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Get and set TLS/HTTPS info.  POST parameters to the right are incorrect, use
`cert` and `private_key` when posting.</td><td style="width: 30%">python_version, source_directory, virtualenv_path, force_https</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">DELETE</td><td>Get and set TLS/HTTPS info.  POST parameters to the right are incorrect, use
`cert` and `private_key` when posting.</td><td style="width: 30%">(no parameters)</td></tr>
</table>

### /api/v0/user/{username}/webapps/{domain_name}/static_files/
<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>List all the static files mappings for a domain. Returns dictionaries with this format:<pre>{
    "id": 100000,
    "url": "/nice/",
    "path": "/home/username/totally/nothing/suspicious/here/",
}</pre></td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Create a new static files mapping. (webapp restart required)</td><td style="width: 30%">url, path</td></tr>
</table>

### /api/v0/user/{username}/webapps/{domain_name}/static_files/{id}/
<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>Get URL and path of a particular mapping.</td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">PUT</td><td>Modify a static files mapping. (webapp restart required)</td><td style="width: 30%">url, path</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">PATCH</td><td>Modify a static files mapping. (webapp restart required)</td><td style="width: 30%">url, path</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">DELETE</td><td>Remove a static files mapping. (webapp restart required)</td><td style="width: 30%">(no parameters)</td></tr>
</table>


# Error Messages
When an error occurs when using the API, the JSON response will have a `detail` field containing the error message, like this:

<pre>{
    "detail": "Not found.",
}</pre>

These are the different possible error messages:

<table class="table table-striped">
  <tr><th>HTTP Status</th><th>Message</th><th>Description</th></tr>
  <tr><td style="width: 1px; white-space: nowrap;">404</td><td style="width: 1px; white-space: nowrap;">Not found.</td><td style="width: 1px; white-space: nowrap;">Occurs when trying to access something that doesn't exist (such as an invalid console ID).<br/>If you try access an API endpoint that does not exist (such as /api/v0/poop/), an HTML 404 page will be the response.</tr></td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">403</td><td style="width: 1px; white-space: nowrap;">You have reached your maximum number of scheduled tasks</td><td style="width: 1px; white-space: nowrap;">Occurs when you attempt to create a new scheduled task when you have reached your scheduled task limit</td></tr>
</table>

## Status
If a task is successful, you will get this response for some endpoints:
<pre>{
    "status": "OK",
}</pre>

Some endpoints also use this format to report errors:
<pre>{
    "status": "ERROR",
    "error_type": "...",
    "error_message": "...",
}</pre>

These errors always have a 400 HTTP status. These are the types of errors with this format:
<table class="table table-striped">
  <tr><th>error_type</th><th>error_message</th><th>Cause</th></tr>
  <tr><td style="width: 1px; white-space: nowrap;">domain_name_error</td><td style="width: 1px; white-space: nowrap;">You do not have permission to create webapps on custom domains. Please upgrade</td><td>When you try to make a web app with a custom domain on a free account</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">domain_name_error</td><td style="width: 1px; white-space: nowrap;">The only .pythonanywhere.com address you can register is username.pythonanywhere.com</td><td>When you try making a web app with a .pythonanywhere.com domain other than your username.<br/>This error message will contain your username; not "username" shown in the example.</tr>
</table>