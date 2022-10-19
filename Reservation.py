from Sitter import Sitter
from Parent import Parent
from Base import Base

from sqlalchemy import Column, Integer, String, Date, ForeignKey, CheckConstraint, Boolean, false
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship

class Reservation(Base):
    """Kumuluje wszystkie dane potrzebne do utworzenia rezerwacji"""

    __tablename__ = 'reservations'
    __table_args__ = (
        CheckConstraint('start_hour > 0 AND start_hour <= 24'),
        CheckConstraint('end_hour> 0 AND end_hour <= 24')
    )

    id = Column(Integer, autoincrement=True, primary_key=True) 
    date = Column(Date, server_default=func.now())
    start_hour = Column(Integer)
    end_hour = Column(Integer)
    sitter_id = Column(ForeignKey(Sitter.id), nullable=False)
    parent_id = Column(ForeignKey(Parent.id), nullable=False)
    can_teach = Column(Boolean, default=false)

    sitter = relationship(Sitter)
    parent = relationship(Parent)

    def __init__(
        self, 
        date: str, 
        start_hour: int, 
        end_hour: int,
        sitter: Sitter,
        parent: Parent,
        can_teach: bool
    ):
        # dopuszczalny zakres [1, 24] 24 -> polnoc
        if start_hour <= 0 or start_hour > 24:
            raise ValueError("Podana godzina rozpoczecia rezerwacji jest nieprawidlowa!")

        if end_hour <= 0 or end_hour > 24:
            raise ValueError("Podana godzina zakonczenia rezerwacji jest nieprawidlowa!")

        if sitter is None:
            raise ValueError("Obiekt opiekunki jest nieprawidlowy!")

        if parent is None:
            raise ValueError("Obiekt rodzica jest nieprawidlowy!")

        self.date = date
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.sitter = sitter
        self.parent = parent
        self.can_teach = can_teach

    def get_reservation_time(self) -> int:
        return self.end_hour - self.start_hour

    def get_reservation_info(self) -> str:
        out = f'ID rezerwacji: {self.id}\n'
        out += f'ID rodzica: {self.parent_id}\n'
        out += f'ID opiekunki: {self.sitter_id}\n'
        out += f'Data rezerwacji: {self.date}\n'
        out += f'Rezerwacja od {self.start_hour} do {self.end_hour}\n'
        out += f'Koszt rezerwacji: {self.get_reservation_cost()}\n'

        return out

    def get_reservation_cost(self) -> float:
        return self.sitter.get_actual_price() * self.get_reservation_time()

    def set_sitter(self, new_sitter: Sitter):
        if new_sitter is None:
            raise ValueError("Obiekt nowej opiekunki nie istnieje!")

        self.sitter = new_sitter
