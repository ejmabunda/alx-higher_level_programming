#!/usr/bin/env python3
import unittest
from models.base import Base


class TestBase(unittest.TestCase):
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
