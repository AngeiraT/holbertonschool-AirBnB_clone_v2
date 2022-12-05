#!/usr/bin/python3
"""  a script that starts a Flask web application: """

from flask import Flask, render_template
from models import storage
from models import State
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states/')
def no_cities():
    """states only"""
    states = storage.all(State)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>')
def state_and_cities(id):
    """by id"""
    states = storage.all(State)
    for state in states.values():
        if state.id == str(id):
            return render_template('9-states.html', states=state)
    return render_template('9-states.html')


@app.teardown_appcontext
def teardown(exception):
    """ Remove the current SQLAlchemy Session"""
    storage.close()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
