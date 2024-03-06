#!/usr/bin/python3
"""This function supplies a function, from_json_string"""
import json


def from_json_string(my_str):
    """Returns an object represented by a JSON string.

    Args:
        str (str): A JSON string that represents an object.

    Returns:
        obj: An object based on its string representation.

    """
    return json.loads(my_str)
