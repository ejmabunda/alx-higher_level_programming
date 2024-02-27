#!/usr/bin/python3
"""This module provides one function, add_integer"""


def add_integer(a, b=98):
    """Add two integers

    Args:
        a: The first integer.
        b (optional): The second integer.

    Returns:
        int: The sum of a and b.

    Raises:
        TypeError: If either a or b is not an integer.


    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
