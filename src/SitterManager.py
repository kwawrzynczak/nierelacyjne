from Sitter import Sitter
from Housekeeper import Housekeeper
from AcademicSitter import AcademicSitter
from Repository import Repository

from uuid import UUID

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
            sitter = Sitter(first_name, last_name, base_price)
        
        if collection_name == 'housekeepers':
            sitter = Housekeeper(first_name, last_name, base_price)
        
        if collection_name == 'academic_sitters':
            sitter = AcademicSitter(first_name, last_name, base_price, bonus, max_age)

        self.repo.add(collection_name, sitter.as_dict())
        return sitter

    def get_sitter(self, collection_name: str, sitter_id: str) -> Sitter:
        sitter_dict = self.repo.get(collection_name, sitter_id)

        if collection_name == 'sitters':
            sitter = Sitter.load_from_dict(sitter_dict)

        if collection_name == 'housekeepers':
            sitter = Housekeeper.load_from_dict(sitter_dict)

        if collection_name == 'academic_sitters':
            sitter = AcademicSitter.load_from_dict(sitter_dict)

        return sitter

    def find_sitters(self, collection_name: str, filter) -> list[Sitter]:
        out = []

        sitters_dict = self.repo.find_by(collection_name, filter)
        for sitter_dict in sitters_dict:
            if collection_name == 'sitters':
                sitter = Sitter.load_from_dict(sitter_dict)

            if collection_name == 'housekeepers':
                sitter = Housekeeper.load_from_dict(sitter_dict)

            if collection_name == 'academic_sitters':
                sitter = AcademicSitter.load_from_dict(sitter_dict)

            out.append(sitter)

        return out

    def find_all_sitters(self, collection_name: str) -> list[Sitter]:
        out = [] 

        sitters_dict = self.repo.find_all(collection_name)
        for sitter_dict in sitters_dict:
            if collection_name == 'sitters':
                sitter = Sitter.load_from_dict(sitter_dict)

            if collection_name == 'housekeepers':
                sitter = Housekeeper.load_from_dict(sitter_dict)

            if collection_name == 'academic_sitters':
                sitter = AcademicSitter.load_from_dict(sitter_dict)

            out.append(sitter)

        return out
