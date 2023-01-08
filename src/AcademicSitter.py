from Sitter import Sitter
from DatabaseObject import DatabaseObject

from uuid import uuid4
from collections import namedtuple

class AcademicSitter(Sitter, DatabaseObject):
    """Opiekunka akademicka z mozliwoscia nauczania dziecka"""

    table_name = 'sitters'
    sitter_type = 'academic'

    @staticmethod
    def create_from_row(db_row: namedtuple) -> object:
        a = AcademicSitter(db_row.s_first_name, db_row.s_last_name, db_row.s_base_price, db_row.as_bonus, db_row.as_max_age)
        a.s_id = db_row.s_id
        return a

    def add_to_database(self) -> str:
        return super()._add_to_database(self.sitter_type)
        
    def delete_from_database(self) -> str:
        return super().delete_from_database()

    def update_data(self) -> str:
        return super().update_data()

    def __init__(
        self, 
        first_name: str, 
        last_name: str, 
        base_price: float,
        bonus: float,
        max_age: int
    ):
        if bonus <= 1:
            raise ValueError("Mnoznik bonusu musi byc wiekszy od 1.") 

        if max_age < 1:
            raise ValueError("Maksymalny wiek dziecka nieprawidlowy!")
        
        super().__init__(first_name, last_name, base_price)
        self.as_bonus = bonus
        self.as_max_age = max_age

    def get_actual_price(self) -> float:
        self.s_base_price * self.as_bonus

    def get_sitter_info(self) -> str:
        out = f'ID opiekunki: {self.id}\n'
        out += f'Opiekunka {self.s_first_name} {self.s_last_name}\n'
        out += f'Typ opiekunki: Academic\n'
        out += f'Cena podstawowa: {self.s_base_price}\n'
        out += f'Mnoznik bonusu: {self.as_bonus}\n'
        out += f'Maksymalny wiek dziecka do nauczania: {self.as_max_age}\n'
        
        return out

    def get_max_age(self) -> int:
        return self.as_max_age
