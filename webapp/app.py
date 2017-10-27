import os
import socket
import json

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello():
    provider = str(os.environ.get('PROVIDER', 'world'))
    return 'Hello '+provider+'!'


@app.route("/hostname/")
def return_hostname():
    return "This is an example wsgi app served from {} to {}".format(socket.gethostname(), request.remote_addr)


@app.route("/version/")
def return_version():
    return "version 1.10 on host {}".format(socket.gethostname())

@app.route("/headers/")
def return_headers():
    return str(request.headers)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('CONTAINER_PORT', 5000))
    app.run(host='0.0.0.0', port=port)
