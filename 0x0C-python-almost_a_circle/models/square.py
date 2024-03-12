#!/usr/bin/python3
"""This module supplies a the Square class"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represents the Square geometric shape"""
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"
