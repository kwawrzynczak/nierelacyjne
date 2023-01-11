from Sitter import Sitter
from DatabaseObject import DatabaseObject

from uuid import uuid4
from collections import namedtuple

class Housekeeper(Sitter, DatabaseObject):
    """Klasa pomocy domowej"""

    table_name = 'sitters'
    sitter_type = 'housekeeper'

    @staticmethod
    def create_from_row(db_row: namedtuple) -> object:
        s = Housekeeper(db_row.s_first_name, db_row.s_last_name, db_row.s_base_price)
        s.s_id = db_row.s_id
        return s

    def add_to_database(self) -> str:
        return super()._add_to_database(self.sitter_type)

    def delete_from_database(self) -> str:
        return super().delete_from_database()
    
    def update_data(self) -> str:
        return super().update_data()

    def __init__(self, first_name: str, last_name: str, base_price: float):
        super().__init__(first_name, last_name, base_price)

    def get_actual_price(self) -> float: 
        return self.s_base_price

    def get_sitter_info(self) -> str: 
        out = f'ID opiekunki: {self.s_id}\n'
        out += f'Opiekunka {self.s_first_name} {self.s_last_name}\n'
        out += 'Pomoc domowa\n'
        out += f'Cena podstawowa: {self.s_base_price}\n'

        return out

    def get_max_age(self) -> int:
        return 0
