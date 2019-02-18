import os
from app.api.application_api import api
from flask import jsonify
from flask_restplus import Resource
from app.service.college import CollegeService
from app.service.student import StudentService

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

@api.route("/ping-college-service")
class CollegePingService(Resource):
    def get(self):
        ''' Checks to see if college service is alive and kicking '''
        college_service = CollegeService()
        ret = college_service.process()
        return jsonify(status=ret)

@api.route("/ping-student-service")
class StudentPingService(Resource):
    def get(self):
        ''' Checks to see if student service is alive and kicking '''
        student_service = StudentService()
        ret = student_service.process()
        return jsonify(status=ret)
