from Base import Base

from sqlalchemy import Column, Integer, String

class Child(Base):
    """Dziecko, dla którego będzie wynajmowana opiekunka"""

    __tablename__ = 'children'
    child_id = Column(Integer, autoincrement=True, primary_key=True)
    child_name = Column(String(50), nullable=False)
    child_age = Column(Integer, nullable=False)

    def __init__(self, name: str, age: int):
        if not name or not name.strip():
            raise ValueError("Wprowadz poprawne imie dziecka!")

        if age < 0:
            raise ValueError("Wprowadz poprawny wiek dziecka!")

        self.child_age = age
        self.child_name = name

    def get_child_info(self) -> str:
        out = ''
        out += f'Imie dziecka: {self.child_name}\n'
        out += f'Wiek dziecka: {self.child_age}'

        if self.child_age == 1:
            out += ' rok\n'
        elif self.child_age in [2, 3, 4]:
            out += ' lata\n'
        else:
            out += ' lat\n'

        return out
