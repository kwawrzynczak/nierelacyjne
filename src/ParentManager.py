from Repository import Repository
from Child import Child
from Parent import Parent

from uuid import UUID

class ParentManager():
    collection_name = 'parents'

    def __init__(self):
        self.repo = Repository()

    def create_parent(
            self,
            parent_name: str,
            address: str,
            phone_number: str,
            is_teaching_required: bool,
            child: Child
    ) -> Parent:

        parent = Parent(parent_name, address, phone_number, is_teaching_required, child)
        self.repo.add(self.collection_name, parent.as_dict())
        return parent

    def get_parent(self, parent_id: str) -> Parent:
        parent_dict = self.repo.get(self.collection_name, parent_id)
        return Parent.load_from_dict(parent_dict)

    def find_parents(self, filter) -> list[Parent]:
        out = []

        parents_dict = self.repo.find_by(self.collection_name, filter)
        for parent in parents_dict:
            out.append(Parent.load_from_dict(parent))

        return out

    def find_all_parents(self) -> list[Parent]:
        out = []

        parents_dict = self.repo.find_all(self.collection_name)
        for parent in parents_dict:
            out.append(Parent.load_from_dict(parent))

        return out
