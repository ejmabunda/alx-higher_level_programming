#!/usr/bin/python3
def search_replace(my_list, search, replace):
    my_list = my_list.copy()
    for elem in my_list:
        if elem == search:
            my_list[my_list.index(elem)] = replace

    return my_list
