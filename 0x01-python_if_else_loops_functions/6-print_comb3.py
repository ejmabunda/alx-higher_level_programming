#!/usr/bin/python3
for left in range(0, 10):
    for right in range(0, 10):
        if left == right or int(f"{right}{left}") < int(f"{left}{right}"):
            continue
        if left == 8 and right == 9:
            print("{0}{1}".format(left, right))
        else:
            print("{0}{1}".format(left, right), end=", ")
