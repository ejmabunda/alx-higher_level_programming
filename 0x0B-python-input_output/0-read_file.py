#!/usr/bin/python3
"""This module supplies a function, read_file"""


def read_file(filename=""):
    """Reads a text file and prints it to stdout

    Args:
        filename (str, optional): The name of the file to read.

    """
    with open(filename, encoding='utf-8') as file:
        print(file.read())
