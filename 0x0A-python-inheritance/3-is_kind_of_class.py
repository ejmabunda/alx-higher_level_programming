#!/usr/bin/python3
"""This module supplies one function, is_kind_of_class()"""


def is_kind_of_class(obj, a_class):
    """Checks object against class

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare obj with.

    Returns:
        bool: True if obj is an instance of, or an instance of
            a class that inherited from a_class. False otherwise.

    """
    return isinstance(obj, a_class)
