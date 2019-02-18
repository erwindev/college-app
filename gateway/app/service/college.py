from app import rpc

class CollegeService:

    def process(self):
        return rpc.college_service.ping()
        