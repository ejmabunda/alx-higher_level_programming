#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_IntegerValidator(self):
        """Test case for the integer_validator function."""
        # Tests for width/height types.
        with self.assertRaises(TypeError) as e:
            Rectangle(10, "2")
        self.assertEqual(str(e.exception), 'height must be an integer')
        
        with self.assertRaises(TypeError) as e:
            Rectangle("10", 2)
        self.assertEqual(str(e.exception), 'width must be an integer')

        # Tests for width/height values.
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 0)
        self.assertEqual(str(e.exception), 'height must be > 0')

        with self.assertRaises(ValueError) as e:
            Rectangle(0, 2)
        self.assertEqual(str(e.exception), 'width must be > 0')

        # Tests for x/y values.
        with self.assertRaises(ValueError) as e:
            Rectangle(10, 3, -1, 3)
        self.assertEqual(str(e.exception), 'x must be >= 0')

        with self.assertRaises(ValueError) as e:
            Rectangle(1, 2, 2, -2)
        self.assertEqual(str(e.exception), 'y must be >= 0')

        Rectangle.reset()  # Reset class attribute, 'id'

    def test_RectangleId(self):
        """Test case for a Rectangle's id"""
        self.r1 = Rectangle(10, 2)
        self.assertEqual(self.r1.id, 1)

        self.r2 = Rectangle(2, 10)
        self.assertEqual(self.r2.id, 2)

        self.r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(self.r3.id, 12)

        Rectangle.reset()  # Reset class attribute, 'id'

    def test_RectangleArea(self):
        """Test case for the Rectangle.area() function"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

        Rectangle.reset()  # Reset class attribute, 'id'
