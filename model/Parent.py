from Child import Child

class Parent():
    """Klasa rodzica odpowiedzialna za wynajmowanie opiekunki dla dziecka"""

    parent_id: int 
    parent_name: str 
    address: str 
    phone_number: str 
    is_teaching_required: bool 
    child: Child 

    def __init__(
        self, 
        parent_id: int,
        parent_name: str, 
        address: str, 
        phone_number: str, 
        is_teaching_required: bool,
        child: Child
    ):
        if not parent_name or not parent_name.split():
            raise ValueError("Wprowadz poprawne imie rodzica!")

        if len(phone_number) != 9:
            raise ValueError("Wprowadz poprawny numer telefonu!")

        if not address or not address.split():
            raise ValueError("Wprowadz poprawny adres!")

        if child is None:
            raise ValueError("Obiekt dziecka nie istnieje!")

        self.parent_id = parent_id
        self.parent_name = parent_name
        self.address = address
        self.phone_number = phone_number
        self.is_teaching_required = is_teaching_required
        self.child = child

    def get_parent_info(self) -> str:
        out = ''
        out += f'ID rodzica: {self.parent_id}\n'
        out += f'Imie: {self.parent_name}\n'
        out += f'Imie dziecka: {self.child.child_name}\n'
        out += f'Adres zamieszkania: {self.address}\n'
        out += f'Numer telefonu: {self.phone_number}\n'
        out += f'UWAGI: Wymagana pomoc w nauce\n' if self.is_teaching_required else ''

        return out

    def get_child_info(self) -> str:
        out = f'ID rodzica: {self.parent_id}\n'
        out += self.child.get_child_info()

        return out
