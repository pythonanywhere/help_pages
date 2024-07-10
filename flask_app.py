from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def root():
    return redirect("/pages/")

@app.route('/pages/FastHTML')
def fasthtml_redirect():
    return redirect("/pages/ASGICommandLine")

@app.route('/pages/FastAPI')
def fastapi_redirect():
    return redirect("/pages/ASGICommandLine")

@app.route('/pages/AsgiDjango')
def asgi_django_redirect():
    return redirect("/pages/ASGICommandLine")