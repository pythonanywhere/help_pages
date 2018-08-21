
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
from the [Accounts page](https://www.pythonanywhere.com/account/#api_token)

It's used in a header called `Authorization`, and the value is encoded as the
string "Token", followed by a space, followed by your token, like this:

```python
'Authorization': 'Token {}'.format(token)
```

Again, you can see a nice example on the [Accounts page](https://www.pythonanywhere.com/account/#api_token)


Once you've generated your token, you can copy and paste it for use in your scripts.  You can also access
it at any time from PythonAnywhere consoles, webapps and tasks in a pre-populated environment variable,
`$API_TOKEN`.


# Endpoints


All endpoints are hosted at *https://www.pythonanywhere.com/*


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

## Files

### /api/v0/user/{username}/files/path{path}/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">DELETE</td><td></td><td style="width: 30%">(no parameters)</td></tr>
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
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Create a new webapp with manual configuration.</td><td style="width: 30%">POST parameters: domain_name, python_version</td></tr>
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

<table class="table table-striped">
### /api/v0/user/{username}/webapps/{domain_name}/reload/
<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Reload the webapp to reflect changes to configuration and/or source code o
n disk.</td><td style="width: 30%">POST parameters: none</td></tr>
</table>
### /api/v0/user/{username}/webapps/{domain_name}/static_files/
<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>List all the static files mappings for a domain.</td><td style="width: 30%"
>(no parameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">POST</td><td>Create a new static files mapping. (webapp restart required)</td><td style
="width: 30%">url, path</td></tr>
</table>
### /api/v0/user/{username}/webapps/{domain_name}/static_files/{id}/
<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td style="width: 1px; white-space: nowrap;">GET</td><td>Get URL and path of a particular mapping.</td><td style="width: 30%">(no pa
rameters)</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">PUT</td><td>Modify a static files mapping. (webapp restart required)</td><td style="wid
th: 30%">url, path</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">PATCH</td><td>Modify a static files mapping. (webapp restart required)</td><td style="w
idth: 30%">url, path</td></tr>
  <tr><td style="width: 1px; white-space: nowrap;">DELETE</td><td>Remove a static files mapping. (webapp restart required)</td><td style="
width: 30%">(no parameters)</td></tr>
</table>