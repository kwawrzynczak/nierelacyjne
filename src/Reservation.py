from Sitter import Sitter
from Parent import Parent
from Base import Base

from Sitter import Sitter
from Housekeeper import Housekeeper
from AcademicSitter import AcademicSitter
from Parent import Parent
from DatabaseObject import DatabaseObject

from uuid import uuid4
from collections import namedtuple

class Reservation(DatabaseObject):
    """Kumuluje wszystkie dane potrzebne do utworzenia rezerwacji"""

    table_name = 'reservations'

    @staticmethod
    def create_from_row(db_row: namedtuple) -> object:
        match db_row.s_sitter_type:
            case 'sitter':      s = Sitter.create_from_row(db_row)
            case 'housekeeper': s = Housekeeper.create_from_row(db_row)
            case 'academic':    s = AcademicSitter.create_from_row(db_row)
            
        r = Reservation(db_row.r_date, db_row.r_start_hour, db_row.r_end_hour, s, Parent.create_from_row(db_row), db_row.p_teaching_required)
        r.r_id = db_row.r_id
        return r

    def add_to_database(self) -> str:
        return f"""
        INSERT INTO {self.table_name}(r_id, r_date, r_start_hour, r_end_hour,
            s_id, s_sitter_type, s_first_name, s_last_name, s_base_price, s_is_available, as_bonus, as_max_age,
            p_id, p_name, p_address, p_phone_number, p_teaching_required,
            c_id, c_name, c_age)
        VALUES({self.r_id}, '{self.r_date}', {self.r_start_hour}, {self.r_end_hour},
            {self.r_sitter.s_id}, '{self.r_sitter.sitter_type}', '{self.r_sitter.s_first_name}', '{self.r_sitter.s_last_name}', {self.r_sitter.s_base_price}, {self.r_sitter.s_is_available}, {self.r_sitter.as_bonus}, {self.r_sitter.as_max_age},
            {self.r_parent.p_id}, '{self.r_parent.p_name}', '{self.r_parent.p_address}', '{self.r_parent.p_phone_number}', {self.r_parent.p_teaching_required},
            {self.r_parent.p_child.c_id}, '{self.r_parent.p_child.c_name}', {self.r_parent.p_child.c_age});
        """

    def delete_from_database(self) -> str:
        return f"""
        DELETE FROM {self.table_name}
        WHERE r_id = {self.r_id};
        """

    def update_data(self) -> str:
        return f"""
        UPDATE {self.table_name}
        SET
            r_date = '{self.r_date}',
            r_start_hour = {self.r_start_hour},
            r_end_hour = {self.r_end_hour},
        WHERE r_id = {self.r_id};
        """

    def __init__(
        self, 
        date: str, 
        start_hour: int, 
        end_hour: int,
        sitter: Sitter,
        parent: Parent,
        can_teach: bool
    ):
        # dopuszczalny zakres [1, 24] 24 -> polnoc
        if start_hour <= 0 or start_hour > 24:
            raise ValueError("Podana godzina rozpoczecia rezerwacji jest nieprawidlowa!")

        if end_hour <= 0 or end_hour > 24:
            raise ValueError("Podana godzina zakonczenia rezerwacji jest nieprawidlowa!")

        if sitter is None:
            raise ValueError("Obiekt opiekunki jest nieprawidlowy!")

        if parent is None:
            raise ValueError("Obiekt rodzica jest nieprawidlowy!")

        self.date = date
        self.start_hour = start_hour
        self.end_hour = end_hour
        self.sitter = sitter
        self.parent = parent
        self.can_teach = can_teach

    def get_reservation_time(self) -> int:
        return self.end_hour - self.start_hour

    def get_reservation_info(self) -> str:
        out = f'ID rezerwacji: {self.id}\n'
        out += f'ID rodzica: {self.parent_id}\n'
        out += f'ID opiekunki: {self.sitter_id}\n'
        out += f'Data rezerwacji: {self.date}\n'
        out += f'Rezerwacja od {self.start_hour} do {self.end_hour}\n'
        out += f'Koszt rezerwacji: {self.get_reservation_cost()}\n'

        return out

    def get_reservation_cost(self) -> float:
        return self.sitter.get_actual_price() * self.get_reservation_time()

    def set_sitter(self, new_sitter: Sitter):
        if new_sitter is None:
            raise ValueError("Obiekt nowej opiekunki nie istnieje!")

        self.sitter = new_sitter
