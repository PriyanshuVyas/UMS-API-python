from connection import app
from flask import jsonify

@app.errorhandler(500)
def server_error(error=None):
    message = {
        'status': 500,
        'message': 'Server Error',
    }
    res = jsonify(message)
    res.status_code = 500

    return res

@app.errorhandler(401)
def bad_request(error=None):
    message={
        "status" : 401,
        "message" : "Bad Request"
    }
    res = jsonify(message)
    res.status_code = 401
    return res

@app.errorhandler(404)
def not_found(error=None):
    message={
        "status" : 404,
        "message" : "ID not found"
    }
    res = jsonify(message)
    res.status_code = 404
    return res