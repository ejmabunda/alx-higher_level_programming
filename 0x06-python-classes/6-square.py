#!/usr/bin/python3
"""This module defines a class, Square, that represents a geometric shape"""


class Square:
    """This class defines a Square shape by its size and area, and position

    Attributes:
        __size (int): The size of the square.
        __position (tuple): The square's left and top offset
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with an optional size and position parameters

        Args:
            size (int, optional): The size of the square. Defaults to 0.
            position (tuple, optional): The position of the square. (0, 0)
            by default.

        Raises:
            TypeError: If size is not an integer, or position is not a
            tuple of 2 integers
            ValueError: If size is negative, or position contains negatives
        """
        # Initialize size
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

        """if type(position) is not tuple or len(position) != 2:
            raise TypeError("position must be a tuple of 2 integers")
        if position[0] < 0 or position[1] < 0:
            raise TypeError("position must be a tuple of 2 integers")
        if position[0] is not int or position[1] is not int:
            raise TypeError("position must be a tuple of 2 integers")"""
        self.__position = position

    def area(self):
        """Returns the current square area.

        Returns:
            int: The area of the square.
        """
        return self.__size ** 2

    @property
    def size(self):
        """Returns the size of the square.

        Returns:
            int: The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets the size of the square.

        Args:
            value (int): The new size of the square.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is negative.
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Returns the position of the square.

        Returns:
            tuple: The square's top and left offset
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Sets the position of the square.

        Args:
            value (tuple): The new position of the square.

        Raises:
            TypeError: If value is not a tuple of 2 integers.
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError("position must be a tuple of 2 integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 integers")
        if value[0] is not int or value[1] is not int:
            raise TypeError("position must be a tuple of 2 integers")
        self.__position = value

    def my_print(self):
        """Prints a square using the # character"""
        if self.__size == 0:
            print()
        else:
            # add empty lines for top offset
            for line in range(self.__position[1]):
                print()

            for row in range(self.__size):
                # add preceding spaces for left offset
                for space in range(self.__position[0]):
                    print(' ', end="")

                # draw line in square
                for col in range(self.__size):
                    print('#', end="")
                print()
