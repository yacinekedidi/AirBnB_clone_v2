#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, escape
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """func"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """func"""
    return "HBNB"


@app.route('/c/<string:t>', strict_slashes=False)
def c(t):
    """func"""
    t = t.replace("_", " ")
    return "C %s" % t

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
