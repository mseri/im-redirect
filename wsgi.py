#!/usr/bin/env python
import os

IP = os.environ.get('OPENSHIFT_PYTHON_IP','127.0.0.1')
PORT = int(os.environ.get('OPENSHIFT_PYTHON_PORT',8080))

from app import app

#
# Below for testing only
#
if __name__ == '__main__':
    from wsgiref.simple_server import make_server
    httpd = make_server(IP, PORT, app)
    # Wait for a single request, serve it and quit.
    httpd.serve_forever()
