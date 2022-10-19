from DatabaseSession import DatabaseSession
from Base import Base

class Repository():

    def __init__(self):
        self.ds = DatabaseSession()
        

    def add(self, obj: Base):
        db = self.ds.create_new_session()
        db.add(obj)
        db.commit()
        db.close()

    def remove(self, obj: Base):
        db = self.ds.create_new_session()
        db.delete(obj)
        db.commit()
        db.close()

    def get(self, class_type: type, id: int) -> Base:
        pass

    def find_all(self, class_type: type) -> list[Base]:
        pass

    def find_by(self, class_type: type, predicate) -> list[Base]:
        pass
    
