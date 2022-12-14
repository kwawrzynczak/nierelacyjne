from redis import Redis 
from redis.commands.json.path import Path
from redis.exceptions import ConnectionError
from yaml import safe_load, YAMLError

class CacheClient():
    """Klient cache'a"""

    CACHE_EXPIRE_SECONDS = 20

    def __init__(self, config_filepath: str):
        with open(config_filepath, 'r') as cfg:
            try:
                data = safe_load(cfg)
            except YAMLError as e:
                print(e)

        self.root_path = Path.root_path()
        self.cache = Redis(
            data['host'],
            data['port'],
            db=data['db'],
        )
        
    def add(self, key: str, document: dict, expire_seconds: int=CACHE_EXPIRE_SECONDS) -> bool:
        try:
            result = self.cache.json().set(key, self.root_path, document)
            print(f'adding {key} to cache. data will expire after {expire_seconds} seconds')
        except ConnectionError:
            return

        self.cache.expire(key, expire_seconds)
        return result

    def remove(self, key: str) -> int:
        try:
            return self.cache.json().delete(key)
        except ConnectionError:
            return

    def get(self, key: str) -> dict or None:
        try:
            result = self.cache.json().get(key)
        except ConnectionError:
            return

        if result: print(f'retrieved {key} from cache')
        else: print(f'failed to retrieve {key} from cache')

        return result

    def clear_cache(self) -> bool:
        try:
            print('clearing cache')
            return self.cache.flushdb()
        except ConnectionError:
            return
