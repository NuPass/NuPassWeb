#!venv/bin/python
"""
    run.py
    ~~~~~~

    Runs NuPassWeb in debug mode for local testing.

    :copyright: (c) 2017 by Sean Callaway.
    :license: GNU GPL v2, see LICENSE for more details.
"""
from nupassweb import app

app.run(debug=True)
