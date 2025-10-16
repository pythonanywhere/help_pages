
<!--
.. title: Debugging issues with static files
.. slug: DebuggingStaticFiles
.. date: 2017-07-31 10:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



*"Help!  My static files aren't working!"*

CSS, JavaScript, or other static files not loading? Hopefully this guide can help.

##  First, have you actually set up your static files on the Web tab?

 
See [this general guide to static files](/pages/StaticFiles)
or [this specific guide to static files in Django](/pages/DjangoStaticFiles)


## If yes: examine a specific example.

Let's start with a specific example of a static file that's not working.

You need to identify 3 pieces of information:

* The **URL** which you expect to be able to load the static file from (eg *www.mydomain.com/static/path/to/myfile.css*)

* The **path** where this file is stored on disk, in your PythonAnywhere
  account(eg */home/myusername/myproject/assets/path/to/myfile.css*)

* The relevant **static files mapping** from the web tab, the values for its
  URL and path  settings (eg: URL `/static/` maps to path
  `/home/myusername/myproject/assets`)


By identifying these 3 pieces of information, you may already be able to figure
out what the problem is -- the static files mapping should be able to transform
the URL to the path on disk, exactly.

## How the static files mapping finds your file

Let's work through an example to show how the static files system finds your
file. 

If you have a css file that is referred to by */static/path/to/myfile.css* in
your HTML, you could use any of the following static files mappings (the first 2 columns
are the values that should be in the *Static files* table and the last is where
there needs to be a file for the mapping to work):


<table border="1">
<tr>
<th colspan="2">Entry in Static files table</th>
<th rowspan="2">Where the file must be</th>
</tr>
<tr>
<th>URL</th>
<th>Directory</th>
</tr>
<tr>
<td>/static</td>
<td>/home/username/mysite/assets/</td>
<td>/home/username/mysite/assets/path/to/myfile.css</td>
</tr>
<tr>
<td>/static/path/</td>
<td>/home/username/mysite/assets/</td>
<td>/home/username/mysite/assets/to/myfile.css</td>
</tr>
<tr>
<td>/static/path/to/</td>
<td>/home/username/mysite/assets/</td>
<td>/home/username/mysite/assets/myfile.css</td>
</tr>
</table>



## Common problems:

* The file is missing on disk

* The path to the file and the path in the URL don't quite match (eg, there's
  an extra level of folder hierarchy in one and not the other)

* **caching** -- if you've only just set up the mapping, the old 404
  response may be being cached by your browser.  Hit Shift+refresh a few times,
  or try a new browser tab.   You may also need to give our distributed filesystem
  a few seconds to catch up if you've only just added the target file to the disk.

* **Case-sensitivity** -- Both the URL (after the domain name) and the path on
  disk are case-sensitive.  so `Path/To/MyFile.css != path/to/myfile.css`.

* Your static files mapping is not active yet.  You may need to reload your web app.

* You've used a relative path instead of an absolute path in the URL in your HTML (eg
  'static/css/myfile.css' instead of '/static/css/myfile.css' -- this will work
  for some paths on your site but not others.  best to use absolute paths
  everywhere)
  
* You have a mapping where the file path is an individual file. In this case,
  the mapping will override all the following mappings where the URL starts
  with the URL of the single-file mapping. For instance, if you first mapping
  is / -> /home/user/myfile.html, then all the following mappings will be
  ignored and myfile.html will be served for all URLs.


