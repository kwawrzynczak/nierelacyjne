from Sitter import Sitter
from Housekeeper import Housekeeper
from AcademicSitter import AcademicSitter
from Parent import Parent

class Reservation():
    """Kumuluje wszystkie dane potrzebne do utworzenia rezerwacji"""

    _id: int
    sitter_id: int
    parent_id: int 
    date: str 
    start_hour: int 
    end_hour: int 
    can_teach: bool 

    def __init__(
        self, 
        _id: int,
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

        self._id = _id
        self.parent_id = parent._id
        self.sitter_id = sitter._id

        self.date = date
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.sitter = sitter
        self.parent = parent
        self.can_teach = can_teach

    def get_reservation_time(self) -> int:
        return self.end_hour - self.start_hour

    def get_reservation_info(self) -> str:
        out = f'ID rezerwacji: {self._id}\n'
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
        if type(self.sitter) == Sitter:
            sitter_prefix = 'sitter:'
        elif type(self.sitter) == Housekeeper:
            sitter_prefix = 'housekeeper:'
        elif type(self.sitter) == AcademicSitter:
            sitter_prefix = 'academic:'

        return {
            '_id': self._id,
            'sitter_id': f'{sitter_prefix}:{self.sitter._id}',
            'parent_id': self.parent._id,
            'date': self.date,
            'start_hour': self.start_hour,
            'end_hour': self.end_hour,
            'can_teach': self.can_teach,
        }

    @staticmethod
    def load_from_dict(reservation: dict, sitter: dict, parent: dict, child: dict) -> object:
        sitter_type = sitter['type']
        if sitter_type == 'sitter': s = Sitter.load_from_dict(reservation['sitter'])
        elif sitter_type == 'housekeeper': s = Housekeeper.load_from_dict(reservation['sitter'])
        elif sitter_type == 'academic': s = AcademicSitter.load_from_dict(reservation['sitter'])
        else: s = None

        return Reservation(
            reservation['_id'],
            reservation['date'], 
            reservation['start_hour'],
            reservation['end_hour'], 
            s,
            Parent.load_from_dict(parent, Child.load_from_dict(child)),
            reservation['can_teach']
        )
