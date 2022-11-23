from Sitter import Sitter

class AcademicSitter(Sitter):
    """Opiekunka akademicka posiada zdolnosc do nauczania dziecka"""

    _id: int
    sitter_id: int
    bonus: float
    max_age: int

    def __init__(
        self,
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

        self.bonus = bonus
        self.max_age = max_age

        super().__init__(first_name, last_name, base_price)
        self.sitter_id = super()._id
        self._id = int

    def get_actual_price(self) -> float:
        return self.base_price * self.bonus

    def get_sitter_info(self) -> str:
        out = f'ID opiekunki: {self.id}\n'
        out += f'Opiekunka {self.first_name} {self.last_name}\n'
        out += f'Typ opiekunki: Academic\n'
        out += f'Cena podstawowa: {self.base_price}\n'
        out += f'Mnoznik bonusu: {self.bonus}\n'
        out += f'Maksymalny wiek dziecka do nauczania: {self.max_age}\n'

        return out

    def get_max_age(self) -> int:
        return self.max_age

    def as_dict(self) -> dict:
        sitter = super().as_dict()

        return {
            '_id': self._id,
            'bonus': self.bonus,
            'max_age': self.max_age,
            'sitter_id': self.sitter_id,
            'type': 'academic'
        }

    @staticmethod
    def load_from_dict(academic: dict) -> object:
        a = AcademicSitter(academic['first_name'], academic['last_name'], academic['base_price'], academic['bonus'], academic['max_age'])
        a._id = academic['_id']
        a.sitter_id = academic['sitter']['_id']

        return a
