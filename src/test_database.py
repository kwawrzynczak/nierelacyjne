import unittest

from DatabaseSession import DatabaseSession
from Child import Child

class TestChild(Child):
    table_name = 'test_children'

class DatabaseTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        cls.ds = DatabaseSession()
        cls.ds.session.execute(
            """
            CREATE TABLE IF NOT EXISTS test_children(
                c_id UUID PRIMARY KEY,
                c_name TEXT,
                c_age INT
            );
            """
        )

    @classmethod
    def tearDownClass(cls) -> None:
        cls.ds.session.execute("DROP TABLE test_children;")

    def test_add(self):
        row_count = self.ds.session.execute("SELECT COUNT(*) FROM test_children").one()[0]

        c = TestChild('Janusz', 49)
        self.ds.add(c)

        current_row_count = self.ds.session.execute("SELECT COUNT(*) FROM test_children").one()[0]
        self.assertEqual(current_row_count, row_count + 1)

        row = self.ds.session.execute(f"SELECT * FROM test_children WHERE c_id = {c.c_id};").one()
        self.assertIsNotNone(row)
        
    def test_delete(self):
        c = TestChild('Jerzy', 28)
        self.ds.add(c)

        row_count = self.ds.session.execute("SELECT COUNT(*) FROM test_children").one()[0]
        self.assertTrue(row_count > 0)

        row = self.ds.session.execute(f"SELECT * FROM test_children WHERE c_id = {c.c_id};").one()
        self.assertEqual('Jerzy', row[2])

        self.ds.remove(c)

        current_row_count = self.ds.session.execute("SELECT COUNT(*) FROM test_children").one()[0]
        self.assertEqual(current_row_count, row_count - 1)

    def test_update(self):
        c = TestChild('Ryszard', 68)
        self.ds.add(c)

        row = self.ds.session.execute(f"SELECT * FROM test_children WHERE c_id = {c.c_id};").one()
        self.assertEqual(68, row[1])
        self.assertEqual('Ryszard', row[2])

        c.c_age = 69
        self.ds.update(c)

        row = self.ds.session.execute(f"SELECT * FROM test_children WHERE c_id = {c.c_id};").one()
        self.assertEqual(69, row[1])

    def test_get(self):
        c = TestChild('Zbigniew', 10)
        self.ds.add(c)

        row = self.ds.get(c.c_id, 'test_children', 'c_id')
        self.assertEqual(10, row[1])
        self.assertEqual('Zbigniew', row[2])

    def test_find_all(self):
        c1 = TestChild('Mariusz', 4)
        c2 = TestChild('Eustachy', 2)
        self.ds.add(c1)
        self.ds.add(c2)

        rows = self.ds.find_all('test_children')

        self.assertTrue(len(rows) >= 2)

        self.assertTrue((c1.c_id, 4, 'Mariusz') in rows)
        self.assertTrue((c2.c_id, 2, 'Eustachy') in rows)

    def test_find_by(self):
        c1 = TestChild('Aa', 5)
        c2 = TestChild('Bb', 4)
        c3 = TestChild('Cc', 13)
        self.ds.add(c1)
        self.ds.add(c2)
        self.ds.add(c3)

        rows = self.ds.find_by('test_children', 'c_age < 10')

        self.assertTrue(len(rows) >= 2)

        self.assertTrue((c1.c_id, 5, 'Aa') in rows)
        self.assertTrue((c2.c_id, 4, 'Bb') in rows)

        rows = self.ds.find_by('test_children', "c_name = 'Cc'")

        self.assertEqual(1, len(rows))
        self.assertEqual(13, rows[0].c_age)
        self.assertEqual('Cc', rows[0].c_name)

if __name__ == '__main__':
    unittest.main()