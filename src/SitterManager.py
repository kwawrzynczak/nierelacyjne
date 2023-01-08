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
        sitter_type: str,
        first_name: str,
        last_name: str, 
        base_price: float,
        bonus: float = 1,
        max_age: int = 0
    ) -> UUID:
        if sitter_type == 'sitter':
            sitter = Sitter(first_name, last_name, base_price)
        
        elif sitter_type == 'housekeeper':
            sitter = Housekeeper(first_name, last_name, base_price)
        
        elif sitter_type == 'academic':
            sitter = AcademicSitter(first_name, last_name, base_price, bonus, max_age)

        else: 
            return None

        self.repo.add(sitter)
        return sitter.s_id

    def get_sitter(self, sitter_id: UUID) -> Sitter: 
        sitter_row = self.repo.get(sitter_id, Sitter.table_name)

        if sitter_row is None:
            raise ValueError("No sitter found with this sitter_id")

        match sitter_row.s_sitter_type:
            case 'sitter':
                return Sitter.create_from_row(sitter_row)
            case 'housekeeper':
                return Housekeeper.create_from_row(sitter_row)
            case 'academic':
                return AcademicSitter.create_from_row(sitter_row)
        
    def find_sitters(self, where_sql_clause: str) -> list[Sitter]:
        found = self.repo.find_by(Sitter.table_name, where_sql_clause)

        out = []
        for sitter_row in found:
            match sitter_row.s_sitter_type:
                case 'sitter':
                    out.append(Sitter.create_from_row(sitter_row))
                case 'housekeeper':
                    out.append(Housekeeper.create_from_row(sitter_row))
                case 'academic':
                    out.append(AcademicSitter.create_from_row(sitter_row))

        return out

    def find_all_sitters(self) -> list[Sitter]:
        found = self.repo.find_all(Sitter.table_name)

        out = []
        for sitter_row in found:
            match sitter_row.s_sitter_type:
                case 'sitter':
                    out.append(Sitter.create_from_row(sitter_row))
                case 'housekeeper':
                    out.append(Housekeeper.create_from_row(sitter_row))
                case 'academic':
                    out.append(AcademicSitter.create_from_row(sitter_row))

        return out