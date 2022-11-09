from Reservation import Reservation
from Repository import Repository
from Sitter import Sitter
from Housekeeper import Housekeeper
from AcademicSitter import AcademicSitter
from Parent import Parent

from uuid import UUID

class ReservationManager():
    collection_name = 'reservations'

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
    ) -> Reservation:

        reservation = Reservation(date, start_hour, end_hour, sitter, parent, can_teach)
        self.repo.add(self.collection_name, reservation.as_dict())
        return reservation

    def remove_reservation(self, reservation: Reservation) -> int:
        return self.repo.remove(self.collection_name, reservation.as_dict())

    def get_reservation(self, reservation_id: str) -> Reservation:
        reservation_dict = self.repo.get(self.collection_name, reservation_id)
        return Reservation.load_from_dict(reservation_dict)

    def find_reservations(self, filter) -> list[Reservation]:
        reservations_dict = self.repo.find_by(self.collection_name, filter)
        return [Reservation.load_from_dict(r) for r in reservations_dict]

    def find_all_reservations(self) -> list[Reservation]:
        reservations_dict = self.repo.find_all(self.collection_name)
        return [Reservation.load_from_dict(r) for r in reservations_dict]

        