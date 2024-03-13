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

    def test_from_json_string(self):
        """Test cases for the from_json_string method."""
        list_input = [
            {'id': 89, 'width': 10, 'height': 4},
            {'id': 7, 'width': 1, 'height': 7}
        ]

        json_list_input = Rectangle.to_json_string(list_input)

        list_output = Rectangle.from_json_string(json_list_input)

        expected_list_input = sorted([{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}], key=lambda x: x['id'])
        expected_json_list_input = sorted([{"height": 4, "width": 10, "id": 89}, {"height": 7, "width": 1, "id": 7}], key=lambda x: x['id'])
        expected_list_output = sorted([{'height': 4, 'width': 10, 'id': 89}, {'height': 7, 'width': 1, 'id': 7}], key=lambda x: x['id'])

        list_input.sort(key=lambda x: x['id'])
        json_list_input = json.dumps(sorted(json.loads(json_list_input), key=lambda x: x['id']), sort_keys=True)
        list_output.sort(key=lambda x: x['id'])

        self.assertEqual(type(list_input), list)
        self.assertEqual(json.dumps(list_input, sort_keys=True), json.dumps(expected_list_input, sort_keys=True))

        self.assertEqual(type(json_list_input), str)
        self.assertEqual(json_list_input, json.dumps(expected_json_list_input, sort_keys=True))

        self.assertEqual(type(list_output), list)
        self.assertEqual(json.dumps(list_output, sort_keys=True), json.dumps(expected_list_output, sort_keys=True))
