#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask
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


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """ Function called with /c/<text> route """
    return 'C %s' % text.replace('_', ' ')


if __name__ == "__main__":
    """ start server """
    app.run(host='0.0.0.0', port=5000)
