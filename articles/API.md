
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


## consoles

list: GET /api/v0/user/{username}/consoles/
List all your consoles
(no parameters)

shared_with_you: GET /api/v0/user/{username}/consoles/shared_with_you/
View consoles shared with you
(no parameters)

read: GET /api/v0/user/{username}/consoles/{id}/
Return information about a console instance.
(no parameters)

delete: DELETE /api/v0/user/{username}/consoles/{id}/
Kill a console.
(no parameters)


## files

### sharing

list: GET /api/v0/user/{username}/files/sharing/
Check sharing status for a path.  Returns 404 if path not currently shared.
Query parameter: path
(no parameters)

create: POST /api/v0/user/{username}/files/sharing/
Start sharing a file.  Returns 201 on success, or 200 if file was already shared.
POST parameter: path
(no parameters)

delete: DELETE /api/v0/user/{username}/files/sharing/
Stop sharing a path.  Returns 204 on successful unshare.
Query parameter: path
(no parameters)


### tree

list: GET /api/v0/user/{username}/files/tree/
Returns a list of the contents of a directory, and its subdirectories
as a list. Paths ending in slash/ represent directories.  Limited to
1000 results.
(no parameters)



## webapps

### web app configuration

list: GET /api/v0/user/{username}/webapps/
List all webapps
(no parameters)

create: POST /api/v0/user/{username}/webapps/
Create a new webapp with manual configuration.
POST parameters: domain_name, python_version

read: GET /api/v0/user/{username}/webapps/{domain_name}/
Return information about a web app's configuration
(no parameters)

update: PUT /api/v0/user/{username}/webapps/{domain_name}/
Modify configuration of a web app. (NB a reload is usually required to apply changes).
parameters: python_version, virtualenv_path

partial_update: PATCH /api/v0/user/{username}/webapps/{domain_name}/
Modify configuration of a web app. (NB a reload is usually required to apply changes).
parameters: python_version, virtualenv_path

delete: DELETE /api/v0/user/{username}/webapps/{domain_name}/
Delete the webapp.  This will take the site offline.
Config is backed up in /var/www, and your code is not touched.
(no parameters)

reload: POST /api/v0/user/{username}/webapps/{domain_name}/reload/
Reload the webapp to reflect changes to configuration and/or source code on disk.
POST parameters: none.


### static_files

<table>
<tr><td>
list: GET /api/v0/user/{username}/webapps/{domain_name}/static_files/ <br/>
List all the static files mappings for a domain. <br/>
(no parameters) <br/>
</tr></td>

<tr><td>
create: POST /api/v0/user/{username}/webapps/{domain_name}/static_files/ <br />
Create a new static files mapping. (webapp restart required) <br />
parameters: url, path <br />
</tr></td>

<tr><td>
read: GET /api/v0/user/{username}/webapps/{domain_name}/static_files/{id}/ <br />
Get URL and path of a particular mapping. <br />
(no parameters) <br />
</tr></td>

<tr><td>
update: PUT /api/v0/user/{username}/webapps/{domain_name}/static_files/{id}/ <br />
Modify a static files mapping. (webapp restart required) <br />
parameters: url, path <br />
</tr></td>

<tr><td>
partial_update: PATCH /api/v0/user/{username}/webapps/{domain_name}/static_files/{id}/ <br />
Modify a static files mapping. (webapp restart required) <br />
parameters: url, path <br />
</tr></td>

<tr><td>
delete: DELETE /api/v0/user/{username}/webapps/{domain_name}/static_files/{id}/ <br />
Remove a static files mapping. (webapp restart required) <br />
(no parameters) <br />
</tr></td>

</table>

