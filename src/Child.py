from dataclasses import dataclass, field
from uuid import uuid4, UUID

@dataclass
class Child():
    """Dziecko, dla którego będzie wynajmowana opiekunka"""

    child_name: str
    child_age: int
    _id: UUID

    def __init__(self, name: str, age: int):
        if not name or not name.strip():
            raise ValueError("Wprowadz poprawne imie dziecka!")

        if age < 0:
            raise ValueError("Wprowadz poprawny wiek dziecka!")

        self.child_age = age
        self.child_name = name
        self._id = uuid4()

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
