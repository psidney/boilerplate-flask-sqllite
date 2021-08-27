import unittest
import os

from src.database import Database, Table

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.testDatabase = Database('test.db')
        tableName = "_test_"
        columnKeyPairs = {"test":"text",
                          "date":"text"}

        self.testDatabase.createTable(tableName,columnKeyPairs)
        return

    def test_createTable(self):
        tableName = "__test__"

        
        # Test createTable with bad keypairs, fail
        columnKeyPairs = {"test","blah"}
        with self.assertRaises(ValueError):
            self.testDatabase.createTable(tableName,columnKeyPairs)

        columnKeyPairs = {"test":"text",
                          "date":"text"}

        # Test createTable, success
        self.assertEqual(True, self.testDatabase.createTable(tableName,columnKeyPairs))

        # Test createTable when Table exists, fail
        with self.assertRaises(ValueError):
            self.testDatabase.createTable(tableName,columnKeyPairs)


    def test_dropTable(self):
        tableName = "_test_"
        # Test dropTable when Table exists
        self.assertEqual(True,self.testDatabase.dropTable(tableName))

        
        # Test dropTable when Table does not exist
        with self.assertRaises(ValueError):
            self.testDatabase.dropTable(tableName)

    def test_selectRecord(self):
        tableName = '_test_'
        
        self.assertIsInstance(self.testDatabase.selectTable(tableName), Table)

        with self.assertRaises(ValueError):
            self.testDatabase.selectTable('nonExistant')

    def test_insertRecord(self):
        table = self.testDatabase.selectTable('_test_')

        self.assertEqual(True, table.insertRecord(['a','b']))

        with self.assertRaises(ValueError):
            table.insertRecord(['a','b','c'])

    def test_insertRecords(self):
        table = self.testDatabase.selectTable('_test_')

        self.assertEqual(True, table.insertRecords([['a','b'],['c','d']]))

        with self.assertRaises(ValueError):
            table.insertRecord([['a','b','c'],['a','b','c']])


    def tearDown(self):
        self.testDatabase.connection.close()
        os.remove('test.db')
        return

if __name__ == '__main__':
    unittest.main()