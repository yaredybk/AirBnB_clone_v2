#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask, render_template
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ home page route """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ hbnb page route """
    return ("HBNB")


@app.route("/c/<text>", strict_slashes=False)
def c_is(text):
    """ hbnb page route """
    return ("C %s" % escape(text).replace('_', ' '))


@app.route("/python/<text>", strict_slashes=False)
@app.route("/python", strict_slashes=False)
def python(text="is cool"):
    """ hbnb page route """
    return ("Python %s" % escape(text).replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def is_num(n):
    """ hbnb page route """
    return ("%d is a number" % n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def num_temp(n):
    """ hbnb page route """
    return render_template('5-number.html', n=n)


if __name__ == "__main__":
    """ start server """
    app.run(host='0.0.0.0', port=5000)
