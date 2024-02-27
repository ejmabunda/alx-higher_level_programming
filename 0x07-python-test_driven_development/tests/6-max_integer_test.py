#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Test class for the max_integer function"""

    def test_max_integer(self):
        """Function to test the max_integer function"""
        self.assertEqual(max_integer([1, 2, 3, 4, 5]), 5)
        self.assertEqual(max_integer([]), None)
        self.assertEqual(max_integer([10]), 10)
        self.assertEqual(max_integer([-10, -7, -9, -3]), -3)
        self.assertEqual(max_integer([5, 5]), 5)
