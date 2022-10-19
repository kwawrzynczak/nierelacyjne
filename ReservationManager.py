from Reservation import Reservation
from Repository import Repository
from Sitter import Sitter
from Parent import Parent

class ReservationManager():

    def __init__(self):
        self.repo = Repository()

    def create_reservation(
        self,
        date,
        start_hour: int,
        end_hour: int,
        sitter: Sitter,
        parent: Parent,
        can_teach: bool
    ) -> bool:
        if not sitter.is_available:
            return False

        reservation = Reservation(date, start_hour, end_hour, sitter, parent, can_teach)
        self.repo.add(reservation)
        return True

    def get_reservation(self, predicate: Any) -> Reservation:
        return self.repo.find_by(Reservation, predicate)

    def get_all_reservations(self) -> list[Reservation]:
        return self.repo.find_all(Reservation)
        