#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """Print a message from Flask"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Print hbnbn message from Flask"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """Displays C"""
    return "C %s" % text.replace('_', ' ')


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', defaults={'text': 'is cool'}, strict_slashes=False)
def python(text):
    """Displays Python default or not"""
    return "Python %s" % text.replace('_', ' ')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
