from DatabaseObject import DatabaseObject

from uuid import uuid4
from collections import namedtuple

class Sitter(DatabaseObject):
    """Bazowa klasa opiekunki dla dzieci"""

    table_name = 'sitters'
    sitter_type = 'sitter'

    @staticmethod
    def create_from_row(db_row: namedtuple) -> object:
        s = Sitter(db_row.s_first_name, db_row.s_last_name, db_row.s_base_price)
        s.s_id = db_row.s_id
        return s

    def add_to_database(self) -> str:
        return self._add_to_database(self.sitter_type)

    def _add_to_database(self, s_type: str) -> str:
        return f"""
        INSERT INTO {self.table_name}(s_id, s_sitter_type, s_first_name, s_last_name, s_base_price, s_is_available, as_bonus, as_max_age)
        VALUES ({self.s_id}, '{s_type}', '{self.s_first_name}', '{self.s_last_name}', {self.s_base_price}, {self.s_is_available}, {self.as_bonus}, {self.as_max_age});
        """

    def delete_from_database(self) -> str:
        return f"""
        DELETE FROM {self.table_name}
        WHERE s_id = {self.s_id};
        """

    def update_data(self) -> str:
        return f"""
        UPDATE {self.table_name}
        SET
            s_first_name = '{self.s_first_name}',
            s_last_name = '{self.s_last_name}',
            s_base_price = {self.s_base_price},
            s_is_available = {self.s_is_available},
            as_bonus = {self.as_bonus},
            as_max_age = {self.as_max_age}
        WHERE s_id = {self.s_id};
        """

    def __init__(
        self, 
        first_name: str, 
        last_name: str,
        base_price: float
    ):
        if not first_name or not first_name.split():
            raise ValueError("Wprowadz poprawne imie opiekunki!")

        if not last_name or not last_name.split():
            raise ValueError("Wprowadz poprawne nazwisko opiekunki!")

        if base_price <= 0:
            raise ValueError("Cena podstawowa powinna byc wieksza od zera.")

        self.s_id = uuid4()
        self.s_first_name = first_name
        self.s_last_name = last_name
        self.s_base_price = base_price
        self.s_is_available = True

        self.as_bonus = None
        self.as_max_age = None

    def set_available(self, is_available: bool):
        self.s_is_available = is_available
        