from Sitter import Sitter
from Parent import Parent

class Reservation():
    """Kumuluje wszystkie dane potrzebne do utworzenia rezerwacji"""

    reservation_id: int 
    date: str
    start_hour: int 
    end_hour: int 
    sitter: Sitter
    parent: Parent 
    can_teach: bool 

    def __init__(
        self, 
        reservation_id: int, 
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

        self.reservation_id = reservation_id
        self.date = date
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.sitter = sitter
        self.parent = parent
        self.can_teach = can_teach

    def get_reservation_time(self) -> int:
        return self.end_hour - self.start_hour

    def get_reservation_info(self) -> str:
        out = f'ID rezerwacji: {self.reservation_id}\n'
        out += f'ID rodzica: {self.parent.parent_id}\n'
        out += f'ID opiekunki: {self.sitter.sitter_id}\n'
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
