#!/usr/bin/python3
"""This module supplies one function, inherits_from()"""


def inherits_from(obj, a_class):
    """Checks if an object inherits from a class

    Args:
        obj (object): The object to check.
        a_class (class): The class to compare obj with.

    Returns:
        bool: True if obj is an instance of a class that inherited
            from a_class. False otherwise.

    """
    if type(obj) is a_class:
        return False
    return issubclass(type(obj), a_class)
