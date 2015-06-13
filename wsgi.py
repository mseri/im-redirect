#!/usr/bin/env python3

from app import app

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server('localhost', 8051, app)
    # Wait for a single request, serve it and quit.
    httpd.serve_forever()
