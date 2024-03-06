#!/usr/bin/python3
"""This module supplies a function, class_to_json"""


def class_to_json(obj):
    """Returns the dictionary description of an object.

    Args:
        obj (obj): The object to serialize.

    Returns:
        obj: The dictionary description of an object.

    """
    return obj.__dict__
