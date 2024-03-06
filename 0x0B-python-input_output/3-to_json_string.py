#!/usr/bin/python3
"""This function supplies a function, to_json_string"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object.

    Args:
        obj (str): The object to encode.

    Returns:
        str: The JSON representation of an object.

    """
    return json.dumps(my_obj)
