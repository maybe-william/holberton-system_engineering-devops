#!/usr/bin/python3
"""This module runs the flask application server"""

from flask import Flask, escape, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb_filters', strict_slashes=False)
def hello_states():
    """display template with states"""
    states = []
    amen = []
    for k, v in storage.all().items():
        if k.split(".")[0] == 'State':
            states.append(v)
        elif k.split(".")[0] == 'Amenity':
            amen.append(v)
    states.sort(key=lambda x: x.name)
    amen.sort(key=lambda x: x.name)
    return render_template('10-hbnb_filters.html', states=states, amen=amen)


@app.teardown_appcontext
def hello_goodbye(exc):
    """close the storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
