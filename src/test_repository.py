import unittest
from Repository import Repository
from DatabaseSession import DatabaseSession
from Child import Child

class RepositoryTest(unittest.TestCase):
    
    def test_repo(self):
        repo = Repository()
        ds = DatabaseSession()

        # adding an object to repo
        s = ds.create_new_session()
        n_rows = s.query(Child.id).count()

        child = Child('Jonathan', 5)
        repo.add(child)

        self.assertTrue(s.query(Child.id).count() == n_rows + 1)

        # removing from repo
        n_rows = s.query(Child.id).count()

        repo.remove(child)
        self.assertTrue(s.query(Child.id).count() == n_rows - 1)

if __name__ == '__main__':
    unittest.main()