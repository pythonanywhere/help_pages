<!--
.. title: How to connect production Vue frontend with a Python backend
.. slug: Vue
.. date: 2022-05-09
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

> Note -- you may need at least the basic Hacker plan because of
> the amount of disk space required to install Vue with all its
> dependencies and CPU seconds consummed during the installation


# Disclaimer

There are multiple possible ways of using Vue with a backend
framework -- steps presented below are showing one possible way of
connecting those on PythonAnywhere to make rather a starting point for
further adjustments.


# Prerequisites

It's assumed that you have a working Node.js environment on your
PythonAnywhere account -- otherwise follow steps mentioned on [this
help page](https://help.pythonanywhere.com/pages/Node/).


# Creating a scaffold Vue frontend app

Install Vue:

```sh
npm install -g @vue/cli
```

As a sanity check, run:

```sh
vue --version
```

Then, assuming your web app (Django or Flask) is at `~/mysite` directory:

```sh
cd ~/mysite
vue create frontend
```


# Django

It's assumed you created a Django web app in `~/mysite` with our
wizard on the Web app page.  The solution presented below assumes as
well that Vue takes care about the templates (and possibly routing
too), so that database connections will be performed in the client
(browser) via API calls.  If you prefer to partially render the
templates server-side (Django driven) and create templates in Django,
you will need extra dependencies allowing rendering the Vue's bundle
via Django (see:
[django-webpack-loader](https://pypi.org/project/django-webpack-loader/)
and
[webpack-bundle-tracker](https://github.com/django-webpack/webpack-bundle-tracker)).

## Build the Vue app

First, update the `vue.config.js` file in the Vue app's directory
(`~/mysite/frontend/`) to :

```js

module.exports = {
    ...
    publicPath: "/dist",
    outputDir: "./dist/",
    ...
};
```

Note that the value of `publicPath` will affect the routing and static
files mappings (see: [below](#static-files-mappings)) -- in our
example the Vue assets will be looked for in
`username.pythonawhere.com/dist`, and the assets will be found in
`~/mysite/frontend/dists`.

See also the [Vue documentation](https://cli.vuejs.org/config/) for reference.

Then, still in `~/mysite/frontend`, run:

```sh
npm run build
```

The successful build should add `dist` directory according to the
configuration in the `vue.config.js`, with `index.html` template
inside:

```sh
~/mysite/frontend $ tree -I node_modules
.
...
├── dist
│   ├── css
│   │   └── app.2cf79ad6.css
│   ├── favicon.ico
│   ├── index.html
│   └── js
│       ├── app.e82b6041.js
│       └── app.e82b6041.js.map
...
```

## `urls.py`

Adjust `~/mysite/mysite/urls.py` to serve the `base.html` template:

```py
from django.contrib import admin
from django.urls import path, re_path
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    # you can put the API endpoints here
    ...
    re_path("^.*$", TemplateView.as_view(template_name="index.html")),
]
```

**Note**: the solution above, using `re_path` and a regex pattern for
the url, assumes that all urls that are not caught by the previous urls
(the admin one and, say, APIs) will be forward to Vue.

## `settings.py`

In `~/mysite/mysite/settings.py`:

Than, assuming that `BASE_DIR` is a `pathlib.Path` object (you may need to
adjust the syntax if you use `os.path` instead), tell Django where to
look for Vue generated templates (`index.html` in our case):

```python
TEMPLATES = [
    {
        ...
        'DIRS': [ BASE_DIR / "frontend/dist" ],
        ...
    },
]
```

## Static files mappings

On your web app page add static files mappings to the `dist` directory
and reload the web app (use your **username** instead of "username"):

| URL          | Directory                           |
|--------------|-------------------------------------|
| ...          | ...                                 |
| /dist/	   | /home/username/mysite/frontend/dist |

You should now see the default Vue page when you visit your web app.


# Flask

It's assumed you created a Flask web app in `~/mysite` with our wizard
on the Web app page.

## Build the Vue app

Go to the `~/mysite/frontend`, where we already created the Vue
application and edit the `vue.config.js` file so it contains:

```js
module.exports = {
    outputDir: "./dist",
    assetsDir: "static",
}
```

This set up will put build assets into `dist/static` and create the
`index.html` template in the `dist` directory. See also the [Vue
documentation](https://cli.vuejs.org/config/) for reference.

Then run the build command in `~/mysite/frontend`:

```sh
npm run build
```

That should create the `dist` directory with the structure provided in
the configuration file above:

```sh
~/mysite/frontend $ tree -I node_modules
.
...
├── dist
│   ├── favicon.ico
│   ├── index.html
│   └── static
│       ├── css
│       │   └── app.2cf79ad6.css
│       └── js
│           ├── app.b7710a01.js
│           ├── app.b7710a01.js.map
│           ├── chunk-vendors.1ce598bf.js
│           └── chunk-vendors.1ce598bf.js.map
...
```

## `flask_app.py`

Edit the `~/mysite/flask_app.py` file to serve the default
`inbox.html` template provided by the Vue build (make sure that the
`static_folder` and the `template_folder` are not the same):

```python
from flask import Flask, render_template

app = Flask(__name__, static_folder = "frontend/dist/static", template_folder = "frontend/dist")

@app.route('/')
def index():
    return render_template("index.html")
```

## Static files mappings

On your web app page add static files mappings to the `dist` directory
and reload the web app (use your **username** instead of "username"):

| URL          | Directory                                   |
|--------------|---------------------------------------------|
| /static/	   | /home/username/mysite/frontend/dist/static  |

You should now see the default Vue page when you visit your web app.
