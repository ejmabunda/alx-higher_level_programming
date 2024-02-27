#!/usr/bin/python3
"""This module supplies one function, matrix_divided()"""


def matrix_divided(matrix, div):
    """Divides all elements of matrix by div

    Args:
        matrix (:obj:`list` of :obj:`list`): 2-d array of
            integers and floats.
        div (int): The integer to divide matrix elements by

    Returns:
        A divided matrix.

    Raises:
        TypeError: If any element of matrix is not an integer
            or float.
            If rows have different sizes.
            If div is not an integer.
        ZeroDivisionError: If div is 0.
    """
    # div must be a non-zero number
    if div == 0:
        raise ZeroDivisionError("division by zero")
    elif not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    row_len = len(matrix[0])
    new_matrix = []

    for row in matrix:
        if len(row) != row_len:  # Check row length
            raise TypeError("Each row of the matrix must have the same size")

        new_row = []

        for elem in row:
            if not isinstance(elem, (int, float)):  # Check type
                raise TypeError("matrix must be a matrix (list of lists), of integers/floats")
            new_row.append(round(elem / div, 2))

        new_matrix.append(new_row)

    return new_matrix
