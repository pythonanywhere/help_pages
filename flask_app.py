from flask import Flask, redirect

app = Flask(__name__)

@app.route('/')
def root():
    return redirect("/pages/")
