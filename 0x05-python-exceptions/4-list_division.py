#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    new_list = []
    for ix in range(list_length):
        try:
            result = my_list_1[ix] / my_list_2[ix]
        except IndexError:
            result = 0
            print("out of range")
        except ZeroDivisionError:
            result = 0
        except TypeError:
            result = 0
            print("wrong type")
        finally:
            new_list.append(result)

    return new_list
