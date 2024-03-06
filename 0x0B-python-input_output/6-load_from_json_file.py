#!/usr/bin/python3
"""This function supplies a function, load_from_json_file"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file

    Args:
        filename (str): The name of the file to retrive
            the Object from..

    """
    with open(filename, 'r', encoding='utf-8') as file:
        obj = json.load(file)

    return obj
