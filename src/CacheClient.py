from redis import Redis 
from redis.commands.json.path import Path
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
        print(f'adding {key} to cache. data will expire after {expire_seconds} seconds')
        result = self.cache.json().set(key, self.root_path, document)
        self.cache.expire(key, expire_seconds)

        return result

    def remove(self, key: str) -> int:
        return self.cache.json().delete(key)

    def get(self, key: str) -> dict or None:
        result = self.cache.json().get(key)

        if result: print(f'retrieved {key} from cache')
        else: print(f'failed to retrieve {key} from cache')

        return result

    def clear_cache(self) -> bool:
        print('clearing cache')
        return self.cache.flushdb()
