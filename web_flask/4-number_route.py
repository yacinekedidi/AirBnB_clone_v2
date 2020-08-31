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
    return "C %s" % t.replace("_", " ")


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:t>', strict_slashes=False)
def p(t="is cool"):
    """func"""
    return "Python %s" % t.replace("_", " ")


@app.route('/number/<int:n>')
def num(n):
    """func"""
    return "%d is a number" % n

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
