from uuid import uuid4, UUID

class Child():
    """Dziecko, dla którego będzie wynajmowana opiekunka"""

    _id: UUID
    name: str
    age: int

    def __init__(self, name: str, age: int):
        if not name or not name.strip():
            raise ValueError("Wprowadz poprawne imie dziecka!")

        if age < 0:
            raise ValueError("Wprowadz poprawny wiek dziecka!")

        self.age = age
        self.name = name

        self._id = uuid4()

    def get_child_info(self) -> str:
        out = ''
        out += f'Imie dziecka: {self.name}\n'
        out += f'Wiek dziecka: {self.age}'

        if self.age == 1:
            out += ' rok\n'
        elif self.age in [2, 3, 4]:
            out += ' lata\n'
        else:
            out += ' lat\n'

        return out

    def as_dict(self) -> dict:
        return {
            '_id': self._id.__str__(),
            'name': self.name,
            'age': self.age,
        }

    @staticmethod
    def load_from_dict(child: dict) -> object:
        c = Child(child['name'], child['age'])
        c._id = child['_id']

        return c
