import pytest
import testing.postgresql
from nameko.testing.services import worker_factory
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.service import StudentService
from app.model import TempTable, DeclarativeBase

def test_service():

    # create instance, providing the test database session
    with testing.postgresql.Postgresql() as postgresql:    
        engine = create_engine(postgresql.url())
        DeclarativeBase.metadata.create_all(engine)    
        session_cls = sessionmaker(bind=engine)
        session = session_cls()

        service = worker_factory(StudentService, db=session)

        # verify ``save`` logic by querying the test database
        name = service.process('Erwin Alberto')
        assert name == 'Erwin Alberto'
