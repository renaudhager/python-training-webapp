import os
import socket
import json
from datadog import initialize, statsd

from flask import Flask, request, jsonify

if 'HOST' in os.environ:
    initialize(statsd_host=os.environ['HOST'], statsd_port=8125)

app = Flask(__name__)


def push_to_statsd(metric_name):
    if 'HOST' in os.environ:
        statsd.increment(metric_name)

@app.route('/')
def hello():
    provider = str(os.environ.get('PROVIDER', 'world'))
    push_to_statsd('hagerren.page.index.hits')
    return 'Hello ' + provider + '!'


@app.route('/polly/create/root/account')
def polly_create_root_account():
    return jsonify({"Please read": "My wonderful pdf."})


@app.route("/hostname")
def return_hostname():
    push_to_statsd('hagerren.page.hostname.hits')
    return "This is an example wsgi app served from {} to {}".format(socket.gethostname(), request.remote_addr)


@app.route("/version")
def return_version():
    push_to_statsd('hagerren.page.version.hits')
    return "version 1.26 on host {}".format(socket.gethostname())

@app.route("/headers")
def return_headers():
    push_to_statsd('hagerren.page.headers.hits')
    return str(request.headers)

@app.route("/http_code")
def return_http_code():
    code = request.args.get('code', default = 200, type = int)
    push_to_statsd('hagerren.page.http_code.hits')
    return str(code), code

@app.route("/health")
def return_health():
    code = request.args.get('code', default = 200, type = int)
    push_to_statsd('hagerren.page.health.hits')
    return "Healthy", 200

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('CONTAINER_PORT', 5000))
    app.run(host='0.0.0.0', port=port)
