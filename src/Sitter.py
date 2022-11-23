from uuid import UUID, uuid4

class Sitter():
    """Bazowa klasa opiekunki dla dzieci"""

    _id: UUID
    first_name: str 
    last_name: str 
    base_price: float 
    is_available: bool 

    def __init__(
        self, 
        first_name: str, 
        last_name: str,
        base_price: float
    ):
        if not first_name or not first_name.split():
            raise ValueError("Wprowadz poprawne imie opiekunki!")

        if not last_name or not last_name.split():
            raise ValueError("Wprowadz poprawne nazwisko opiekunki!")

        if base_price <= 0:
            raise ValueError("Cena podstawowa powinna byc wieksza od zera.")

        self.first_name = first_name
        self.last_name = last_name
        self.base_price = base_price
        self.is_available = True
        self._id = uuid4()

    def get_actual_price(self) -> float:
        return self.base_price

    def set_available(self, is_available: bool):
        self.is_available = is_available

    def as_dict(self) -> dict:
        return {
            '_id': self._id.__str__(),
            'first_name': self.first_name,
            'last_name': self.last_name,
            'base_price': self.base_price,
            'is_available': self.is_available,
            'type': 'sitter',
        }

    @staticmethod
    def load_from_dict(sitter: dict) -> object:
        s = Sitter(sitter['first_name'], sitter['last_name'], sitter['base_price'])
        s._id = sitter['_id']

        return s
        