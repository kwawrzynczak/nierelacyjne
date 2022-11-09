from Sitter import Sitter

from dataclasses import dataclass, field
from uuid import UUID, uuid4

@dataclass
class Housekeeper(Sitter):
    """Klasa pomocy domowej"""

    sitter_id: UUID
    _id: UUID
    
    def __init__(self, first_name: str, last_name: str, base_price: float):
        self.sitter_id = super().__init__(first_name, last_name, base_price)
        self._id = uuid4()

    def get_actual_price(self) -> float: 
        return self.base_price

    def get_sitter_info(self) -> str: 
        out = f'ID opiekunki: {self.id}\n'
        out += f'Opiekunka {self.first_name} {self.last_name}\n'
        out += 'Pomoc domowa\n'
        out += f'Cena podstawowa: {self.base_price}\n'

        return out

    def get_max_age(self) -> int:
        return self.max_age
