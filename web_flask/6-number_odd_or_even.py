#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
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


@app.route('/number/<int:n>', strict_slashes=False)
def num(n):
    """func"""
    return "%d is a number" % n


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    """func"""
    return render_template("5-number.html", n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def num_odd_even(n):
    """func"""
    answer = "even" if n % 2 == 0 else "odd"
    return render_template("6-number_odd_or_even.html", n=n, o_e=answer)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
