#!/usr/bin/env python
"""
    NuPassWeb.fcgi
    ~~~~~~~~~~~~~~

    An fcgi file for running NuPassWeb in production.

    :copyright: (c) 2017 by Sean Callaway.
    :license: GNU GPL v2, see LICENSE for more details.
"""
from flup.server.fcgi import WSGIServer
from nupassweb import app

if __name__ == '__main__':
    WSGIServer(app).run()
