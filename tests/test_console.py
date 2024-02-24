from console import HBNBCommand
from io import StringIO
from models import storage
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.engine.file_storage import FileStorage
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
from unittest.mock import patch
import os
import sys
import unittest


class ConsoleTest(unittest.TestCase):
    """ A class to test the console class """

    s_test = FileStorage()

    models = {
        "BaseModel": BaseModel,
        "User": User,
        "State": State,
        "City": City,
        "Amenity": Amenity,
        "Place": Place,
        "Review": Review
    }

    @classmethod
    def setUpClass(cls):
        """ creates all models to be used for testing """

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create BaseModel")
            cls.base_id = f.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create User")
            cls.user_id = f.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create State")
            cls.state_id = f.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create City")
            cls.city_id = f.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Amenity")
            cls.amenity_id = f.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Place")
            cls.place_id = f.getvalue()[:-1]

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("create Review")
            cls.review_id = f.getvalue()[:-1]

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Using DB")
    def testquit(self):
        """ tests the quit command """

        with patch("sys.stdout", new=StringIO()) as f:
            HBNBCommand().onecmd("quit")
            value = f.getvalue()
            self.assertEqual(value, "")
