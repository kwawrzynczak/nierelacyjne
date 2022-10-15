from Sitter import Sitter

class AcademicSitter(Sitter):
    """Opiekunka akademicka posiada zdolnosc do nauczania dziecka"""

    bonus: float 
    max_age: int 

    def __init__(
        self, 
        sitter_id: int, 
        first_name: str, 
        last_name: str, 
        base_price: float,
        bonus: float,
        max_age: int
    ):
        if bonus <= 1:
            raise ValueError("Mnoznik bonusu musi byc wiekszy od 1.") 

        if max_age < 1:
            raise ValueError("Maksymalny wiek dziecka nieprawidlowy!")
        
        super().__init__(sitter_id, first_name, last_name, base_price)
        self.bonus = bonus
        self.max_age = max_age

    def get_actual_price(self) -> float:
        self.base_price * self.bonus

    def get_sitter_info(self) -> str:
        out = f'ID opiekunki: {self.sitter_id}\n'
        out += f'Opiekunka {self.first_name} {self.last_name}\n'
        out += f'Typ opiekunki: Academic\n'
        out += f'Cena podstawowa: {self.base_price}\n'
        out += f'Mnoznik bonusu: {self.bonus}\n'
        out += f'Maksymalny wiek dziecka do nauczania: {self.max_age}\n'
        
        return out

    def get_max_age(self) -> int:
        return self.max_age
