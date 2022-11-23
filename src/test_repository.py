import unittest
from Repository import Repository
from Child import Child
from DatabaseClient import DatabaseError

class RepositoryTest(unittest.TestCase):
    repo = Repository()

    def test_repo_set(self):
        # set id
        self.assertEqual(None, self.repo.add('test_child_id', 15, overwrite=True))

        with self.assertRaises(DatabaseError): self.repo.add('test_child_id', 10)

        self.assertEqual(None, self.repo.add('test_child_id', 16, overwrite=True))

        # set object
        tc = Child(1, 'name', 12)
        self.assertEqual(None, self.repo.add(f'test_child:{tc._id}', tc.as_dict(), overwrite=True))

        # try to add another object with already used id
        tc2 = Child(1, 'testkid', 15544)
        with self.assertRaises(DatabaseError):
            self.repo.add(f'test_child:{tc2._id}', tc2.as_dict())

        # allow to add another object with overwrite flag
        self.assertEqual(None, self.repo.add(f'test_child:{tc2._id}', tc2.as_dict(), overwrite=True))

    def test_repo_remove(self):
        tc = Child(420, 'Jerzy', 47)
        self.repo.add(f'test_child:{tc._id}', tc.as_dict())

        # make sure 1 entry was deleted
        self.assertEqual(1, self.repo.remove('test_child:420'))

    def test_repo_get(self):
        tc = Child(421, 'Jezus', 2022)
        self.repo.add(f'test_child:{tc._id}', tc.as_dict(), overwrite=True)

        tc_from_db = self.repo.get('test_child:421')

        self.assertEqual(tc_from_db['_id'], tc._id)
        self.assertEqual(tc_from_db['name'], tc.name)
        self.assertEqual(tc_from_db, tc.as_dict())

    def test_repo_find_all(self):
        tc1 = Child(422, 'dzieciak1', 10)
        tc2 = Child(423, 'dzieciak2', 12)

        self.repo.add(f'test_child:{tc1._id}', tc1.as_dict(), overwrite=True)
        self.repo.add(f'test_child:{tc2._id}', tc2.as_dict(), overwrite=True)

        out = self.repo.find_all('test_child:*')
        self.assertTrue(len(out) >= 2)
        self.assertTrue(tc1.as_dict() in out)
        self.assertTrue(tc2.as_dict() in out)

        for child in out:
            _id = child["_id"]
            self.repo.remove(f'test_child:{_id}')

        out = self.repo.find_all('test_child:*')
        self.assertTrue(len(out) == 0)

    def test_repo_find_by(self):
        tc1 = Child(422, 'dzieciak1', 10)
        tc2 = Child(423, 'dzieciak2', 12)

        self.repo.add(f'test_child:{tc1._id}', tc1.as_dict(), overwrite=True)
        self.repo.add(f'test_child:{tc2._id}', tc2.as_dict(), overwrite=True)

        out = self.repo.find_by('test_child:*', { 'age': 12 })
        self.assertTrue(tc2.as_dict() in out)
        self.assertFalse(tc1.as_dict() in out)

        
if __name__ == '__main__':
    unittest.main()