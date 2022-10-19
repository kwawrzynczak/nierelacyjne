from Sitter import Sitter
from Base import Base

from sqlalchemy import Column, ForeignKey, Integer, CheckConstraint

class Housekeeper(Sitter, Base):
    """Klasa pomocy domowej"""

    __tablename__ = 'housekeepers'
    __table_args__ = (
        CheckConstraint('max_age >= 0')
    )

    sitter_id = Column(ForeignKey(Sitter.sitter_id))
    max_age = Column(Integer)
    
    def __init__(self, first_name: str, last_name: str, base_price: float):
        super().__init__(first_name, last_name, base_price)
        self.max_age = 0

    def get_actual_price(self) -> float: 
        return self.base_price

    def get_sitter_info(self) -> str: 
        out = f'ID opiekunki: {self.sitter_id}\n'
        out += f'Opiekunka {self.first_name} {self.last_name}\n'
        out += 'Pomoc domowa\n'
        out += f'Cena podstawowa: {self.base_price}\n'

        return out

    def get_max_age(self) -> int:
        return self.max_age
