from DatabaseClient import DatabaseClient
from CacheClient import CacheClient

from uuid import UUID

class Repository():
    """klasa zajmujaca sie obsluga danych"""

    def __init__(self):
        self.db = DatabaseClient()
        self.cache = CacheClient('redis_config.yml')
        
    def add(self, collection_name: str, document: dict, use_cache: bool=True) -> UUID | None:
        inserted_id = self.db.add(collection_name, document)
        if use_cache: self.cache.add(f'{collection_name}:{document["_id"]}', document)

        return inserted_id

    def remove(self, collection_name: str, document: dict, use_cache: bool=True) -> int:
        if use_cache: self.cache.remove(f'{collection_name}:{document["_id"]}')

        return self.db.remove(collection_name, document)

    def get(self, collection_name: str, _id: UUID, use_cache: bool=True) -> dict or None:
        if not use_cache: return self.db.get(collection_name, _id)

        doc = self.cache.get(f'{collection_name}:{_id}')
        if not doc: # tried to get from cache but failed
            doc = self.db.get(collection_name, _id)
            self.cache.add(f'{collection_name}:{_id}', doc)

        return doc

    def find_all(self, collection_name: str) -> list[dict]:
        return self.db.find_all(collection_name)

    def find_by(self, collection_name: str, projection: dict) -> list[dict]:
        return self.db.find_by(collection_name, projection)

    def clear_cache(self) -> bool:
        return self.cache.clear_cache()
