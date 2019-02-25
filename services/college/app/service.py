from nameko.events import event_handler
from nameko.rpc import rpc
import uuid
from app.model import TempTable
from datetime import datetime
from nameko_sqlalchemy import DatabaseSession
from app.model import TempTable, College, DeclarativeBase
from sqlalchemy.dialects.postgresql import insert as pg_insert

class CollegeService:

    name = 'college_service'
    db = DatabaseSession(DeclarativeBase)

    @rpc
    def ping(self):
        return 'alive'

    @rpc
    def process(self, name):
        id = str(uuid.uuid4())
        temp_data = TempTable()
        temp_data.name = name
        temp_data.id = id

        self.db.add(temp_data)
        self.db.commit()
        temp_datax = self.db.query(TempTable).filter_by(id=id).first()

        return temp_datax.name

    @rpc
    def process_college(self, college_data):
        
        college = College()
        college.unitid = college_data['UNITID']
        college.name = college_data['INSTNM']
        college.address1 = college_data['ADDR']
        college.city = college_data['CITY']
        college.state = college_data['STABBR']
        college.phone = college_data['GENTELE']
        college.web_url = college_data['WEBADDR']
        college.admissions_url = college_data['ADMINURL']
        college.netprice_url = college_data['NPRICURL']
        college.sector = college_data['SECTOR']
        college.locale = college_data['LOCALE']
        college.hbcu = college_data['HBCU']
        college.latitude = college_data['LATITUDE']
        college.longitude = college_data['LONGITUD']

        #upsert
        statement = pg_insert(College).values(**college.as_dict()).on_conflict_do_update(constraint='college_pkey', set_=college.props_dict())        
        self.db.execute(statement)
        self.db.commit()

        return college.name
