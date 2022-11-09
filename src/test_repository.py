import unittest
from Repository import Repository
from Child import Child

class RepositoryTest(unittest.TestCase):
    collection_name = 'test_children'
    
    def test_repo(self):
        repo = Repository()

        # adding an object to repo
        current_count = len(repo.find_all(self.collection_name))

        child = Child('Jonathan', 5)
        repo.add(self.collection_name, child.as_dict())

        self.assertEqual(len(repo.find_all(self.collection_name)), current_count + 1)

        # ensure id values of object and database document are the same
        self.assertEqual(child._id.__str__(), repo.find_by(self.collection_name, { 'name': 'Jonathan' })[-1]['_id'])

        # removing from repo
        current_count = len(repo.find_all(self.collection_name))
        
        repo.remove(self.collection_name, child.as_dict())

        self.assertEqual(len(repo.find_all(self.collection_name)), current_count - 1)

if __name__ == '__main__':
    unittest.main()