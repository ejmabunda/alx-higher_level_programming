#!/usr/bin/python3
"""This module supplies one class, BaseGeometry

"""


class BaseGeometry:
    """Represents geometric shapes"""
    def area(self):
        """Raises an Exception

        Raises:
            Exception: raised when called.

        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates a value

        Args:
            name (str): name
            value (int): value

        Raises:
            TypeError: if value is not an integer.
            ValueError: if value is less or equal to 0.

        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise TypeError(f"{name} must be greater than 0")
