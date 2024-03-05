#!/usr/bin/python3
"""This module supplies a class, Square
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a rectangle

    Attributes:
        size (int): represents a side of the square.

    """
    def __init__(self, size):
        super().__init__(size, size)
        self.integer_validator("size", size)

        self.__size = size

    def area(self):
        """Calculates the area of the square

        Returns:
            int: The area of the square.

        """
        return self.__size ** 2
