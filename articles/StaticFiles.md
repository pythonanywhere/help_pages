
<!--
.. title: Static files mappings
.. slug: StaticFiles
.. date: 2015-05-13 14:35:28 UTC+01:00
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->



Our static files support is an optional extra. If you're happy letting your web
framework serve static files for you, then that's fine. Or if you want to you
can give the job of serving static files to our web servers, by setting up a
static files mapping -- it should mean your web worker has more time for
non-static requests, the ones that actually need code.

Static files config is basically a mapping from a URL to a directory. You tell
us where your files are (eg `/home/me/myapp/static`), and what URL you want
them served at (eg `/static/`) and then hit "Reload web app". Then, any files
inside the static folder will be served, eg
`/home/me/myapp/static/css/base.css` will appear at
`http://me.pythonanywhere.com/static/css/base.css`.


##A worked example


Supposing you have some static files stored like this:

    /home/myusername/myproject
    └── assets
        ├── css
        │   ├── base.css
        │   └── bootstrap.css
        ├── images
        │   ├── img1.jpg
        │   └── img2.png
        └── js
            └── widgets.js


And, supposing in one of your templates, you want to use some of your static assets, like this:

    :::html
    <link rel="stylesheet" link href="/static/css/base.css">
    <script type="text/javascript" src="/static/js/widgets.js"></script>
    [...]
    <img src="/static/images/img1.jpg">


The two things to note are:

  1. The URLs all start with `/static/`
  1. The path to the place where all your static files are stored is `/home/myusername/myproject/assets`

So, what you want is a static files mapping that says:

**The URL /static/ should map to the folder /home/myusername/myproject/assets**

Hopefully you can see how, after that, the relative paths are the same?

So now you know what to put in the two boxes on the Static files section in the web tab. Remember to hit "reload" when you're done. To test it, visit the URL of one of your static files directly. Remember to use Ctrl+F5 to force a reload of the page.


## Static files in Django

Please see [this specific help page on static files in Django](/pages/DjangoStaticFiles)


## Debugging static files issues

Please see [this page on debugging problems with static files](/pages/DebuggingStaticFiles)


