"""
    __init__.py
    ~~~~~~~~~~~

    The init script for the nupassweb package.

    :copyright: (c) 2017 by Sean Callaway.
    :license: GNU GPL v2, see LICENSE for more details.
"""
from flask import Flask

app = Flask(__name__)

from nupassweb import views
