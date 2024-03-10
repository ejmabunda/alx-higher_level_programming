#!/usr/bin/env python3
import unittest
from models.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_IntegerValidator(self):
        with self.assertRaises(TypeError):
            Rectangle(10, "2")
        Rectangle.reset()

    def test_RectangleId(self):
        self.r1 = Rectangle(10, 2)
        self.assertEqual(self.r1.id, 1)

        self.r2 = Rectangle(2, 10)
        self.assertEqual(self.r2.id, 2)

        self.r3 = Rectangle(10, 2, 0, 0, 12)
        self.assertEqual(self.r3.id, 12)
