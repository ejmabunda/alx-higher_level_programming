#!/usr/bin/python3
"""This module supplies a class, MyList"""


class MyList(list):
    """Represents a list

    Methods:
        print_sorted(): Prints the list sorted in ascending
            order.

    """
    def __init__(self):
        super().__init__()

    def print_sorted(self):
        """Prints the list sorted in ascending order"""
        print(sorted(self))
