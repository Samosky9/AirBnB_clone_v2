#!/usr/bin/python3
""" Unittests for reviews """
from tests.test_models.test_base_model import test_basemodel
from models.review import Review
import unittest
import os


class test_review(test_basemodel):
    """ """

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Using DB")
    def __init__(self, *args, **kwargs):
        """ """
        super().__init__(*args, **kwargs)
        self.name = "Review"
        self.value = Review

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Using DB")
    def test_place_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.place_id), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Using DB")
    def test_user_id(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.user_id), str)

    @unittest.skipIf(os.getenv('HBNB_TYPE_STORAGE') == 'db', "Using DB")
    def test_text(self):
        """ """
        new = self.value()
        self.assertEqual(type(new.text), str)
