#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    # to store num of actual printed elems
    printed = 0
    for i in range(x):
        # try to print, then increment counter
        try:
            print(my_list[i], end="")
            printed += 1
        # end of list reached
        except IndexError:
            break

    print()
    return printed
