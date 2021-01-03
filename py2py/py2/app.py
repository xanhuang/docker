from flask import Flask, render_template
import os
import random
import requests

app = Flask(__name__)

@app.route("/")
def index():
    r = requests.get('http://www.google.com')
    return r.text

@app.route("/call")
def call():
    r = requests.get('http://pyhello:8888/hello')
    return r.text

if __name__ == "__main__":
    #app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))
    app.run(host="0.0.0.0", port=7777)