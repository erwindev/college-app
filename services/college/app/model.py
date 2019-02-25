from sqlalchemy.dialects.postgresql import UUID
import datetime
from sqlalchemy import Column, Integer, Float, DateTime, String
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
        return '<Temp Table: {} {}>'.format(
            self.id,
            self.name
        )

    def as_dict(self):
        dict_result = {
            'id': self.id,
            'name': self.name
        }
        return dict_result

class College(DeclarativeBase):
    __tablename__ = 'college'
    unitid = Column(String(10), primary_key=True)
    name = Column(String(200))
    address1 = Column(String(200))
    city = Column(String(50))
    state = Column(String(5))
    phone = Column(String(20))
    web_url = Column(String(300))
    admissions_url = Column(String(300))
    application_url = Column(String(300))
    netprice_url = Column(String(300))
    netprice_url = Column(String(300))
    netprice_url = Column(String(300))
    sector = Column(String(3))
    hbcu = Column(String(3))
    locale = Column(String(3))
    longitude = Column(Float())
    latitude = Column(Float())

    def __repr__(self):
        return '<College: {} {}>'.format(
            self.unitid,
            self.name
        )

    def as_dict(self):
        dict_result = {
            'unitid': self.unitid,
            'name': self.name,
            'address1': self.address1,
            'city': self.city,
            'state': self.state,
            'phone': self.phone,
            'web_url': self.web_url,
            'admissions_url': self.admissions_url,
            'application_url': self.application_url,
            'netprice_url': self.netprice_url,
            'sector': self.sector,
            'hbcu': self.hbcu,
            'locale': self.locale,
            'longitude': self.longitude,
            'latitude': self.latitude            
        }
        return dict_result

    def props_dict(self):
        d = self.as_dict()
        d.pop('unitid')
        return d