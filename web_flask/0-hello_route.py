#!usr/bin/python3
from Flask import Flask
app = Flask(__name__)

@app.route("/", strict_slashes=False)
def home():
    # home page route
    return ("Hello HBNB!")

if __name__ == __main__:
    # start server
    app.run(host='0.0.0.0', port=5000)
