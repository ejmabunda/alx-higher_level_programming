#!/usr/bin/python3
"""This function supplies a function, write_file"""


def write_file(filename="", text=""):
    """Writes a string to a text file

    Args:
        filename (str, optional): The name of the file
            to write to. Defaults to an empty string.
        text (str, optional): The contents that written to the
            file. Defaults to an empty string.

    Returns:
        int: The number of characters written.

    """
    with open(filename, 'w', encoding='utf-8') as file:
        num_chars = file.write(text)

    return num_chars
