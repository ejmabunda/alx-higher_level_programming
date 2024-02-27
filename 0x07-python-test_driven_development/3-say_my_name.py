#!/usr/bin/python3
"""This module supplies one function, say_my_name()"""


def say_my_name(first_name, last_name=""):
    """Prints provided name

    Args:
        first_name (str): Represents a persons first name.
        last_name (str, optional): Represents a person's last name.

    Raises:
        TypeError: If either first_name or last_name is not a string.

    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    print(f"My name is {first_name} {last_name}")
