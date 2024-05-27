#!/usr/bin/env python3
"""
Route module for the API
"""
from logging import exception
from os import getenv
from api.v1.views import app_views
from flask import Flask, jsonify, abort, request
import os


app = Flask(__name__)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})


@app.errorhandler(404)
def not_found(error) -> str:
    """
    returns Not found handler
    """
    return jsonify({"error": "Not found"}), 404


@app.errorhandler(401)
def unauthorized(error) -> str:
    '''
    unauthorized error handler jsonify
    arguments error type desciption
    returns str description
    '''
    return jsonify({'error': 'Unauthorized'}), 401


@app.errorhandler(403)
def forbidden(error) -> str:
    '''
    user is authenicated and not allowed
    arguments error type
    rturns str forbidden
    '''
    return jsonify({'error': 'Forbidden'}), 403


if __name__ == "__main__":
    host = getenv("API_HOST", "0.0.0.0")
    port = getenv("API_PORT", "5000")
    app.run(host=host, port=port)
