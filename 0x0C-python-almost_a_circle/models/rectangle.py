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
            if name == 'x' or name == 'y':
                if n < 0:
                    raise ValueError(f"{name} must be >= 0")

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

    def display(self):
        """Prints the rectangle using #."""
        for row in range(self.__height):
            for col in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """Returns a string representation of a Rectangle.

        Returns:
            str: A string representation of a Rectangle.

        """
        # I had to split for pycodestyle.
        s = f"[Rectangle] ({self.id}) {self.x}/{self.y} "

        return s + f"- {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """Assigns a new value to each attribute.

        Args:
            *args: Variable length no-keyword arguments, expected
                id (int): The new value for Rectangle id.
                width (int): The new value for Rectangle width.
                height (int): The new value for Rectangle height.
                x (int): The new value for Rectangle x offset.
                y (int): The new value for Rectangle y offset.

            **kwargs: Variable length keyworded arguments, expected
                id (int): The new value for Rectangle id.
                width (int): The new value for Rectangle width.
                height (int): The new value for Rectangle height.
                x (int): The new value for Rectangle x offset.
                y (int): The new value for Rectangle y offset.

        """
        if len(args) != 0:
            counter = 0
            for n in args:
                if counter == 0:
                    self.integer_validator(id=n)
                    self.id = n
                elif counter == 1:
                    self.width = n
                elif counter == 2:
                    self.height = n
                elif counter == 3:
                    self.x = n
                elif counter == 4:
                    self.y = n
                counter += 1
            return

        for attr, value in kwargs.items():
            if attr == 'id':
                self.integer_validator(id=value)
                self.id = value
            elif attr == 'width':
                self.width = value
            elif attr == 'height':
                self.height = value
            elif attr == 'x':
                self.x = value
            elif attr == 'y':
                self.y = value
