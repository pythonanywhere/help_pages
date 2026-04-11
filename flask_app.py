from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def root():
    return redirect("/page/")

@app.route('/page/FastHTML')
@app.route('/page/FastHTML/')
def fasthtml_redirect():
    return redirect("/pages/ASGICommandLine")

@app.route('/page/FastAPI')
@app.route('/page/FastAPI/')
def fastapi_redirect():
    return redirect("/pages/ASGICommandLine")

@app.route('/page/AsgiDjango')
@app.route('/page/AsgiDjango/')
def asgi_django_redirect():
    return redirect("/pages/ASGICommandLine")
