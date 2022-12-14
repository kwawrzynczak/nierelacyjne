from unittest import TestCase
from DatabaseClient import DatabaseClient
from Child import Child

class DatabaseTest(TestCase):
    collection_name = 'test_children'
    
    def test_db(self):
        dc = DatabaseClient()

        # adding an object to db
        current_count = len(dc.find_all(self.collection_name))

        child = Child('Jonathan', 5)
        dc.add(self.collection_name, child.as_dict())

        self.assertEqual(len(dc.find_all(self.collection_name)), current_count + 1)

        # ensure id values of object and database document are the same
        self.assertEqual(child._id.__str__(), dc.find_by(self.collection_name, { 'name': 'Jonathan' })[-1]['_id'])

        # removing fromdc 
        current_count = len(dc.find_all(self.collection_name))
        
        dc.remove(self.collection_name, child.as_dict())

        self.assertEqual(len(dc.find_all(self.collection_name)), current_count - 1)
