#!/usr/bin/python3
"""This function supplies a function, append_write"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file

    Args:
        filename (str, optional): The name of the file
            to append to. Defaults to an empty string.
        text (str, optional): The contents to add to the
            file. Defaults to an empty string.

    Returns:
        int: The number of characters added.

    """
    with open(filename, 'a', encoding='utf-8') as file:
        num_chars = file.write(text)

    return num_chars
