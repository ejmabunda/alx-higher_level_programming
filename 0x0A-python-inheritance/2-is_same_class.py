#!/usr/bin/python3
"""This module supplies one function, is_same_class()"""


def is_same_class(obj, a_class):
    """Checks if obj is an instance of a_class

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare with.

    Returns:
        bool: True if obj is an instance of a_class,
            False otherwise.

    """
    return type(obj) is a_class
