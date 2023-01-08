from DatabaseSession import DatabaseSession
from DatabaseObject import DatabaseObject

from uuid import UUID
from collections import namedtuple

class Repository():
    """klasa zajmujaca sie obsluga danych z bazy danych"""

    def __init__(self):
        self.ds = DatabaseSession()
        
    def add(self, obj: DatabaseObject):
        self.ds.add(obj)

    def remove(self, obj: DatabaseObject):
        self.ds.remove(obj)

    def get(self, _id: UUID, table_name: str, table_id_col: str=None) -> namedtuple:
        return self.ds.get(_id, table_name, table_id_col)

    def find_all(self, table_name: str) -> list[namedtuple]:
        return self.ds.find_all(table_name)

    def find_by(self, table_name: str, where_sql_clause: str) -> list[namedtuple]:
        return self.ds.find_by(table_name, where_sql_clause)
