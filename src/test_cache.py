from unittest import TestCase
from CacheClient import CacheClient
from time import sleep

class CacheTest(TestCase):
    EXPIRE_TIME = 3
    cc = CacheClient('redis_config.yml')
    
    def test_add(self):
        self.assertTrue(self.cc.add('test:123', { '_id': 123, 'name': 'Ryszard' }))

        # allow overwriting
        self.assertTrue(self.cc.add('test:123', { '_id': 123, 'name': 'Janek' }, expire_seconds = self.EXPIRE_TIME))

    def test_remove(self):
        test = { '_id': 1, 'funnyNumber' : 727 }
        self.assertIsNone(self.cc.get('test:1'))

        self.cc.add('test:1', test)
        self.assertIsNotNone(self.cc.get('test:1'))

        self.cc.remove('test:1')
        self.assertIsNone(self.cc.get('test:1'))

    def test_get(self):
        test = { '_id': 123321, 'test': True }

        # not found
        self.assertIsNone(self.cc.get('test:123321'))

        self.cc.add('test:123321', test)

        # stored in cache
        self.assertEqual(test, self.cc.get('test:123321'))
 
    def test_get_expire_cache(self):
        test_dict = { '_id': 321, 'name': 'Jerzy', 'age': 49 }
        self.cc.add('test:321', test_dict, expire_seconds=self.EXPIRE_TIME)

        self.assertEqual(self.cc.get('test:321'), test_dict)

        # ensure expired data gets deleted
        sleep(self.EXPIRE_TIME)
        self.assertIsNone(self.cc.get('test:321'))

    def test_clear_cache(self):
        test_dict = { '_id': 321, 'name': 'Jerzy', 'age': 49 }
        self.cc.add('test:321', test_dict, expire_seconds=self.EXPIRE_TIME)

        self.assertIsNotNone(self.cc.get('test:321'))

        self.assertTrue(self.cc.clear_cache())

        self.assertIsNone(self.cc.get('test:321'))
