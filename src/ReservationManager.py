from Reservation import Reservation
from Repository import Repository
from Sitter import Sitter
from Housekeeper import Housekeeper
from AcademicSitter import AcademicSitter
from Parent import Parent
from DatabaseClient import DatabaseError

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
    ) -> Reservation:

        try:
            rid = self.repo.get('reservation_id')
            new_reservation_id = rid + 1
        except DatabaseError:
            new_reservation_id = 1

        reservation = Reservation(new_reservation_id, date, start_hour, end_hour, sitter, parent, can_teach)
        self.repo.add(f'reservation:{new_reservation_id}', reservation.as_dict())

        self.repo.add('reservation_id', new_reservation_id, overwrite=True)

        return reservation

    def remove_reservation(self, reservation: Reservation) -> bool:
        return True if self.repo.remove(f'reservation:{reservation._id}') == 1 else False

    def get_reservation(self, reservation_id: int) -> Reservation:
        reservation_dict = self.repo.get(f'reservation:{reservation_id}')
        sitter_dict = self.repo.get(reservation_dict['sitter_id'])
        parent_dict = self.repo.get(f'parent:{reservation_dict["parent_id"]}')
        child_dict = self.repo.get(f'child:{parent_dict["child_id"]}')

        return Reservation.load_from_dict(reservation_dict, sitter_dict, parent_dict, child_dict)

    def find_reservations(self, predicate: dict) -> list[Reservation]:
        out = []

        for reservation_dict in self.repo.find_by('reservation', predicate):
            sitter_dict = self.repo.get(reservation_dict['sitter_id'])
            parent_dict = self.repo.get(f'parent:{reservation_dict["parent_id"]}')
            child_dict = self.repo.get(f'child:{parent_dict["child_id"]}')

            out.append(Reservation.load_from_dict(reservation_dict, sitter_dict, parent_dict, child_dict))

        return out


    def find_all_reservations(self) -> list[Reservation]:
        out = []

        for reservation_dict in self.repo.find_all('reservation'):
            sitter_dict = self.repo.get(reservation_dict['sitter_id'])
            parent_dict = self.repo.get(f'parent:{reservation_dict["parent_id"]}')
            child_dict = self.repo.get(f'child:{parent_dict["child_id"]}')

            out.append(Reservation.load_from_dict(reservation_dict, sitter_dict, parent_dict, child_dict))

        return out
        