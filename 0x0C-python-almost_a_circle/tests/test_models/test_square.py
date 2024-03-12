#!/usr/bin/python3
"""This module supplies the TestSquare class"""
import unittest
from models.square import Square


class TestSquare(unittest.TestCase):
    """Test cases for the square module"""

    def setUp(self):
        """Called before each test"""
        Square.reset()  # Resets the number of instances attribute.

    def tearDown(self):
        """Called after each test"""
        Square.reset()  # Resets the number of instances attribute.

    def test_Square__str__(self):
        """Test cases for the Square __str__ method."""
        s1 = Square(5)
        self.assertEqual(s1.__str__(), '[Square] (1) 0/0 - 5')

        s2 = Square(2, 2)
        self.assertEqual(s2.__str__(), '[Square] (2) 2/0 - 2')

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.__str__(), '[Square] (3) 1/3 - 3')

    def test_SquareArea(self):
        """Test cases for the area function"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)

        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)

    def test_SquareSize(self):
        """Test cases for the size setter method."""
        s1 = Square(5)

        self.assertEqual(s1.__str__(), '[Square] (1) 0/0 - 5')

        self.assertEqual(s1.size, 5)

        s1.size = 10

        self.assertEqual(s1.__str__(), '[Square] (1) 0/0 - 10')

        try:
            s1.size = "9"
        except Exception as e:
            self.assertEqual('TypeError', e.__class__.__name__)
