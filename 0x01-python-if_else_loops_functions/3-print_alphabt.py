#!/usr/bin/python3
for code in range(97, 123):
    if chr(code) != 'q' and chr(code) != 'e':
        print("{0}".format(chr(code)), end="")
