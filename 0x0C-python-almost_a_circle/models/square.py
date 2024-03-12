#!/usr/bin/python3
"""This module supplies a the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents the Square geometric shape"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Returns the width of the Square instance.

        Returns:
            int: The width of the Square instance.

        """
        return self.width

    @size.setter
    def size(self, value):
        """Updates the width of the Square instance.

        Args:
            value (int): Represents the new value of the width of
                the Square.

        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Updates attributes of the Square instance.

        Args:
            *args: Variable length no-keyword arguments, expected
                id (int): The new value for Square id.
                size (int): The new value for Square size.
                x (int): The new value for Square x offset.
                y (int): The new value for Square y offset.

            **kwargs: Variable-length keyworded arguments, expected
                id (int): The new value for Square id.
                size (int): The new value for Square size.
                x (int): The new value for Square x offset.
                y (int): The new value for Square y offset.

        """
        if len(args) != 0:
            counter = 0
            for item in args:
                if counter == 0:
                    self.integer_validator(id=item)
                    self.id = item
                elif counter == 1:
                    self.size = item
                elif counter == 2:
                    self.x = item
                elif counter == 3:
                    self.y = item
                counter += 1
            return

        for attr, value in kwargs.items():
            if attr == 'id':
                self.integer_validator(id=value)
                self.id = value
            elif attr == 'size':
                self.size = value
            elif attr == 'x':
                self.x = value
            elif attr == 'y':
                self.y = value
