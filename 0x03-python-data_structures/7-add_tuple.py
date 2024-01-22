#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    # try to add firsts
    try:
        first = tuple_a[0] + tuple_b[0]
    except:
        try:
            first = tuple_a[0] + 0
        except:
            first = 0 + tuple_b[0]
    
    # try to add seconds
    try:
        second = tuple_a[1] + tuple_b[1]
    except:
        try:
            second = tuple_a[1] + 0
        except:
            second = 0 + tuple_b[1]
    return (first, second)
