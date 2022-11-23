from Sitter import Sitter
from Housekeeper import Housekeeper
from AcademicSitter import AcademicSitter
from Repository import Repository
from DatabaseClient import DatabaseError

class SitterManager():

    def __init__(self):
        self.repo = Repository()

    def create_sitter(
        self,
        collection_name: str,
        first_name: str,
        last_name: str,
        base_price: float,
        bonus: float = 1,
        max_age: int = 0
    ) -> Sitter:

        if collection_name == 'sitters':
            try:
                sid = int(self.repo.get('sitter_id'))
                new_sitter_id = sid + 1
            except DatabaseError:
                new_sitter_id = 1

            sitter = Sitter(new_sitter_id, first_name, last_name, base_price)
            self.repo.add(f'sitter:{new_sitter_id}', sitter.as_dict(), overwrite=True)
            self.repo.add('sitter_id', new_sitter_id, overwrite=True)

        if collection_name == 'housekeepers':
            try:
                hid = int(self.repo.get('housekeeper_id'))
                new_sitter_id = hid + 1
            except DatabaseError:
                new_sitter_id = 1

            sitter = Housekeeper(new_housekeeper_id, first_name, last_name, base_price)
            self.repo.add(f'housekeeper:{new_housekeeper_id}', sitter.as_dict())
            self.repo.add('housekeeper_id', new_housekeeper_id, overwrite=True)

        if collection_name == 'academic_sitters':
            try:
                aid = int(self.repo.get('academic_id'))
                new_sitter_id = aid + 1
            except DatabaseError:
                new_sitter_id = 1

            sitter = AcademicSitter(new_academic_id, first_name, last_name, base_price, bonus, max_age)
            self.repo.add(f'academic:{new_academic_id}', sitter.as_dict())
            self.repo.add('academic_id', new_academic_id, overwrite=True)

        return sitter

    def remove_sitter(self, collection_name: str, sitter: Sitter) -> int:
        if collection_name == 'sitters':
            return True if self.repo.remove(f'sitter:{sitter._id}') == 1 else False

        if collection_name == 'housekeepers':
            return True if self.repo.remove(f'housekeeper:{housekeeper._id}') == 1 else False

        if collection_name == 'academic_sitters':
            return True if self.repo.remove(f'academic:{academic._id}') == 1 else False


    def get_sitter(self, collection_name: str, sitter_id: int) -> Sitter:

        if collection_name == 'sitters':
            sitter_dict = self.repo.get(f'sitter:{sitter_id}')
            sitter = Sitter.load_from_dict(sitter_dict)


        if collection_name == 'housekeepers':
            sitter_dict = self.repo.get(f'housekeeper:{housekeeper_id}')
            sitter = Housekeeper.load_from_dict(sitter_dict)


        if collection_name == 'academic_sitters':
            sitter_dict = self.repo.get(f'academic:{academic_id}')
            sitter = AcademicSitter.load_from_dict(sitter_dict)

        return sitter

    def find_sitters(self, collection_name: str, filter) -> list[Sitter]:
        out = []

        for sitter_dict in seld.repo.find_by('sitter', predicate):
            out.append(Sitter.load_from_dict(sitter_dict))

        return out

    def find_all_sitters(self, collection_name: str) -> list[Sitter]:
        out = []

        for sitter_dict in self.repo.find_all('sitter:*'):
            out.append(Sitter.load_from_dict(sitter_dict))

        return out
