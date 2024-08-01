
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


# Getting started and Authentication

The PythonAnywhere API uses token-based authentication.  You can get your token
from [your Account page on the API Token tab](https://www.pythonanywhere.com/account/#api_token).

It's used in a header called `Authorization`, and the value is encoded as the
string "Token", followed by a space, followed by your token, like this:

```python
'Authorization': 'Token {}'.format(token)
```

For example, this code using the `requests` module would get the details of your
CPU usage on PythonAnywhere; you would just need to change the three variables
at the top to match your actual username, your API token, and the correct host:

* `www.pythonanywhere.com` if your account is on our US-based system.
* `eu.pythonanywhere.com` if your account is on our EU-based system.

```python
import requests
username = 'your username'
token = 'your token'
host = 'your host'

response = requests.get(
    'https://{host}/api/v0/user/{username}/cpu/'.format(
        host=host, username=username
    ),
    headers={'Authorization': 'Token {token}'.format(token=token)}
)
if response.status_code == 200:
    print('CPU quota info:')
    print(response.content)
else:
    print('Got unexpected status code {}: {!r}'.format(response.status_code, response.content))
```

Once you've generated your token, you can copy and paste it for use in your scripts.  You can also access
it at any time from PythonAnywhere consoles, webapps and tasks in a pre-populated environment variable,
`$API_TOKEN`.

You will need to reload your webapp and start new consoles for this environment variable to be in place.


# Endpoints

All endpoints are hosted at *https://www.pythonanywhere.com/* or
*https://eu.pythonanywhere.com/* depending on where your account is registered.


# Rate-limits

Each endpoint has a 40 requests per minute rate limit, apart from the `send_input`
endpoint on consoles, which is 120 requests per minute.


## Always_On

### /api/v0/user/{username}/always_on/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">List all of your always-on tasks</td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">POST</td><td class="description">Create and start a new always-on task</td><td class="params">command, description, enabled</td></tr>
</table>


### /api/v0/user/{username}/always_on/{id}/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Return information about an always-on task.</td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">PUT</td><td class="description">Endpoints for always-on tasks</td><td class="params">command, description, enabled</td></tr>
  <tr><td class="method">PATCH</td><td class="description">Endpoints for always-on tasks</td><td class="params">command, description, enabled</td></tr>
  <tr><td class="method">DELETE</td><td class="description">Stop and delete an always-on task</td><td class="params">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/always_on/{id}/restart/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">POST</td><td class="description">Endpoints for always-on tasks</td><td class="params">command, description, enabled</td></tr>
</table>

## Consoles

### /api/v0/user/{username}/consoles/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">List all your consoles</td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">POST</td><td class="description">Create a new console object (NB does not actually start the process. Only
connecting to the console in a browser will do that).</td><td class="params">executable, arguments, working_directory</td></tr>
</table>


### /api/v0/user/{username}/consoles/shared_with_you/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">View consoles shared with you.</td><td class="params">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/consoles/{id}/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Return information about a console instance.</td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">DELETE</td><td class="description">Kill a console.</td><td class="params">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/consoles/{id}/get_latest_output/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Get the most recent output from the console (approximately 500 characters).</td><td class="params">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/consoles/{id}/send_input/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">POST</td><td class="description">"type" into the console.  Add a "\n" for return.</td><td class="params">POST parameter: input</td></tr>
</table>

## Cpu

### /api/v0/user/{username}/cpu/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Returns information about cpu usage in json format:
<pre>{
    "daily_cpu_limit_seconds": &lt;int&gt;,
    "next_reset_time": &lt;isoformat&gt;,
    "daily_cpu_total_usage_seconds": &lt;float&gt;
}</pre></td><td class="params">(no parameters)</td></tr>
</table>

## Databases

### /api/v0/user/{username}/databases/mysql/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description"></td><td class="params">(no parameters)</td></tr>
</table>

## Default_Python3_Version

### /api/v0/user/{username}/default_python3_version/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Returns information about user's current and available default Python 3 version
in json format:
<pre>{
    "default_python3_version": &lt;str&gt;,
    "available_python3_versions": [&lt;str&gt;],
}</pre></td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">PATCH</td><td class="description">Sets default Python 3 version for user.</td><td class="params">(no parameters)</td></tr>
</table>

## Default_Python_Version

### /api/v0/user/{username}/default_python_version/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Returns information about user's current and available default Python version
in json format:
<pre>{
    "default_python_version": &lt;str&gt;,
    "available_python_versions": [&lt;str&gt;],
}</pre></td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">PATCH</td><td class="description">Sets default Python version for user.</td><td class="params">(no parameters)</td></tr>
</table>

## Default_Save_And_Run_Python_Version

### /api/v0/user/{username}/default_save_and_run_python_version/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Returns information about user's current and available Python version used for
the "Run" button in the editor, in json format:
<pre>{
    "default_save_and_run_python_version": &lt;str&gt;,
    "available_python_versions": [&lt;str&gt;],
}</pre></td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">PATCH</td><td class="description">Sets Python version used for the "Run" button in the editor.</td><td class="params">(no parameters)</td></tr>
</table>

## Files

### /api/v0/user/{username}/files/path{path}

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description"></td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">POST</td><td class="description">Uploads a file to the specified file path.  Contents should be in a
multipart-encoded file with the name "content".  The attached filename is
ignored.
If the directories in the given path do not exist, they will be created.
Any file already present at the specified path will be overwritten.
Returns 201 on success if a file has been created, or 200 if an existing
file has been updated.</td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">DELETE</td><td class="description">Deletes the file at the specified path. This method can be used to
delete log files that are not longer required.
Returns 204 on success.</td><td class="params">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/files/sharing/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">POST</td><td class="description">Start sharing a file.  Returns 201 on success, or 200 if file was already shared.</td><td class="params">POST parameter: path</td></tr>
</table>


### /api/v0/user/{username}/files/sharing/?path={path}

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Check sharing status for a path.  Returns 404 if path not currently shared.</td><td class="params">Query parameter: path</td></tr>
  <tr><td class="method">DELETE</td><td class="description">Stop sharing a path.  Returns 204 on successful unshare.</td><td class="params">Query parameter: path</td></tr>
</table>


### /api/v0/user/{username}/files/tree/?path={path}

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Returns a list of the contents of a directory, and its subdirectories
as a list. Paths ending in slash/ represent directories.  Limited to
1000 results.</td><td class="params">Query parameter: path</td></tr>
</table>

## Schedule

### /api/v0/user/{username}/schedule/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">List all of your scheduled tasks</td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">POST</td><td class="description">Create a new scheduled task</td><td class="params">command, enabled, interval, hour, minute, description</td></tr>
</table>


### /api/v0/user/{username}/schedule/{id}/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Return information about a scheduled task.</td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">PUT</td><td class="description">Endpoints for scheduled tasks</td><td class="params">command, enabled, interval, hour, minute, description</td></tr>
  <tr><td class="method">PATCH</td><td class="description">Endpoints for scheduled tasks</td><td class="params">command, enabled, interval, hour, minute, description</td></tr>
  <tr><td class="method">DELETE</td><td class="description">Delete an scheduled task</td><td class="params">(no parameters)</td></tr>
</table>

## Students

### /api/v0/user/{username}/students/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Returns a list of students of the current user
<pre>{
    "students": [
        {"username": &lt;string&gt;},
        {"username": &lt;string&gt;},
        ...
    ]
}</pre></td><td class="params">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/students/{student}/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">DELETE</td><td class="description"></td><td class="params">(no parameters)</td></tr>
</table>

## System_Image

### /api/v0/user/{username}/system_image/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Returns information about user's current and available system images
in json format:
<pre>{
    "system_image": &lt;str&gt;,
    "available_system_images": [&lt;str&gt;],
}</pre></td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">PATCH</td><td class="description">Sets system image for user.</td><td class="params">(no parameters)</td></tr>
</table>

## Webapps

### /api/v0/user/{username}/webapps/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">List all webapps</td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">POST</td><td class="description">Create a new webapp with manual configuration.   Use (for example) "python36" to
specify Python 3.6.</td><td class="params">POST parameters: domain_name, python_version</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Return information about a web app's configuration</td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">PUT</td><td class="description">Modify configuration of a web app. (NB a reload is usually required to apply changes).</td><td class="params">python_version, source_directory, virtualenv_path, force_https, password_protection_enabled, password_protection_username, password_protection_password</td></tr>
  <tr><td class="method">PATCH</td><td class="description">Modify configuration of a web app. (NB a reload is usually required to apply changes).</td><td class="params">python_version, source_directory, virtualenv_path, force_https, password_protection_enabled, password_protection_username, password_protection_password</td></tr>
  <tr><td class="method">DELETE</td><td class="description">Delete the webapp.  This will take the site offline.
Config is backed up in /var/www, and your code is not touched.</td><td class="params">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/disable/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">POST</td><td class="description">Disable the webapp.</td><td class="params">POST parameters: none</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/enable/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">POST</td><td class="description">Enable the webapp.</td><td class="params">POST parameters: none</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/reload/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">POST</td><td class="description">Reload the webapp to reflect changes to configuration and/or source code on disk.</td><td class="params">POST parameters: none</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/ssl/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Get and set TLS/HTTPS info.  POST parameters to the right are incorrect, use
`cert` and `private_key` when posting.</td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">POST</td><td class="description">Get and set TLS/HTTPS info.  POST parameters to the right are incorrect, use
`cert` and `private_key` when posting.</td><td class="params">python_version, source_directory, virtualenv_path, force_https, password_protection_enabled, password_protection_username, password_protection_password</td></tr>
  <tr><td class="method">DELETE</td><td class="description">Get and set TLS/HTTPS info.  POST parameters to the right are incorrect, use
`cert` and `private_key` when posting.</td><td class="params">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/static_files/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">List all the static files mappings for a domain.</td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">POST</td><td class="description">Create a new static files mapping. (webapp restart required)</td><td class="params">url, path</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/static_files/{id}/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Get URL and path of a particular mapping.</td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">PUT</td><td class="description">Modify a static files mapping. (webapp restart required)</td><td class="params">url, path</td></tr>
  <tr><td class="method">PATCH</td><td class="description">Modify a static files mapping. (webapp restart required)</td><td class="params">url, path</td></tr>
  <tr><td class="method">DELETE</td><td class="description">Remove a static files mapping. (webapp restart required)</td><td class="params">(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/static_headers/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">List all the static headers for a domain.</td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">POST</td><td class="description">Create a new static header. (webapp restart required)</td><td class="params">url, name, value</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/static_headers/{id}/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Get URL, name and value of a particular header.</td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">PUT</td><td class="description">Modify a static header. (webapp restart required)</td><td class="params">url, name, value</td></tr>
  <tr><td class="method">PATCH</td><td class="description">Modify a static header. (webapp restart required)</td><td class="params">url, name, value</td></tr>
  <tr><td class="method">DELETE</td><td class="description">Remove a static header. (webapp restart required)</td><td class="params">(no parameters)</td></tr>
</table>

## Websites

### /api/v1/user/{username}/websites/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">List all domains with their webapp details in json format:
<pre>[
    {
        'id': &lt;int&gt;,
        'user': &lt;str&gt;,
        'domain_name': &lt;str&gt;,
        'enabled': &lt;bool&gt;,
        'webapp': {
            'id': &lt;str&gt;,
            'command': &lt;str&gt;,
            'domains': [{'domain_name': &lt;str&gt;, 'enabled': &lt;bool&gt;}]
        },
        'logfiles': {
            'access': &lt;str&gt;,
            'server': &lt;str&gt;,
            'error': &lt;str&gt;,
        }
    }
]</pre></td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">POST</td><td class="description">Create a new domain and associated webapp

Returns information about created website (domain with webapp)
in json format:
<pre>{
    'id': &lt;int&gt;,
    'user': &lt;str&gt;,
    'domain_name': &lt;str&gt;,
    'enabled': &lt;bool&gt;,
    'webapp': {
        'id': &lt;str&gt;,
        'command': &lt;str&gt;,
        'domains': [{'domain_name': &lt;str&gt;, 'enabled': &lt;bool&gt;}]
    },
    'logfiles': {
        'access': &lt;str&gt;,
        'server': &lt;str&gt;,
        'error': &lt;str&gt;,
    }
}</pre>
<code>logfiles</code> paths are ready to be used in the <code>files</code> API</td><td class="params">domain_name, enabled, webapp</td></tr>
</table>


### /api/v1/user/{username}/websites/{domain_name}/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">GET</td><td class="description">Get information about the domain and its webapp
in json format:
<pre>{
    'id': &lt;int&gt;,
    'user': &lt;str&gt;,
    'domain_name': &lt;str&gt;,
    'enabled': &lt;bool&gt;,
    'webapp': {
        'id': &lt;str&gt;,
        'command': &lt;str&gt;,
        'domains': [{'domain_name': &lt;str&gt;, 'enabled': &lt;bool&gt;}]
    },
    'logfiles': {
        'access': &lt;str&gt;,
        'server': &lt;str&gt;,
        'error': &lt;str&gt;,
    }
}</pre>
<code>logfiles</code> paths are ready to be used in the <code>files</code> API</td><td class="params">(no parameters)</td></tr>
  <tr><td class="method">PATCH</td><td class="description">Modify the domain/webapp</td><td class="params">domain_name, enabled, webapp</td></tr>
  <tr><td class="method">DELETE</td><td class="description">Remove the domain and webapp</td><td class="params">(no parameters)</td></tr>
</table>


### /api/v1/user/{username}/websites/{domain_name}/reload/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td class="method">POST</td><td class="description">Reload the webapp to reflect changes to configuration and/or source code on disk.</td><td class="params">POST parameters: none</td></tr>
</table>

