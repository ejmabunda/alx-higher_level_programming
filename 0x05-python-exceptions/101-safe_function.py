#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        return fct(*args)

    except ZeroDivisionError as e:
        print(f"Exception: {e}", file=sys.stderr)
        return None

    except IndexError as ie:
        print(f"Exception: {ie}", file=sys.stderr)
        return None
