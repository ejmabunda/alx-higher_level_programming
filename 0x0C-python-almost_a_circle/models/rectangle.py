#!/usr/bin/python3
"""This module supplies the Rectangle class
"""
from models.base import Base


class Rectangle(Base):
    """Represents a geometric shape, the Rectangle.

    Attributes:
        width (int): The width of the rectangle.
        height (int): The height of the rectangle.
        x (int): Horizontal position of the rectangle.
        y (int): Vertical position of the rectangle.

    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)

        self.integer_validator(width=width)
        self.__width = width

        self.integer_validator(height=height)
        self.__height = height

        self.integer_validator(x=x)
        self.__x = x

        self.integer_validator(y=y)
        self.__y = y

    def integer_validator(self, **kwargs):
        """Validates integers

        Args:
            **kwargs: Arbitrary keyword arguments, expecting
                width (int): represents the width of the rectangle.
                height (int): represents the height of the rectangle.
                x (int): represents the horizontal position of the rectangle.
                y (int): represents the vertical position of the rectangle.

        Raises:
            TypeError: If kwargs contains a non-integer.
            ValueError: If kwargs contains width (or height) <= 0,
                or kwargs contains x (or y) < 0.

        """
        for name, n in kwargs.items():
            if not isinstance(n, int):
                raise TypeError(f"{name} must be an integer")
            if name == 'width' or name == 'height':
                if n <= 0:
                    raise ValueError(f"{name} must be > 0")

    @property
    def width(self):
        """Returns the private property, width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Sets a new value for the private property, width"""
        self.integer_validator(width=value)
        self.__width = value

    @property
    def height(self):
        """Returns the private property, height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets a new value for the private property, height"""
        self.integer_validator(height=value)
        self.__height = value

    @property
    def x(self):
        """Returns the private property, x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets a new value for the private property, x"""
        self.integer_validator(x=value)
        self.__x = value

    @property
    def y(self):
        """Returns the private property, y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets a new value for the private property, y"""
        self.integer_validator(y=value)
        self.__y = value

    def area(self):
        """Calculates the area of the rectangle instance.

        Returns:
            int: The area value of the rectangle instance.

        """
        return self.__width * self.__height
