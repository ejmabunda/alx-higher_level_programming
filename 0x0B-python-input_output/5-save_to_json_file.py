#!/usr/bin/python3
"""This function supplies a function, save_to_json_file"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an Object to a a text file, using JSON.

    Args:
        my_obj (obj): The Object to write to a file.
        filiname (str): The name of the file to write to.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        json.dump(my_obj, file)
