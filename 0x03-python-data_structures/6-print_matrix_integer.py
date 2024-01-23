#!/usr/bin/python3
def print_matrix_integer(matrix=[]):
    for row in matrix:
        for col in row:
            if (row.index(col) == 0):
                print("{:d}".format(col), end="")
            else:
                print(" {:d}".format(col), end="")
        print()
