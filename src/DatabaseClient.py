from pymongo import MongoClient

class DatabaseClient():
    """Klient bazy danych"""

    def __init__(self):
        client = MongoClient(connection_string)

        # dostep do bazy dantch o nazwie 'nierelacyjne'
        self.db = client['nierelacyjne']


import redis
from redis.commands.json.path import Path
from Sitter import Sitter

r = redis.Redis(
    host='localhost',
    port=6379,
)

s = Sitter('first_name', 'last_name', 1300)

r.set('foo', 12)
# r.set('foo', s.as_dict())
r.json().set('sitter:1', Path.root_path(), s.as_dict())
value = r.json().get('sitter:1')

print(value)