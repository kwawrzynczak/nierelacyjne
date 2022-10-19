from Base import Base

from sqlalchemy import Column, Integer, String, Float, Boolean, true

class Sitter(Base):
    """Bazowa klasa opiekunki dla dzieci"""

    __tablename__ = 'sitters'

    id = Column(Integer, autoincrement=True, primary_key=True) 
    first_name = Column(String(50))
    last_name = Column(String(50))
    base_price = Column(Float, nullable=False)
    is_available = Column(Boolean, default=True)

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

        self.first_name = first_name
        self.last_name = last_name
        self.base_price = base_price

    def set_available(self, is_available: bool):
        self.is_available = is_available
        