from Sitter import Sitter
from Housekeeper import Housekeeper
from AcademicSitter import AcademicSitter
from Repository import Repository

class SitterManager():
    
    def __init__(self):
        self.repo = Repository()

    def create_sitter(
        self,
        sitter_type: type,
        first_name: str,
        last_name: str, 
        base_price: float,
        bonus: float = 1,
        max_age: int = 0
    ) -> bool:
        if sitter_type == Sitter:
            sitter = Sitter(first_name, last_name, base_price)
        
        elif sitter_type == Housekeeper:
            sitter = Housekeeper(first_name, last_name, base_price)
        
        elif sitter_type == AcademicSitter:
            sitter = AcademicSitter(first_name, last_name, base_price, bonus, max_age)

        else: return False

        self.repo.add(sitter)
        return True

    def get_sitter(self, sitter_id: int) -> Sitter: 
        return self.repo.get(Sitter, sitter_id)

    def find_sitters(self, predicate) -> list[Sitter]:
        return self.repo.find_by(Sitter, predicate)

    def find_all_sitters(self) -> list[Sitter]:
        return self.repo.find_all(Sitter)