
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



# Authentication

The PythonAnywhere API uses token-based authentication.  You can get your token
from the [Accounts page](https://www.pythonanywhere.com/account/#api_token)

It's used in a header like this:

```python
'Authorization': f'Token {token}'
```

Again, you can see a nice example on your [Accounts page](https://www.pythonanywhere.com/account/#api_token)


# Endpoints


All endpoints are hosted at *http://www.pythonanywhere.com/*

### /api/v0/user/{username}/consoles/
<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td>GET</td><td>List all your consoles</td><td>(no parameters)</td></tr>
</table>
### /api/v0/user/{username}/consoles/shared_with_you/
<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td>GET</td><td>View consoles shared with you</td><td>(no parameters)</td></tr>
</table>
### /api/v0/user/{username}/consoles/{id}/
<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td>GET</td><td>Return information about a console instance.</td><td>(no parameters)</td></tr>
  <tr><td>DELETE</td><td>Kill a console.</td><td>(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/files/sharing/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td>GET</td><td>Check sharing status for a path.  Returns 404 if path not currently shared.</td><td>Query parameter: path</td></tr>
  <tr><td>POST</td><td>Start sharing a file.  Returns 201 on success, or 200 if file was already shared.</td><td>POST parameter: path</td></tr>
  <tr><td>DELETE</td><td>Stop sharing a path.  Returns 204 on successful unshare.</td><td>Query parameter: path</td></tr>
</table>


### /api/v0/user/{username}/files/tree/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td>GET</td><td>Returns a list of the contents of a directory, and its subdirectories
as a list. Paths ending in slash/ represent directories.  Limited to
1000 results.</td><td>(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/webapps/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td>GET</td><td>List all webapps</td><td>(no parameters)</td></tr>
  <tr><td>POST</td><td>Create a new webapp with manual configuration.</td><td>POST parameters: domain_name, python_version</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td>GET</td><td>Return information about a web app's configuration</td><td>(no parameters)</td></tr>
  <tr><td>PUT</td><td>Modify configuration of a web app. (NB a reload is usually required to apply changes).</td><td>python_version, virtualenv_path</td></tr>
  <tr><td>PATCH</td><td>Modify configuration of a web app. (NB a reload is usually required to apply changes).</td><td>python_version, virtualenv_path</td></tr>
  <tr><td>DELETE</td><td>Delete the webapp.  This will take the site offline.
Config is backed up in /var/www, and your code is not touched.</td><td>(no parameters)</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/reload/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td>POST</td><td>Reload the webapp to reflect changes to configuration and/or source code on disk.</td><td>POST parameters: none.</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/static_files/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td>GET</td><td>List all the static files mappings for a domain.</td><td>(no parameters)</td></tr>
  <tr><td>POST</td><td>Create a new static files mapping. (webapp restart required)</td><td>url, path</td></tr>
</table>


### /api/v0/user/{username}/webapps/{domain_name}/static_files/{id}/

<table class="table table-striped">
  <tr><th>Method</th><th>Description</th><th>Parameters</th>
  <tr><td>GET</td><td>Get URL and path of a particular mapping.</td><td>(no parameters)</td></tr>
  <tr><td>PUT</td><td>Modify a static files mapping. (webapp restart required)</td><td>url, path</td></tr>
  <tr><td>PATCH</td><td>Modify a static files mapping. (webapp restart required)</td><td>url, path</td></tr>
  <tr><td>DELETE</td><td>Remove a static files mapping. (webapp restart required)</td><td>(no parameters)</td></tr>
</table>

All endpoints are hosted at *http://www.pythonanywhere.com/*

