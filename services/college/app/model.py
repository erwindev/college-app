from sqlalchemy.dialects.postgresql import UUID
import datetime
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class TempTable(Base):
    __tablename__ = 'temp_table'
    id = Column(UUID, primary_key=True)
    name = Column(String(256))
    create_date = Column(DateTime)

    def __repr__(self):
        return '<Temp Table: {} {} {}>'.format(
            self.id,
            self.name,
            self.create_date
        )

    def to_json(self):
        json_job_result = {
            'id': self.id,
            'name': self.name,
            'create_date': self.create_date
        }
        return json_job_result
