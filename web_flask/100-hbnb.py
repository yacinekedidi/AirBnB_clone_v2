#!/usr/bin/python3
"""a script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
app = Flask(__name__)


@app.teardown_appcontext
def remove_session(self):
    """After each request you must remove the current SQLAlchemy Session:"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """func"""
    states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    places = list(storage.all(Place).values())
    return render_template("100-hbnb.html", all_states=states,
                           all_amenities=amenities, all_places=places)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
