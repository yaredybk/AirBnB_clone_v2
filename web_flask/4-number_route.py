#!usr/bin/python3
from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def home():
    # home page route
    return ("Hello HBNB!")


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    # hbnb page route
    return ("HBNB")


@app.route("/c/<tmp>", strict_slashes=False)
def hbnb():
    # hbnb page route
    return (f"C {escape(tmp).replace('_', ' ')}")


@app.route("/number/<int:tmp>", strict_slashes=False)
def hbnb():
    # hbnb page route
    return (f"{tmp} is a number")


if __name__ == __main__:
    # start server
    app.run(host='0.0.0.0', port=5000)
