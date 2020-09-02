#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(self):
    """After each request you must remove the current SQLAlchemy Session:"""
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def fil():
    """func"""
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    return render_template("10-hbnb_filters.html", all_states=states,
                           all_amenities=amenities)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
