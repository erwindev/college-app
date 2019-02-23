import os
from app.api.application_api import api
from flask import jsonify
from flask_restplus import Resource
from app.service.student import StudentService
from app.application_exception import ApplicationException


@api.route("/student/ping")
class StudentPingService(Resource):
    def get(self):
        ''' Checks to see if student service is alive and kicking '''
        student_service = StudentService()
        ret = student_service.ping()
        return jsonify(status=ret)

@api.route("/student/v1/sample")
class StudentSample(Resource):
    """
    This class contains the functions to run the API request.
    HTTP methods are implemented as functions.  Currently,
    this API only supports HTTP GET
    """

    def get(self):
        """Run the sample request"""
        try:
            student_service = StudentService()
            message = student_service.process()
            return jsonify(message=message)
        except ApplicationException as e:
            error_message = str(e)
            return jsonify(message=error_message[:200])    
