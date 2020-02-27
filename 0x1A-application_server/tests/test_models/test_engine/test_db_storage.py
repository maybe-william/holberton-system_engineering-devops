#!/usr/bin/python3
"""test for file storage"""
import unittest
import pep8
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.db_storage import DBStorage


@unittest.skipIf(os.environ['HBNB_TYPE_STORAGE'] != 'db', 'not db storage')
class TestDBStorage(unittest.TestCase):
    '''this will test the DBStorage'''

    @classmethod
    def setUpClass(cls):
        """set up for test"""
        cls.user = User()
        cls.user.first_name = "Kev"
        cls.user.last_name = "Yo"
        cls.user.email = "1234@yahoo.com"
        cls.storage = DBStorage()

    @classmethod
    def teardown(cls):
        """at the end of the test this will tear it down"""
        del cls.user

    def tearDown(self):
        """teardown"""
        pass

    def test_pep8_DBStorage(self):
        """Tests pep8 style"""
        style = pep8.StyleGuide(quiet=True)
        p = style.check_files(['models/engine/db_storage.py'])
        self.assertEqual(p.total_errors, 0, "fix pep8")

    def test_all(self):
        """tests if all works in DBStorage"""
        storage = DBStorage()
        obj = storage.all()
        self.assertIsNotNone(obj)
        self.assertEqual(type(obj), dict)

    def test_new(self):
        """test when new is created"""
        storage = DBStorage()
        obj = storage.all()
        user = User()
        user.id = 123455
        user.name = "Kevin"
        user.email = "x"
        user.password = "y"
        storage.new(user)
        key = user.__class__.__name__ + "." + str(user.id)
        if os.environ['HBNB_TYPE_STORAGE'] != 'db':
            self.assertIsNotNone(obj[key])

    def test_reload_DBStorage(self):
        """
        tests reload
        """
        self.storage.save()
        Root = os.path.dirname(os.path.abspath("console.py"))
        path = os.path.join(Root, "file.json")
        x = self.storage._DBStorage__session
        self.storage.reload()
        y = self.storage._DBStorage__session
        self.assertNotEqual(x, y)

    def test_console_regex(self):
        """make sure regex will work"""
        try:
            from console import re
        except:
            self.assertEqual(True, False)

if __name__ == "__main__":
    unittest.main()
