#!/usr/bin/python3
import unittest
from models.rectangle import Rectangle
# from unittest.mock import patch


class TestRectangle(unittest.TestCase):
    def test_RectangleId(self):
        """Test case for a Rectangle's id"""

        Rectangle.reset()

        self.r1 = Rectangle(10, 2)
        self.assertEqual(self.r1.id, 1)

        self.r2 = Rectangle(2, 10)
        self.assertEqual(self.r2.id, 2)

        self.r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(self.r3.id, 12)

        Rectangle.reset()  # Reset class attribute, 'id'

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

    def test_RectangleArea(self):
        """Test case for the Rectangle.area() function"""
        r1 = Rectangle(3, 2)
        self.assertEqual(r1.area(), 6)

        r2 = Rectangle(2, 10)
        self.assertEqual(r2.area(), 20)

        r3 = Rectangle(8, 7, 0, 0, 12)
        self.assertEqual(r3.area(), 56)

        Rectangle.reset()  # Reset class attribute, 'id'

    '''@patch('sys.stdout', new_callable=StringIO)
    def test_RectangleDisplay(self, mock_stdout):
        """Test cases for the display function"""
        r1 = Rectangle(4, 6)
        r1.display()
        self.assertEqual(mock_stdout.getValue().strip(), "####\n" * 6)

        Rectangle.reset()  # Reset class attribute, 'id'''

    def test___str__(self):
        """Test cases for the __str__ function"""
        Rectangle.reset()
        r1 = Rectangle(4, 6, 2, 1, 12)
        self.assertEqual(r1.__str__(), '[Rectangle] (12) 2/1 - 4/6')

        r2 = Rectangle(5, 5, 1)
        self.assertEqual(r2.__str__(), '[Rectangle] (1) 1/0 - 5/5')

        Rectangle.reset()

    def test_RectangleUpdate(self):
        """Test cases for the update funtion"""
        r1 = Rectangle(10, 10, 10, 10)
        self.assertEqual(r1.__str__(), '[Rectangle] (1) 10/10 - 10/10')

        r1.update(89)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 10/10 - 10/10')

        r1.update(89, 2)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 10/10 - 2/10')

        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 10/10 - 2/3')

        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 4/10 - 2/3')

        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), '[Rectangle] (89) 4/5 - 2/3')

        Rectangle.reset()  # Resets Rectangle's class attribute, 'id'
