#!/usr/bin/python3
"""This module runs the flask application server"""

from flask import Flask, escape, render_template
from models import storage

app = Flask(__name__)


@app.route('/hbnb', strict_slashes=False)
def hello_states():
    """display template with everything"""
    st = []
    am = []
    pl = []
    us = []
    for k, v in storage.all().items():
        cls = k.split('.')[0]
        if cls == 'State':
            st.append(v)
        elif cls == 'Amenity':
            am.append(v)
        elif cls == 'Place':
            pl.append(v)
        elif cls == 'User':
            us.append(v)
    st.sort(key=lambda x: x.name)
    am.sort(key=lambda x: x.name)
    pl.sort(key=lambda x: x.name)
    for i in pl:
        i.own = "Bob Nonexistent"
        for u in us:
            if u.id == i.user_id:
                i.own = u.first_name + " " + u.last_name
    return render_template('100-hbnb.html', st=st, am=am, pl=pl)


@app.teardown_appcontext
def hello_goodbye(exc):
    """close the storage"""
    storage.close()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
