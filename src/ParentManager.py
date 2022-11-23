from Repository import Repository
from Child import Child
from Parent import Parent
from DatabaseClient import DatabaseError

class ParentManager():
    def __init__(self):
        self.repo = Repository()

    def create_parent(
            self,
            parent_name: str,
            address: str,
            phone_number: str,
            is_teaching_required: bool,
            child_name: str,
            child_age: int,
    ) -> Parent:

        # dodaj dziecko
        try:
            cid = int(self.repo.get('child_id'))
            new_child_id = cid + 1
        except DatabaseError:
            new_child_id = 1

        child = Child(new_child_id, child_name, child_age)
        self.repo.add(f'child:{new_child_id}', child.as_dict())
        self.repo.add('child_id', new_child_id)

        # obecnie najwieksze uzywane id rodzica
        try:
            pid = int(self.repo.get('parent_id'))
            new_parent_id = pid + 1
        except DatabaseError: # parent_id doesnt exist yet
            new_parent_id = 1

        parent = Parent(new_parent_id, parent_name, address, phone_number, is_teaching_required, child)

        # dodanie do bazy danych
        self.repo.add(f'parent:{new_parent_id}', parent.as_dict())

        # update parent_id
        self.repo.add('parent_id', new_parent_id, overwrite=True)

        return parent

    def remove_parent(self, parent: Parent) -> bool:
        # zwraca prawde jezeli uda sie usunac obiekt z bazy danych
        return True if self.repo.remove(f'parent:{parent._id}') == 1 else False

    def get_parent(self, parent_id: int) -> Parent:
        parent_dict = self.repo.get(f'parent:{parent_id}')
        child_dict = self.repo.get(f'child:{parent_dict["child_id"]}')

        return Parent.load_from_dict(parent_dict, child_dict)

    def find_parents(self, predicate: dict) -> list[Parent]:
        out = []

        for parent_dict in self.repo.find_by('parent:*', predicate):
            child_dict = self.repo.get(f'child:{parent_dict["child_id"]}')
            out.append(Parent.load_from_dict(parent_dict, child_dict))

        return out

    def find_all_parents(self) -> list[Parent]:
        out = []
        
        for parent_dict in self.repo.find_all('parent:*'):
            child_dict = self.repo.get(f'child:{parent_dict["child_id"]}')
            out.append(Parent.load_from_dict(parent_dict, child_dict))

        return out
