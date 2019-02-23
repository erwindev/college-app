from nameko.events import event_handler
from nameko.rpc import rpc
import uuid
from app.model import TempTable
from datetime import datetime
from nameko_sqlalchemy import DatabaseSession
from app.model import TempTable, DeclarativeBase

class CollegeService:

    name = 'student_service'
    db = DatabaseSession(DeclarativeBase)

    @rpc
    def ping(self):
        return 'alive'

    @rpc
    def process(self):
        id = str(uuid.uuid4())
        temp_data = TempTable()
        temp_data.name = 'Erwin Alberto - {}'.format(id)
        temp_data.id = id

        self.db.add(temp_data)
        self.db.commit()
        temp_datax = self.db.query(TempTable).filter_by(id=id).first()

        return 'I JUST RAN THIS PROCESS FOR {}'.format(temp_datax.name)
