#!/usr/bin/python3
""" Test the City"""
from tests.test_models.test_base_model import test_basemodel
from models.city import City
import unittest
import os


class test_City(test_basemodel):
    """ Test city unittest"""

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Using DB")
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "City"
        self.value = City

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Using DB")
    def test_state_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.state_id), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Using DB")
    def test_name(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.name), str)
