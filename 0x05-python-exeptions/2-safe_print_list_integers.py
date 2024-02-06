#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # to store the number of elements printed
    printed = 0

    for ix in range(x):
        # try to detect IndexError and TypeError
        try:
            print("{:d}".format(my_list[ix]), end="")
            printed += 1

        # reached end of list
        except IndexError:
            break

        # not an integer, skip
        except (ValueError, TypeError):
            continue

    print()
    return printed
