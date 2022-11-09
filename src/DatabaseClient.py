from pymongo import MongoClient
from Child import Child

class DatabaseClient():
    """Klient bazy danych"""

    def __init__(self):
        connection_string = 'mongodb://dsosnia:mIsFgTGBvDDG33JMgCqBCxAN9iPhNp5mee5cJVkPCWnCfQFoB5TJbHvB3Xj3uJAyUvur8bOTTZHz0Hux8PG4xg==@dsosnia.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@dsosnia@'
        client = MongoClient(connection_string)

        # dostep do bazy dantch o nazwie 'nierelacyjne'
        self.db = client['nierelacyjne']
