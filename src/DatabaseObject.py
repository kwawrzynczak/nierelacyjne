
class DatabaseObject():
    """reprezentuje interfejs obiektu, ktory mozna dodac do bazy danych"""

    table_name: str # nazwa tabeli w bazie danych dla danego obiektu

    def add_to_database(self) -> str:
        """zwraca zapytanie sql dodajace siebie do bazy danych"""
        pass

    def delete_from_database(self) -> str:
        """zwraca zapytanie sql usuwajace siebie z bazy danych"""
        pass

    def update_data(self) -> str:
        """zwraca zapytanie sql aktualizujace dane w bazie danych"""
        pass
