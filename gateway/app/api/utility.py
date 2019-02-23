import os
from app.api.application_api import api
from flask import jsonify
from flask_restplus import Resource

# Required routes

service_name = os.getenv('SERVICE_NAME') or 'not set'
version = os.getenv('CURRENT_VERSION') or 'not set'

@api.route("/health")
class Health(Resource):
    def get(self):
        ''' Provides status of "UP" '''
        return jsonify(status='UP')


@api.route("/info")
class Info(Resource):
    def get(self):
        ''' Provides name and current version '''
        return jsonify(name=service_name, version=version)
