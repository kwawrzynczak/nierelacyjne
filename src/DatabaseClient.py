import redis
from redis.commands.json.path import Path

class DatabaseClient():
    """Klient bazy danych"""

    db: redis.Redis
    json_root: Path

    def __init__(self):
        self.json_root = Path.root_path()

        self.db = redis.Redis(
            host='localhost',
            port=6379,
        )

class DatabaseError(Exception):
    pass
