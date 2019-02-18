from nameko.events import event_handler
from nameko.rpc import rpc

class CollegeService:

    name = 'college_service'

    @rpc
    def ping(self):
        return 'alive'
