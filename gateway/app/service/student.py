from app import rpc

class StudentService:

    def process(self):
        return rpc.student_service.ping()
        