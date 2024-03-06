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

    def to_json(self):
        """Retrieves a dictionary representation of a Student

        Returns:
            obj: A dictionary representation of a Student instance.

        """
        return self.__dict__
