from flask import request
from flask import jsonify

from . import app
from . import snipper


class ClientError(Exception):
    def __init__(self, message, status_code=400, payload=None):
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        rv = dict(self.payload or ())
        rv['message'] = self.message
        return rv


@app.errorhandler(ClientError)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.route("/api/snip", methods=['POST'])
def snip():
    data = request.get_json(force=True)
    url = data.get('url')
    reusable = data.get('reusable', False)
    if not url:
        raise ClientError("Cannot shorten empty URL", 400)

    app.logger.info(f"Snipping url {url}")
    snip = snipper.snip(url, reusable)
    return {"url": url, "snip": snip}


@app.route("/api/unsnip/<snip>", methods=['GET'])
def unsnip(snip):
    url = snipper.unsnip(snip)
    if not url:
        raise ClientError(f"Snip {snip} not found", 404)

    return {"url": url, "snip": snip}
