#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(self):
    """After each request you must remove the current SQLAlchemy Session:"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def state_id(id=None):
    """func"""
    states = list(storage.all(State).values())
    if id is None:
        return render_template("9-states.html", a="States",
                               b="Cities", all_states=states)
    for s in states:
        if s.id == id:
            x = s
            return render_template("9-states.html", a="State",
                                   b="Cities", state_obj=x)
    return render_template("9-states.html", a="Not found!")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
