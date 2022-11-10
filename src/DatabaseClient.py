from pymongo import MongoClient

class DatabaseClient():
    """Klient bazy danych"""

    def __init__(self):
        client = MongoClient(connection_string)

        # dostep do bazy dantch o nazwie 'nierelacyjne'
        self.db = client['nierelacyjne']
