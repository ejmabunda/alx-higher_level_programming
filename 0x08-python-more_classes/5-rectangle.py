#!/usr/bin/python3
"""This module defines the Rectangle class

The Rectangle class the geometric shape, rectangle
"""


class Rectangle:
    """Represents a rectangle with width and height attributes.

    Args:
        width (int, optional): The width of the rectangle.
            Defaults to 0.
        height (int, optional): The height of the rectangle.
            Defaults to 0.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        number_of_instances (int): The number of Rectangle instances

    """

    def __init__(self, width=0, height=0):
        """Initializes a new Rectangle instance.

        Args:
            width (int, optional): The width of the rectangle.
                Defaults to 0.
            height (int, optional): The height of the rectangle.
                Defaults to 0.

        """
        self.__height = height
        self.__width = width

    @property
    def width(self):
        """Getter method for retrieving the width.

        Returns:
            int: The width of the rectangle.
        """
        return self.__width

    @property
    def height(self):
        """Getter method for retrieving the height.

        Returns:
            int: The height of the rectangle.
        """
        return self.__height

    @width.setter
    def width(self, value):
        """Setter method for setting the width.

        Args:
            value (int): The new width of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @height.setter
    def height(self, value):
        """Setter method for setting the height.

        Args:
            value (int): The new height of the rectangle.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    def area(self):
        """Calculates the area of the rectangle.

        Returns:
            int: The area of the rectangle.

        """
        return self.__width * self.__height

    def perimeter(self):
        """Computes the permiter of the rectangle.

        Returns:
            int: The perimeter of the rectangle.

        """
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """Prints the rectangle with the character ``#``
        """
        rect = ""
        for row in range(self.__height):
            for col in range(self.__width):
                rect += "#"
            rect += "\n"

        return rect

    def __repr__(self):
        """Method for the string representation of the rectangle

        Returns:
            str: String representation of the rectangle such that
                a new instance can be created using eval()

        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Prints a message when a rectangle is deleted"""
        print("Bye rectangle...")
