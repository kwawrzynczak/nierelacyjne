from DatabaseClient import DatabaseClient

from uuid import UUID

class Repository():
    """klasa zajmujaca sie obsluga danych z bazy danych"""

    def __init__(self):
        self.dc = DatabaseClient()
        
    def add(self, collection_name: str, document: dict) -> UUID | None:
        collection = self.dc.db[collection_name]
        ins_id = collection.insert_one(document).inserted_id

        return ins_id

    def remove(self, collection_name: str, document: dict) -> int:
        collection = self.dc.db[collection_name]
        del_count = collection.delete_one({ '_id': document['_id'] }).deleted_count

        return del_count

    def get(self, collection_name: str, id: str) -> dict | None:
        collection = self.dc.db[collection_name]
        result = collection.find_one({ '_id': id })
        
        return result

    def find_all(self, collection_name: str) -> list[dict]:
        collection = self.dc.db[collection_name]
        result = collection.find()

        return list(result)

    def find_by(self, collection_name: str, filter) -> list[dict]:
        collection = self.dc.db[collection_name]
        result = collection.find(filter)

        return list(result)
