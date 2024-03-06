#!/usr/bin/python3
"""This module supplies a function, pascal_triangle"""


def pascal_triangle(n):
    """Returns a list of lists of integers representing Pascal's Triangle

    Args:
        n (int): The number of rows.

    Returns:
        list(list): A representation of Pascal's triangle.

    """
    triangle = []
    for row in range(n):
        row_list = []
        for col in range(row):
            row_list.append(1)

        triangle.append(row_list)
