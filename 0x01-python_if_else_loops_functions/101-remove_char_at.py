#!/usr/bin/python3
def remove_char_at(str, n):
    copy = ""
    index = 0
    for letter in str:
        if index == n:
            index += 1
            continue

        copy = "".join([copy, letter])
        index += 1

    return copy
