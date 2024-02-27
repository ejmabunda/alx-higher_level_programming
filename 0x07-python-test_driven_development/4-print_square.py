#!/usr/bin/python3
"""This module supplies one function, print_square()"""


def print_square(size):
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    if isinstance(size, float):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")

    for row in range(size):
        for col in range(size):
            print("#", end="")
        print()
