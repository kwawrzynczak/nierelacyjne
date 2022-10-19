from Child import Child
from Base import Base
from sqlalchemy import Column, Integer, String, Boolean, false, ForeignKey
from sqlalchemy.orm import relationship

class Parent(Base):
    """Klasa rodzica odpowiedzialna za wynajmowanie opiekunki dla dziecka"""

    __tablename__ = 'parents'
    parent_id = Column(Integer, autoincrement=True, primary_key=True) 
    parent_name = Column(String(50), nullable=False)
    address = Column(String(255), nullable=False)
    phone_number = Column(String(12), nullable=False)
    is_teaching_required = Column(Boolean, default=false)

    child_id = Column(Integer, ForeignKey(Child.child_id))
    child = relationship(Child)

    def __init__(
        self, 
        parent_name: str, 
        address: str, 
        phone_number: str, 
        is_teaching_required: bool,
        child: Child
    ):
        if not parent_name or not parent_name.split():
            raise ValueError("Wprowadz poprawne imie rodzica!")

        if len(phone_number) < 9:
            raise ValueError("Wprowadz poprawny numer telefonu!")

        if not address or not address.split():
            raise ValueError("Wprowadz poprawny adres!")

        if child is None:
            raise ValueError("Obiekt dziecka nie istnieje!")

        self.parent_name = parent_name
        self.address = address
        self.phone_number = phone_number
        self.is_teaching_required = is_teaching_required
        self.child = child

    def get_parent_info(self) -> str:
        out = f'Imie: {self.parent_name}\n'
        out += f'Imie dziecka: {self.child.child_name}\n'
        out += f'Adres zamieszkania: {self.address}\n'
        out += f'Numer telefonu: {self.phone_number}\n'
        out += f'UWAGI: Wymagana pomoc w nauce\n' if self.is_teaching_required else ''

        return out

    def get_child_info(self) -> str:
        out = f'Imie rodzica: {self.parent_name}\n'
        out += self.child.get_child_info()

        return out
