import os
import socket
import json
from datadog import initialize, statsd

from flask import Flask, request

initialize(statsd_host=os.environ['HOST'], statsd_port=8125)
app = Flask(__name__)


@app.route('/')
def hello():
    provider = str(os.environ.get('PROVIDER', 'world'))
    statsd.increment('hagerren.page.index.hits')
    return 'Hello ' + provider + '!'


@app.route("/hostname")
def return_hostname():
    statsd.increment('hagerren.page.hostname.hits')
    return "This is an example wsgi app served from {} to {}".format(socket.gethostname(), request.remote_addr)


@app.route("/version")
def return_version():
    statsd.increment('hagerren.page.version.hits')
    return "version 1.26 on host {}".format(socket.gethostname())

@app.route("/headers")
def return_headers():
    statsd.increment('hagerren.page.headers.hits')
    return str(request.headers)

@app.route("/http_code")
def return_http_code():
    code = request.args.get('code', default = 200, type = int)
    statsd.increment('hagerren.page.http_code.hits')
    return str(code), code

@app.route("/health")
def return_health():
    code = request.args.get('code', default = 200, type = int)
    statsd.increment('hagerren.page.health.hits')
    return "Healthy", 200

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('CONTAINER_PORT', 5000))
    app.run(host='0.0.0.0', port=port)
