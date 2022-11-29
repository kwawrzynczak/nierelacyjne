from unittest import TestCase
from Repository import Repository
from DatabaseClient import DatabaseClient
from time import sleep

class TestRepository(Repository):
    def __init__(self):
        super().__init__()

    # make cache methods public
    def add_to_cache(self, cache_key: str, document: dict, expire_seconds: int = DatabaseClient.CACHE_EXPIRE_SECONDS) -> bool:
        return self._add_to_cache(cache_key, document, expire_seconds=expire_seconds)

    def get_from_cache(self, cache_key: str) -> dict | None:
        return self._get_from_cache(cache_key)

class CacheTest(TestCase):
    EXPIRE_TIME = 3
    repo = TestRepository()
    
    def test_add(self):
        self.assertTrue(self.repo.add_to_cache('test:123', { '_id': 123, 'name': 'Ryszard' }, expire_seconds = self.EXPIRE_TIME))

        # allow overwriting
        self.assertTrue(self.repo.add_to_cache('test:123', { '_id': 123, 'name': 'Janek' }, expire_seconds = self.EXPIRE_TIME))
 
    def test_get(self):
        test_dict = { '_id': 321, 'name': 'Jerzy', 'age': 49 }
        self.repo.add_to_cache('test:321', test_dict, expire_seconds=self.EXPIRE_TIME)

        self.assertEqual(self.repo.get_from_cache('test:321'), test_dict)

        # ensure expired data gets deleted
        sleep(self.EXPIRE_TIME)
        self.assertIsNone(self.repo.get_from_cache('test:321'))
