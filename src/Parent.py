from DatabaseObject import DatabaseObject
from Child import Child

from uuid import uuid4
from collections import namedtuple


class Parent(DatabaseObject):
    """Klasa rodzica odpowiedzialna za wynajmowanie opiekunki dla dziecka"""

    table_name = 'parents'

    @staticmethod
    def create_from_row(db_row: namedtuple) -> object:
        p = Parent(db_row.p_name, db_row.p_address, db_row.p_phone_number,
                   db_row.p_teaching_required, Child.create_from_row(db_row))
        p.p_id = db_row.p_id
        return p

    def add_to_database(self) -> str:
        return f"""
        INSERT INTO {self.table_name}(p_id, p_name, p_address, p_phone_number, p_teaching_required, c_id, c_name, c_age)
        VALUES({self.p_id}, '{self.p_name}', '{self.p_address}', '{self.p_phone_number}', {self.p_teaching_required}, {self.p_child.c_id}, '{self.p_child.c_name}', {self.p_child.c_age});
        """

    def delete_from_database(self) -> str:
        return f"""
        DELETE FROM {self.table_name}
        WHERE p_id = {self.p_id};
        """

    def update_data(self) -> str:
        return f"""
        UPDATE {self.table_name}
        SET
            p_name = '{self.p_name}',
            p_address = '{self.p_address}',
            p_phone_number = '{self.p_phone_number}',
            p_teaching_required = {self.p_teaching_required}
        WHERE p_id = {self.p_id};
        """

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

        # if len(phone_number) < 9:
        #     raise ValueError("Wprowadz poprawny numer telefonu!")

        if not address or not address.split():
            raise ValueError("Wprowadz poprawny adres!")

        if child is None:
            raise ValueError("Obiekt dziecka nie istnieje!")

        self.p_id = uuid4()
        self.p_name = parent_name
        self.p_address = address
        self.p_phone_number = phone_number
        self.p_teaching_required = is_teaching_required
        self.p_child = child

    def get_parent_info(self) -> str:
        out = f'Imie: {self.p_name}\n'
        out += f'Imie dziecka: {self.p_child.c_name}\n'
        out += f'Adres zamieszkania: {self.p_address}\n'
        out += f'Numer telefonu: {self.p_phone_number}\n'
        out += f'UWAGI: Wymagana pomoc w nauce\n' if self.p_teaching_required else ''

        return out

    def get_child_info(self) -> str:
        out = f'Imie rodzica: {self.p_name}\n'
        out += self.p_child.get_child_info()

        return out
