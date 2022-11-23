from DatabaseClient import DatabaseClient, DatabaseError
from redis import ResponseError

class Repository():
    """klasa zajmujaca sie obsluga danych z bazy danych
        Przedrostki klucza (w zaleznosci od klasy):
            - sitter
            - housekeeper
            - academic
            - child
            - parent
            - reservation

        Przyklad: sitter:1 -> pokojowka z _id = 1
    """

    def __init__(self):
        self.dc = DatabaseClient()
        
    def add(self, name: str, value: object, overwrite: bool = False):
        if type(value) == dict: # dodajemy nowy obiekt klasy w postaci json
            result = self.dc.db.json().set(name, self.dc.json_root, value)
        else: # cos innego
            result = self.dc.db.set(name, value, nx=not overwrite)

        if result == None or result == False:
            raise DatabaseError('Failed to add new item to the database.')

    def remove(self, name: str) -> int:
        json = self.dc.db.json().delete(name)
        return self.dc.db.delete(name) + json

    def get(self, name: str) -> object:
        try:
            result = self.dc.db.get(name)
        except ResponseError: # chcemy dostac obiekt klasy
            result = self.dc.db.json().get(name)

        if result == None:
            raise DatabaseError(f'Failed to retrieve {name}. Pair does not exist.')

        return result

    def find_all(self, prefix: str) -> list[dict]:
        _, keys = self.dc.db.scan(match=prefix)

        return self.dc.db.json().mget(keys, self.dc.json_root)

    def find_by(self, prefix: str, predicate: dict) -> list[dict]:
        _, keys = self.dc.db.scan(match=prefix)

        out = []
        for obj in self.dc.db.json().mget(keys, self.dc.json_root):
            matching = True

            for key, value in predicate.items():
                if obj[key] != value:
                    matching = False
                    break

            if matching:
                out.append(obj)
        
        return out
