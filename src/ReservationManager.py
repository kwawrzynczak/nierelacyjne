from Reservation import Reservation
from Repository import Repository
from Sitter import Sitter
from Parent import Parent

from uuid import UUID

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
    ) -> UUID:
        if not sitter.s_is_available:
            return None

        reservation = Reservation(date, start_hour, end_hour, sitter, parent, can_teach)
        self.repo.add(reservation)
        return reservation.r_id

    def get_reservation(self, reservation_id: UUID) -> Reservation:
        reservation_row = self.repo.get(reservation_id, Reservation.table_name)

        if reservation_row is None:
            raise ValueError("No reservation found with this reservation_id")

        return Reservation.create_from_row(reservation_row)

    def find_reservations(self, where_sql_clause: str) -> list[Reservation]:
        found = self.repo.find_by(Reservation.table_name, where_sql_clause)
        return [Reservation.create_from_row(r_row) for r_row in found]

    def find_all_reservations(self) -> list[Reservation]:
        found = self.repo.find_all(Reservation.table_name)
        return [Reservation.create_from_row(r_row) for r_row in found]
        