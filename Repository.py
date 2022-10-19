from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import text

Base = declarative_base()

class Repository():

    def __init__(self):
        dialect = 'postgresql'
        driver = 'psycopg2'
        username = 'nbd'
        password = 'nbdpassword'
        host = 'localhost'
        port = 5432
        database = 'nbddb'

        self.engine = create_engine(
            f'{dialect}+{driver}://{username}:{password}@{host}:{port}/{database}',
            echo=True
        )

        self.session_creator = sessionmaker(bind=self.engine)
        

    def add(self, obj: Base):
        db = self.session_creator()
        db.add(obj)
        db.commit()

        print(db.query(type(obj)).count())
        db.close()

    def remove(self, obj: Base):
        db = self.session_creator()
        db.delete(obj)
        db.close()

repo = Repository()

