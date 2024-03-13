#!/usr/bin/python3
"""This module supplies a class, Base.
"""
import json


class Base:
    """Represents the base of all classes in this project.

    Attributes:
        nb_objects (int): Represents the number of objects.

    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def reset(cls):
        """Resets the number of objects to 0, for testing."""
        Base.__nb_objects = 0

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns the JSON string representation of a list of dictionaries.

        Args:
            list_dictionaries (list `dict`): A list of dictionaries.

        Returns:
            str: The JSON string representation of a list of dictionaries.

        """
        if not list_dictionaries:
            return "[]"

        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON representation of objects to a file.

        Args:
            list_objs (List[obj]): A list of objects.

        """
        filename = cls.__name__ + ".json"
        
        list_dicts = [obj.to_dictionary() for obj in list_objs]
        with open(filename, 'w') as f:
            if not list_objs:
                f.write([])
            else:
                f.write(cls.to_json_string(list_dicts))
