from nameko.events import event_handler
from nameko.rpc import rpc

class StudentService:

    name = 'student_service'

    @rpc
    def ping(self):
        return 'alive'
