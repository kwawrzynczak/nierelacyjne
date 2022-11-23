from Sitter import Sitter

class Housekeeper(Sitter):
    """Klasa pomocy domowej"""

    _id: int
    sitter_id: int

    def __init__(self, first_name: str, last_name: str, base_price: float):
        super().__init__(first_name, last_name, base_price)
        self.sitter_id = super()._id
        self._id = int

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

    def as_dict(self) -> dict:
        sitter = super().as_dict()

        return {
            '_id': self._id,
            'sitter': sitter,
            'type': 'housekeeper',
        }

    @staticmethod
    def load_from_dict(housekeeper: dict) -> object:
        h = Housekeeper(housekeeper['first_name'], housekeeper['last_name'], housekeeper['base_price'])
        h._id = housekeeper['_id']
        h.sitter_id = housekeeper['sitter']['_id']

        return h