from Child import Child

from uuid import uuid4, UUID

class Parent():
    """Klasa rodzica odpowiedzialna za wynajmowanie opiekunki dla dziecka"""

    _id: UUID
    child_id: UUID
    name: str 
    address: str
    phone_number: str
    is_teaching_required: bool 

    def __init__(
        self, 
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
            raise ValueError("Obiekt dziecka nie istnieje!")

        self.name = name 
        self.address = address
        self.phone_number = phone_number
        self.is_teaching_required = is_teaching_required
        self.child = child

        self._id = uuid4()
        self.child_id = self.child._id

    def get_parent_info(self) -> str:
        out = f'Imie: {self.name}\n'
        out += f'Imie dziecka: {self.child.child_name}\n'
        out += f'Adres zamieszkania: {self.address}\n'
        out += f'Numer telefonu: {self.phone_number}\n'
        out += f'UWAGI: Wymagana pomoc w nauce\n' if self.is_teaching_required else ''

        return out

    def get_child_info(self) -> str:
        out = f'Imie rodzica: {self.name}\n'
        out += self.child.get_child_info()

        return out

    def as_dict(self) -> dict:
        child = self.child.as_dict()

        return {
            '_id': self._id.__str__(),
            'name': self.name,
            'address': self.address,
            'phone_number': self.phone_number,
            'is_teaching_required': self.is_teaching_required,
            'child': child,
        }
