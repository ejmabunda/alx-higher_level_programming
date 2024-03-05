#!/usr/bin/python3
"""This module supplies one funtion, lookup()"""


def lookup(obj):
    """Retrives an object's attributes and methods

    Args:
        obj (object): The object to retrive attributes of.

    Returns:
        list: A list of obj's attributes and methods.

    """
    return dir(obj)
