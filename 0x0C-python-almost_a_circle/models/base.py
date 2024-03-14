#!/usr/bin/python3
"""This module supplies a class, Base.
"""
import json
import os


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
            if list_objs is None or list_objs == []:
                f.write('[]')
            else:
                f.write(cls.to_json_string(list_dicts))

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            List[dict]: If json_string is None or empty, return an empty list.
                        Otherwise, return the list represented by json_string.
        """
        if json_string is None or json_string == '':
            return ""
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            dictionary (dict): A dictionary consisting of object attributes.

        Returns:
            Rectangle: An new Rectangle instance with attributes set.

        """
        dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Retrieves a list of Rectangle/Square instances from a json file.

        Returns:
            List[Square or Rectangle]: A list of either Rectangle or
                Square instances.

        """
        filename = f'{cls.__name__}.json'
        if not os.path.isfile(filename):
            return []

        with open(filename, 'r', encoding='utf-8') as file:
            json_data = json.load(file)
            json_string = json.dumps(json_data)
            list_inst = cls.from_json_string(json_string)

        list_objs = []

        for inst in list_inst:
            list_objs.append(cls.create(**inst))

        return list_objs
