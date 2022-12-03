#!/usr/bin/python3
"""  a script that starts a Flask web application: """

from flask import Flask, render_template
from models import storage
from models import State
app = Flask(__name__)


@app.teardown_appcontext
def teardown(exception):
    """ Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/states/', strict_slashes=False)
def no_cities():
    """states only"""
    states = storage.all('State')
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def state_and_cities(id):
    """by id"""
    for state in storage.all("State").values():
        if state.id == id:
            return render_template("9-states.html", state=state)
    return render_template("9-states.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
