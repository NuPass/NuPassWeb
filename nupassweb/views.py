"""
    views.py
    ~~~~~~~~

    The URL processing portion of the application.

    :copyright: (c) 2017 by Sean Callaway.
    :license: GNU GPL v2, see LICENSE for more details.
"""
from flask import render_template, request, jsonify
import nupass
from nupassweb import app

@app.route('/')
def index():
    """Main page view."""
    return render_template('index.html')

@app.route('/gen_pass')
def gen_pass():
    """Generate passwords view.

    HTTP GET ARGUMENTS:
    qty -- the number of passwords to generate (default 5)
    """

    pass_list = []

    qty = request.args.get('qty', 5, type=int)
    notice = 0
    notice_str = ""
    if qty > 20:
        qty = 20
        notice = 2
        notice_str = "If more than 20 passwords are required, please rerun the " \
                 "tool or consider using the command-line version.\n\n"
    for _ in range(0, qty):
        pass_dict = {'password' : nupass.gen_pass()}
        pass_list.append(pass_dict)

    return jsonify(rows=notice+qty, notice_str=notice_str, passwords=pass_list)

@app.errorhandler(404)
def page_not_found(e):
    return render_template("error.html", error_code='404', 
                           error_msg="The page you're looking for can't be found."
                           ), 404

@app.errorhandler(500)
def int_server_error(e):
    return render_template("error.html", error_code='500', 
                           error_msg="Something went wrong. We're looking into it."
                           ), 500