from Child import Child
from Repository import Repository

class Parent():
    """Klasa rodzica odpowiedzialna za wynajmowanie opiekunki dla dziecka"""

    _id: int 
    child_id: int 
    name: str 
    address: str
    phone_number: str
    is_teaching_required: bool 

    def __init__(
        self, 
        _id: int,
        name: str, 
        address: str, 
        phone_number: str, 
        is_teaching_required: bool,
        child: Child
    ):
        if not name or not name.split():
            raise ValueError("Wprowadz poprawne imie rodzica!")

        if len(phone_number) < 9:
            raise ValueError("Wprowadz poprawny numer telefonu!")

        if not address or not address.split():
            raise ValueError("Wprowadz poprawny adres!")

        if child is None:
            raise ValueError("Podane dziecko nie istnieje!")

        self._id = _id
        self.child_id = child._id
        self.name = name 
        self.address = address
        self.phone_number = phone_number
        self.is_teaching_required = is_teaching_required
        self.child = child

    def get_parent_info(self) -> str:
        out = f'Imie: {self.name}\n'
        out += f'Imie dziecka: {self.child.name}\n'
        out += f'Adres zamieszkania: {self.address}\n'
        out += f'Numer telefonu: {self.phone_number}\n'
        out += f'UWAGI: Wymagana pomoc w nauce\n' if self.is_teaching_required else ''

        return out

    def get_child_info(self) -> str:
        out = f'Imie rodzica: {self.name}\n'
        out += self.child.get_child_info()

        return out

    def as_dict(self) -> dict:
        return {
            '_id': self._id,
            'child_id': self.child._id,
            'name': self.name,
            'address': self.address,
            'phone_number': self.phone_number,
            'is_teaching_required': self.is_teaching_required,
        }

    @staticmethod
    def load_from_dict(parent: dict, child: dict) -> object:
        return Parent(
            parent['_id'], 
            parent['name'], 
            parent['address'], 
            parent['phone_number'], 
            parent['is_teaching_required'], 
            Child.load_from_dict(child),
        )
