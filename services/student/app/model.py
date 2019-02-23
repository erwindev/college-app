from sqlalchemy.dialects.postgresql import UUID
import datetime
from sqlalchemy import Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

class Base(object):
    created_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        nullable=False
    )
    updated_at = Column(
        DateTime,
        default=datetime.datetime.utcnow,
        onupdate=datetime.datetime.utcnow,
        nullable=False
    )

DeclarativeBase = declarative_base(cls=Base)

class TempTable(DeclarativeBase):
    __tablename__ = 'temp_table'
    id = Column(UUID, primary_key=True)
    name = Column(String(256))

    def __repr__(self):
        return '<Temp Table: {} {} {}>'.format(
            self.id,
            self.name
        )

    def to_json(self):
        json_job_result = {
            'id': self.id,
            'name': self.name
        }
        return json_job_result
