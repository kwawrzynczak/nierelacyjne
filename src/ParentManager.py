# from Repository import Repository

from src.model.Child import Child


class ParentManager():
    def __init__(self):
        self.repo = Repository()

    def create_parent(
            self,
            parent_name: str,
            address: str,
            phone_number: str,
            is_teaching_required: bool,
            child: Child
    ):

        parent = Parent(parent_name, address, phone_number, is_teaching_required, child)
        self.repo.add(parent)
        return True

    def get_parent(self, parent_id: int) -> Parent:
        return self.repo.get(Parent, parent_id)

    def find_parents(self, predicate) -> list[Parent]:
        return self.repo.find_by(Parent, predicate)

    def get_all_parents(self) -> list[Parent]:
        return self.repo.find_all(Parent)
