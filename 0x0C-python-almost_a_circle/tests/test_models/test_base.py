#!/usr/bin/env python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
import json


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

    def test_save_to_file(self):
        """Test cases for the test_to_file function."""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        Rectangle.save_to_file([r1, r2])

        with open("Rectangle.json", "r") as file:
            # Load JSON data from file
            data = json.load(file)
            # Expected result
            expected = [{"y": 8, "x": 2, "id": 1, "width": 10, "height": 7}, {"y": 0, "x": 0, "id": 2, "width": 2, "height": 4}]
            self.assertEqual(data, expected)
