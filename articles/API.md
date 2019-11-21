
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
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>List all your consoles</td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Create a new console object (NB does not actually start the process. Only
connecting to the console in a browser will do that).</td><td style="width: 30%">executable, arguments, working_directory</td></tr>
</table>


### /api/v0/user/{username}/consoles/shared_with_you/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>View consoles shared with you.</td><td style="width: 30%">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/consoles/{id}/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>Return information about a console instance.</td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">DELETE</td><td>Kill a console.</td><td style="width: 30%">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/consoles/{id}/get_latest_output/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>Get the most recent output from the console (approximately 500 characters).</td><td style="width: 30%">(no parameters)</td></tr>
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

### /api/v0/user/{username}/files/path{path}

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
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>Returns a list of the contents of a directory, and its subdirectories
as a list. Paths ending in slash/ represent directories.  Limited to
1000 results.</td><td style="width: 30%">Query parameter: path</td></tr>
</table>

## Schedule

### /api/v0/user/{username}/schedule/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>List all of your scheduled tasks</td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Create a new scheduled task</td><td style="width: 30%">command, enabled, interval, hour, minute</td></tr>
</table>


### /api/v0/user/{username}/schedule/{id}/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>Return information about a scheduled task.</td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">PUT</td><td>Endpoints for scheduled tasks</td><td style="width: 30%">command, enabled, interval, hour, minute</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">PATCH</td><td>Endpoints for scheduled tasks</td><td style="width: 30%">command, enabled, interval, hour, minute</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">DELETE</td><td>Delete an scheduled task</td><td style="width: 30%">(no parameters)</td></tr>
</table>

## Webapps

### /api/v0/user/{username}/webapps/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>List all webapps</td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Create a new webapp with manual configuration.   Use (for example) "python36" to
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


### /api/v0/user/{username}/webapps/{domain_name}/disable/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Disable the webapp.</td><td style="width: 30%">POST parameters: none</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/enable/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Enable the webapp.</td><td style="width: 30%">POST parameters: none</td></tr>
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
`cert` and `private_key` when posting.</td><td style="width: 30%">(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Get and set TLS/HTTPS info.  POST parameters to the right are incorrect, use
`cert` and `private_key` when posting.</td><td style="width: 30%">python_version, source_directory, virtualenv_path, force_https</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">DELETE</td><td>Get and set TLS/HTTPS info.  POST parameters to the right are incorrect, use
`cert` and `private_key` when posting.</td><td style="width: 30%">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/static_files/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>List all the static files mappings for a domain.</td><td style="width: 30%">(no parameters)</td></tr>
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

