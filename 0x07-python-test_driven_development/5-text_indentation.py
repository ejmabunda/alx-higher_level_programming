#!/usr/bin/python3
"""This module supplies one funtion, text_indentation()"""


def text_indentation(text):
    # text must be a string
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    skip = False

    for char in text:
        if char in ".?:":  # skip next char, if whitespace
            print(f"{char}\n")
            skip = True
            continue
        elif char == " ":
            if skip:
                skip = False
                continue
            print(char, end="")
        else:
            skip = False
            print(char, end="")
