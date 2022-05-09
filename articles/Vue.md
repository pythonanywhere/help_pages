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

> Warning -- you may need at least the basic Hacker plan because of
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

Install vue:

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

We assume you created a Django web app in `~/mysite` with our wizard
on the Web app page.

## Installing dependencies

We will need
[django-webpack-loader](https://pypi.org/project/django-webpack-loader/)
for Django, and
[webpack-bundle-tracker](https://github.com/django-webpack/webpack-bundle-tracker)
for Vue.

Make sure you're using a correct `pip` command (see: [this help
page](https://help.pythonanywhere.com/pages/InstallingNewModules/)):

```sh
pip install django-webpack-loader
```

Again, assuming that the Vue app has been created in `~/mysite/frontend`:

```sh
cd ~/mysite/frontend
npm install --save-dev webpack-bundle-tracker
```

## Create a `base.html` template to render the Vue app

```sh
cd ~/mysite
mkdir templates
```

Then edit `~/mysite/templates/base.html` file:

```python
{% load render_bundle from webpack_loader %}

<!DOCTYPE html>
<html>
    <head>
        <meta charset="UTF-8">
        {% render_bundle 'app' 'css' %}
        <title>Django Vue App</title>
    </head>
    <body>
        <div id="app"></div>
        {% render_bundle 'app' 'js' %}
    </body>
</html>
```

## settings.py

In `~/mysite/mysite/settings.py`:

Add `django-webpack-loader` to installed applications:

```python
INSTALLED_APPS = [
    ...
    "webpack_loader",
]
```

Than, assuming that `BASE_DIR` is a `pathlib.Path` object (you may need to
adjust the syntax if you use `os.path` instead), tell Django where to
look for our new `base.html` template:

```python
TEMPLATES = [
    {
        ...
        'DIRS': [ BASE_DIR / "templates" ],
        ...
    },
]
```

Also add a `WEBPACK_LOADER` environment variable containing, among
other settings, the path to the `webpack-stats.json` file:

```python
FRONTEND_DIR = BASE_DIR / "frontend"
WEBPACK_LOADER = {
  'DEFAULT': {
    'CACHE': not DEBUG,
    'STATS_FILE': FRONTEND_DIR / 'webpack-stats.json',
    'POLL_INTERVAL': 0.1,
    'IGNORE': [r'.+\.hot-update.js', r'.+\.map'],
  }
}
```

See also [django-webpack-loader's
documentation](https://github.com/django-webpack/django-webpack-loader#configuring-the-settings-file)
for reference.

# Build the Vue app

First, update the `vue.config.js` file in the Vue app's directory
(`~/mysite/frontend/`):

```js
const BundleTracker = require('webpack-bundle-tracker');

module.exports = {
    publicPath: "/dist",
    outputDir: "./dist/",
    chainWebpack: config => {
        config.optimization.splitChunks(false)

        config.plugin('BundleTracker').use(BundleTracker, [
            {
                filename: './webpack-stats.json'
            }
        ])

    }
};
```

Note that the value of `publicPath` will affect the routing and static
files mappings (see: [below](#static-files-mappings)) -- in our example the Vue assets will be
looked for in `username.pythonawhere.com/dist`, and the assets will be
found in `~/mysite/frontend/dists`.

Also `webpack-stats.json` file path must match the path provided in
`WEBPACK_LOADER["STATS_FILE"]` in the `settings.py` file (see: [above](#settingspy)).

See also the [Vue documentation](https://cli.vuejs.org/config/) for reference.

Then, still in `~/mysite/frontend`, run:

```sh
npm run build
```

The successful build should add `dist` directory and the
`webpack-stats.js` file according to the configuration in the `vue.config.js`:

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
└── webpack-stats.js
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

## flask_app.py

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

Reload the web app and you should see the default Vue page after
visiting it.
