"""
    views.py
    ~~~~~~~~

    The URL processing portion of the application.

    :copyright: (c) 2017 by Sean Callaway.
    :license: GNU GPL v2, see LICENSE for more details.
"""
from flask import render_template
from nupassweb import app, nupass

@app.route('/')
def index():
    passes = ""
    for i in range(0, 5):
        passes = passes + nupass.gen_pass() + "\n"
    return render_template('index.html', passwords=passes)
