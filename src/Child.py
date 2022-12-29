from DatabaseObject import DatabaseObject

from uuid import uuid4

class Child(DatabaseObject):
    """Dziecko, dla którego będzie wynajmowana opiekunka"""

    table_name = 'children'

    def add_to_database(self) -> str:
        return f"""
        INSERT INTO {self.table_name}(c_id, c_name, c_age)
        VALUES ({self.c_id}, '{self.c_name}', {self.c_age});
        """

    def delete_from_database(self) -> str:
        return f"""
        DELETE FROM {self.table_name}
        WHERE c_id = {self.c_id};
        """

    def update_data(self) -> str:
        return f"""
        UPDATE {self.table_name}
        SET 
            c_name = '{self.c_name}',
            c_age = {self.c_age}
        WHERE c_id = {self.c_id};
        """

    def __init__(self, name: str, age: int):
        if not name or not name.strip():
            raise ValueError("Wprowadz poprawne imie dziecka!")

        if age < 0:
            raise ValueError("Wprowadz poprawny wiek dziecka!")

        self.c_id = uuid4()
        self.c_name = name
        self.c_age = age

    def get_child_info(self) -> str:
        out = ''
        out += f'Imie dziecka: {self.c_name}\n'
        out += f'Wiek dziecka: {self.c_age}'

        if self.c_age == 1:
            out += ' rok\n'
        elif self.c_age in [2, 3, 4]:
            out += ' lata\n'
        else:
            out += ' lat\n'

        return out
