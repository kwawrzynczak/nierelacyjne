
class Sitter():
    """Bazowa klasa opiekunki dla dzieci"""

    sitter_id: int
    first_name: str
    last_name: str 
    base_price: float 
    is_available: bool 

    def __init__(
        self, 
        sitter_id: int, 
        first_name: str, 
        last_name: str,
        base_price: float
    ):
        if not first_name or not first_name.split():
            raise ValueError("Wprowadz poprawne imie opiekunki!")

        if not last_name or not last_name.split():
            raise ValueError("Wprowadz poprawne nazwisko opiekunki!")

        if base_price <= 0:
            raise ValueError("Cena podstawowa powinna byc wieksza od zera.")

        self.sitter_id = sitter_id
        self.first_name = first_name
        self.last_name = last_name
        self.base_price = base_price

    def set_available(self, is_available: bool):
        self.is_available = is_available
        