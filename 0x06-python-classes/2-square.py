#!/usr/bin/python3
"""This module defines a class, Square, that represents a geometric shape"""


class Square:
    """This class defines a Square shape by its size

    Attributes:
        __size (int): The size of the square.
    """

    def __init__(self, size=0):
        """Initialize the square with an optional size parameter

        Args:
            size (int, optional): The size of the square. Defaults to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size if negative.
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
