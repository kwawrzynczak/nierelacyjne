from Child import Child
from Parent import Parent
from Repository import Repository

from uuid import UUID


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
    ) -> UUID:

        parent = Parent(parent_name, address, phone_number,
                        is_teaching_required, child)
        self.repo.add(parent)  # add parent + child to parents
        self.repo.add(child)  # add child to children

        return parent.p_id

    def get_parent(self, parent_id: UUID) -> Parent:
        parent_row = self.repo.get(parent_id, Parent.table_name)

        if parent_row is None:
            raise ValueError("No parent found  with this parent_id")

        return Parent.create_from_row(parent_row)

    def find_parents(self, where_sql_clause: str) -> list[Parent]:
        found = self.repo.find_by(Parent.table_name, where_sql_clause)
        return [Parent.create_from_row(parent_row) for parent_row in found]

    def find_all_parents(self) -> list[Parent]:
        found = self.repo.find_all(Parent.table_name)
        return [Parent.create_from_row(parent_row) for parent_row in found]
