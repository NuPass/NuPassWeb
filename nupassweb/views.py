"""
    views.py
    ~~~~~~~~

    The URL processing portion of the application.

    :copyright: (c) 2017 by Sean Callaway.
    :license: GNU GPL v2, see LICENSE for more details.
"""
from flask import render_template, request
from nupass import gen_pass
from nupassweb import app

@app.route('/')
def index():
    """Main page view.

    HTTP GET ARGUMENTS:
    qty -- the number of passwords to generate (default 5)
    """
    qty = int(request.args.get('qty', '5'))
    notice = 0
    passes = ""
    if qty > 30:
        qty = 30
        notice = 2
        passes = "If more than 30 passwords are required, please rerun the " \
                 "tool or consider using the command-line version.\n\n"
    for _ in range(0, qty):
        passes = passes + gen_pass() + "\n"
    return render_template('index.html', passwords=passes, numRows=qty+notice)
