#!/usr/bin/python3
""" Script that runs an app with Flask framework """
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    """ home page route """
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ hbnb page route """
    return ("HBNB")


if __name__ == '__main__':
    """ start server """
    app.run(host='0.0.0.0', port=5000)
