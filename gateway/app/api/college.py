import os
from app.api.application_api import api
from flask import jsonify
from flask_restplus import Resource
from app.service.college import CollegeService
from app.application_exception import ApplicationException


@api.route("/college/ping")
class CollegePingService(Resource):
    def get(self):
        ''' Checks to see if college service is alive and kicking '''
        college_service = CollegeService()
        ret = college_service.ping()
        return jsonify(status=ret)

@api.route("/college/v1/sample")
class CollegeSample(Resource):
    """
    This class contains the functions to run the API request.
    HTTP methods are implemented as functions.  Currently,
    this API only supports HTTP GET
    """

    def get(self):
        """Run the sample request"""
        try:
            college_service = CollegeService()
            message = college_service.process()
            return jsonify(message=message)
        except ApplicationException as e:
            error_message = str(e)
            return jsonify(message=error_message[:200])    
