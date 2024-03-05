#!/usr/bin/python3
"""This module supplies one class, Rectangle

"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Represents the geometric shape, rectangle

    Attributes:
        width (int): represents the width of a rectangle.
        height (int): represents the height of a rectangle

    """
    def __init__(self, width, height):
        super().__init__()
        self.integer_validator("width", width)
        self.integer_validator("height", height)

        self.__width = width
        self.__height = height
