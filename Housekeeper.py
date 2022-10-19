from Sitter import Sitter

class Housekeeper(Sitter):
    """Klasa pomocy domowej"""

    def __init__(self, first_name: str, last_name: str, base_price: float):
        super().__init__(first_name, last_name, base_price)

    def get_actual_price(self) -> float: 
        return self.base_price

    def get_sitter_info(self) -> str: 
        out = f'ID opiekunki: {self.id}\n'
        out += f'Opiekunka {self.first_name} {self.last_name}\n'
        out += 'Pomoc domowa\n'
        out += f'Cena podstawowa: {self.base_price}\n'

        return out

    def get_max_age(self) -> int:
        return 0
