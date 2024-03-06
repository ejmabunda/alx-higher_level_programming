#!/usr/bin/python3
"""This module supplies a class, Student"""


class Student:
    """Represents a student

    Attributes:
        first_name (str): A student't first name.
        last_name (str): A student't last name.
        age (int): A student't age.

    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student

        Args:
            attrs (list, optional): A list of attributes to retrieve.
                Defaults to None.

        Returns:
            obj: A dictionary representation of a Student instance.

        """
        if attrs is not None:
            return {attr: getattr(self, attr, None) for attr in attrs
                    if getattr(self, attr, None) is not None}
        return self.__dict__

    def reload_from_json(self, json):
        """Replaces all attributes of the Student instance.

        Args:
            json (dict): A dictionary of with attributes to replace with.

        """
        self.first_name = json.get('first_name')
        self.last_name = json.get('last_name')
        self.age = json.get('age')
