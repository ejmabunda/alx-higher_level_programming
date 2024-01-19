#!/usr/bin/python3
import sys
# this code shouldn't execute when imported
if __name__ == "__main__":
    sum = 0
    for i in range(1, len(sys.argv)):
        sum += int(sys.argv[i])

    print("{0}".format(sum))
