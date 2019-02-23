from app import rpc

class CollegeService:

    def ping(self):
        return rpc.college_service.ping()

    def process(self):
        return rpc.college_service.process()
