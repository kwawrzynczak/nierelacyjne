from DatabaseClient import DatabaseClient

from uuid import UUID

class Repository():
    """klasa zajmujaca sie obsluga danych z bazy danych"""

    def __init__(self):
        dc = DatabaseClient()

        self.db = dc.mongo_db
        self.cache = dc.redis_db
        self.root = dc.cache_root
        
    def add(self, collection_name: str, document: dict, use_cache: bool = True) -> UUID | None:
        inserted_id = self._add_to_db(collection_name, document)
        if use_cache: self._add_to_cache(f'{collection_name}:{document["_id"]}', document)

        return inserted_id

    def remove(self, collection_name: str, document: dict) -> int:
        # in case it was also stored in cache
        self.cache.json().delete(f'{collection_name}:{document["_id"]}')
        collection = self.db[collection_name]
        return collection.delete_one({ '_id': document['_id'] }).deleted_count

    def get(self, collection_name: str, _id: str, use_cache: bool = True) -> dict | None:
        if not use_cache:
            return self._get_from_db(collection_name, _id)

        doc = self._get_from_cache(f'{collection_name}:{_id}')
        if not doc: # tried to get from cache but failed
            doc = self._get_from_db(collection_name, _id)
            self._add_to_cache(f'{collection_name}:{_id}', doc)

        return doc

    def find_all(self, collection_name: str) -> list[dict]:
        collection = self.db[collection_name]
        return list(collection.find())

    def find_by(self, collection_name: str, filter: dict) -> list[dict]:
        collection = self.db[collection_name]
        return list(collection.find(filter))

    def _add_to_db(self, collection_name: str, document: dict) -> UUID | None:
        collection = self.db[collection_name]
        return collection.insert_one(document).inserted_id

    def _add_to_cache(self, cache_key: str, document: dict, expire_seconds: int = DatabaseClient.CACHE_EXPIRE_SECONDS) -> bool:
        print(f'adding {cache_key} to cache. data will expire after {expire_seconds} seconds')
        rslt = self.cache.json().set(cache_key, self.root, document)
        self.cache.expire(cache_key, expire_seconds)
        return rslt

    def _get_from_cache(self, cache_key: str) -> dict | None:
        rslt = self.cache.json().get(cache_key)
        
        if rslt: print(f'retrieved {cache_key} from cache')
        else: print(f'failed to retrieve {cache_key} from cache')
        
        return rslt

    def _get_from_db(self, collection_name: str, _id: str) -> dict | None:
        collection = self.db[collection_name]
        return collection.find_one({ '_id': _id })
