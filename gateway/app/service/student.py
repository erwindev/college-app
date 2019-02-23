from app import rpc

class StudentService:

    def ping(self):
        return rpc.student_service.ping()

    def process(self):
        return rpc.student_service.process()    
