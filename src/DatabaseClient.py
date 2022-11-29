from pymongo import MongoClient
from redis import Redis
from redis.commands.json.path import Path

class DatabaseClient():
    """Klient bazy danych"""

    CACHE_EXPIRE_SECONDS = 20

    def __init__(self):
        connection_string = 'mongodb://dsosnia:mIsFgTGBvDDG33JMgCqBCxAN9iPhNp5mee5cJVkPCWnCfQFoB5TJbHvB3Xj3uJAyUvur8bOTTZHz0Hux8PG4xg==@dsosnia.mongo.cosmos.azure.com:10255/?ssl=true&replicaSet=globaldb&retrywrites=false&maxIdleTimeMS=120000&appName=@dsosnia@'
        client = MongoClient(connection_string)

        # dostep do bazy dantch o nazwie 'nierelacyjne'
        self.mongo_db = client['nierelacyjne']

        self.redis_db = Redis(
            'localhost',
            6379,
            db=0
        )

        self.cache_root = Path.root_path()
        