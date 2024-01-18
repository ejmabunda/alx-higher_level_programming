#!/usr/bin/python3
for code in reversed(range(97, 123)):
    if code % 2 == 0:
        print(chr(code), end="")
    else:
        print(chr(code - 32), end="")
