#!/usr/bin/python3
import sys
if __name__ == "__main__":  # this code shouldn't execute when imported
    num_args = len(sys.argv)
    if num_args == 1:
        str = "arguments."
    elif num_args > 2:
        str = "arguments:"
        for i in range(1, num_args):
            str = "{0}\n{1}: {2}".format(str, i, sys.argv[i])
    else:
        str = "argument:\n{0}: {1}".format(1, sys.argv[1])

    print("{0} {1}".format(num_args - 1, str))
