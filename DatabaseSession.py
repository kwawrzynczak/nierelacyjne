from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine

class DatabaseSession():
    """Fabryka sesji korzystania z bazy danych"""

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
            isolation_level='SERIALIZABLE',
            echo=False
        )

        self.factory = sessionmaker(bind=self.engine)

    def create_new_session(self) -> Session:
        return self.factory()
