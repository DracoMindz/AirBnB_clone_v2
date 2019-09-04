#!/usr/bin/python3
"""
States Rules for accessing parts of the web
"""

from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Return Hello HBNB """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Return HBNB """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def text_var():
    """
    Return C, display text varible
    Set text variable
    """
    return "C {}".format(text.replace("_", " "))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
