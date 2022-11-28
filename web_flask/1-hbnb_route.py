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


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
