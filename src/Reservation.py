from Sitter import Sitter
from Housekeeper import Housekeeper
from AcademicSitter import AcademicSitter
from Parent import Parent

from uuid import UUID, uuid4

class Reservation(Base):
    """Kumuluje wszystkie dane potrzebne do utworzenia rezerwacji"""

    _id: UUID
    sitter_id: UUID
    parent_id: UUID 
    date: str 
    start_hour: int 
    end_hour: int 
    can_teach: bool 

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

        self._id = uuid4()
        self.parent = self.parent._id
        self.sitter_id = self.sitter._id

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

    def as_dict(self) -> dict:
        sitter = self.sitter.as_dict()
        parent = self.parent.as_dict()

        return {
            '_id': self._id.__str__(),
            'date': self.date,
            'start_hour': self.start_hour,
            'end_hour': self.end_hour,
            'can_teach': self.can_teach,
            'sitter': sitter,
            'parent': parent
        }

    @staticmethod
    def load_from_dict(reservation: dict) -> object:
        sitter_type = reservation['sitter']['type']

        if sitter_type == 'sitter': sitter = Sitter.load_from_dict(reservation['sitter'])
        elif sitter_type == 'housekeeper': sitter = Housekeeper.load_from_dict(reservation['sitter'])
        elif sitter_type == 'academic': sitter = AcademicSitter.load_from_dict(reservation['sitter'])
        else: sitter = None

        parent = Parent.load_from_dict(reservation['parent'])

        r = Reservation(reservation['date'], reservation['start_hour'], reservation['end_hour'], sitter, parent, reservation['can_teach'])

        return r