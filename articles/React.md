<!--
.. title: How to connect production React frontend with Python backend
.. slug: React
.. date: 2022-05-09
.. tags:
.. category:
.. link:
.. description:
.. type: text
-->

> Warning -- you may need at least the basic Hacker plan because of
> the amount of disk space required to install React with all its
> dependencies and CPU seconds consummed during the installation


# Disclaimer

There are multiple possible ways of using React with a backend
framework -- steps presented below are showing one possible way of
connecting those on PythonAnywhere to make rather a starting point for
further adjustments.


# Prerequisites

It's assumed that you have a working Node.js environment on your
PythonAnywhere account -- otherwise follow steps mentioned on [this
help page](https://help.pythonanywhere.com/pages/Node/).


# Creating a scaffold React frontend app

Assuming your web app (Django or Flask) is at `~/mysite` directory:

```sh
cd ~/mysite
npx create-react-app frontend
```

If that works fine, enter the `frontend` directory and create a
production build of the React app:

```sh
cd frontend
npm run build
```

That will add a `build` directory with a `static` subdirectory inside.
Have a look where `index.html` as well as `css` and `js` resources are
located:

```sh
~/mysite/frontend $ tree -I node_modules
...
├── build
│   ├── asset-manifest.json
│   ├── favicon.ico
│   ├── index.html
│   ├── logo192.png
│   ├── logo512.png
│   ├── manifest.json
│   ├── robots.txt
│   └── static
│       ├── css
│       │   ├── main.073c9b0a.css
│       │   └── main.073c9b0a.css.map
│       ├── js
│       │   ├── 787.cda612ba.chunk.js
│       │   ├── 787.cda612ba.chunk.js.map
│       │   ├── main.b7ea7086.js
│       │   ├── main.b7ea7086.js.LICENSE.txt
│       │   └── main.b7ea7086.js.map
│       └── media
│           └── logo.6ce24c58023cc2f8fd88fe9d219db6c6.svg
...
```


# Django

We assume you created a Django web app in `~/mysite` with our wizard on the Web app
page.

## settings.py

Open `~/mysite/mysite/settings.py`.

Assuming that `BASE_DIR` is a `pathlib.Path` object (you may need to
adjust the syntax if you use `os.path` instead), tell Django where to
look for the basic `index.html` template provided by React:

```python
FRONTEND_DIR = BASE_DIR / "frontend"

TEMPLATES = [
    {
        ...
        "DIRS": [
            FRONTEND_DIR / "build",
        ],
        ...
    },
]
```

Next, point Django to the static resources provided by the React
build:

```python
STATIC_URL = "/static/"
STATICFILES_DIRS = [
    FRONTEND_DIR / "build/static",
]
```

## urls.py

Let's use a simple `TemplateView` serving `index.html` provided by the
frontend app:

```python
from django.views.generic import TemplateView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", TemplateView.as_view(template_name="index.html")),
]
```

## Set static files mappings

Adjust the static files mappings to serve the React ones:

| URL          | Directory                                   |
|--------------|---------------------------------------------|
| /static/	   | /home/username/mysite/frontend/build/static |
  
If you want your admin to have a proper CSS, add this as well:

| /static/admin	| /home/username/mysite/static/admin |

Reload the web app and you should see the default React page when you
visit it.


# Flask

We assume you created a Flask web app in `~/mysite` with our wizard on the Web app
page.

##  flask_app.py

Open `~/mysite/flask_app.py` and edit it so it contains:

```python
from flask import Flask

app = Flask(__name__, static_folder="./frontend/build", static_url_path="/")

@app.route('/')
def index():
    return app.send_static_file('index.html')
```

## Static files mappings

Adjust the static files mappings to serve the React ones:

| URL          | Directory                                   |
|--------------|---------------------------------------------|
| /static/	   | /home/username/mysite/frontend/build/static |

Reload the web app and you should see the default React page when you
visit it.
