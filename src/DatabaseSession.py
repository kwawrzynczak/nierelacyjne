from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy import create_engine

class DatabaseSession():
    """Fabryka sesji korzystania z bazy danych"""

    def __init__(self):
        self.engine = create_engine(
            f'mongodb://dsosnia:mIsFgTGBvDDG33JMgCqBCxAN9iPhNp5mee5cJVkPCWnCfQFoB5TJbHvB3Xj3uJAyUvur8bOTTZHz0Hux8PG4xg==@dsosnia.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@dsosnia@',
            echo=True
        )

        self.factory = sessionmaker(bind=self.engine)

    def create_new_session(self) -> Session:
        return self.factory()
        