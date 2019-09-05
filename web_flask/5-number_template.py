#!/usr/bin/python3
"""
States Rules for accessing parts of the web
"""
import flask
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
def text_var(text):
    """
    Return C, display text varible
    Set text variable
    """
    return "C {}".format(text.replace("_", " "))


@app.route("/python/", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_default(text='is cool'):
    """
    Return Python, display text variable as default
    Route depends on if text is provided
    Text default value = "is cool"
    """
    return "Python {}".format(text.replace("_", " "))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """
    Display n is a number if n is an integer
    """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def number_template(n):
    """
    Return n in a string if n is an integer
    """
    return render_template('5-number.html', Markup(n=n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
