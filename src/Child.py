
class Child():
    """Dziecko, dla którego będzie wynajmowana opiekunka"""

    _id: int
    name: str
    age: int

    def __init__(self, _id: int, name: str, age: int):
        if not name or not name.strip():
            raise ValueError("Wprowadz poprawne imie dziecka!")

        if age < 0:
            raise ValueError("Wprowadz poprawny wiek dziecka!")

        self._id = _id
        self.age = age
        self.name = name

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
            '_id': self._id,
            'name': self.name,
            'age': self.age,
        }

    @staticmethod
    def load_from_dict(child: dict) -> object:
        return Child(child['_id'], child['name'], child['age'])
