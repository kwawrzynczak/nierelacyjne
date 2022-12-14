from pymongo import MongoClient
from uuid import UUID

class DatabaseClient():
    """Klient bazy danych"""

    def __init__(self):
        connection_string = 'mongodb://localhost:27017'
        client = MongoClient(connection_string)

        self.db = client['nierelacyjne']

    def add(self, collection_name: str, document: dict) -> UUID:
        return self.db[collection_name].insert_one(document).inserted_id

    def remove(self, collection_name: str, document: dict) -> int:
        return self.db[collection_name].delete_one({ '_id': document['_id'] }).deleted_count

    def get(self, collection_name: str, _id: UUID) -> dict or None:
        return self.db[collection_name].find_one({ '_id': str(_id) })

    def find_all(self, collection_name: str) -> list[dict]:
        return list(self.db[collection_name].find())

    def find_by(self, collection_name: str, projection: dict) -> list[dict]:
        return list(self.db[collection_name].find(projection))
