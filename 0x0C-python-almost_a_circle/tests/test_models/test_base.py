#!/usr/bin/env python3
import unittest
from models.base import Base
from models.rectangle import Rectangle


class TestBase(unittest.TestCase):
    """Test class for the Base class."""
    def setUp(self):
        """Called before each test."""
        Rectangle.reset()

    def tearDown(self):
        """Called after each test."""
        Rectangle.reset()

    def test_BaseId(self):
        self.b1 = Base()
        self.assertEqual(self.b1.id, 1)
        self.b2 = Base()
        self.assertEqual(self.b2.id, 2)
        self.b3 = Base()
        self.assertEqual(self.b3.id, 3)
        self.b4 = Base(12)
        self.assertEqual(self.b4.id, 12)
        self.b5 = Base()
        self.assertEqual(self.b5.id, 4)

    def test_to_string_json(self):
        """Test cases for the to_json_string function."""
        r1 = Rectangle(10, 7, 2, 8)
        dictionary = r1.to_dictionary()
        json_dictionary = Base.to_json_string([dictionary])
        self.assertEqual(dictionary, {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8})

        self.assertEqual(type(dictionary), dict)

        self.assertEqual(json_dictionary, '[{"x": 2, "width": 10, "id": 1, "height": 7, "y": 8}]')

        self.assertEqual(type(json_dictionary), str)
