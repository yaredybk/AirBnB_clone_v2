#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """home page route"""
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb page route"""
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def hbnb():
    """hbnb page route"""
    return (f"C {escape(text).replace('_', ' ')}")


@app.route("/number/<int:n>", strict_slashes=False)
def hbnb():
    """hbnb page route"""
    return (f"{n} is a number")


@app.route("/number_template/<int:n>", strict_slashes=False)
def hbnb():
    """hbnb page route"""
    return render_template('5-number.html', number=n)


if __name__ == '__main__':
    """start server"""
    app.run(host='0.0.0.0', port=5000)
