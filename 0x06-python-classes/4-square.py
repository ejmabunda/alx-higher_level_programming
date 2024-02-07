#!/usr/bin/python3
"""This module defines a class, Square, that represents a geometric shape"""


class Square:
    """This class defines a Square shape by its size and area

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

    def area(self):
        """Return the current square area

        Returns: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of the square

        Returns: 
            int: The size of the square
        """
        return __size

    @size.setter
    def size(self, value):
        """Sets the size of the square

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value if negative.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value
