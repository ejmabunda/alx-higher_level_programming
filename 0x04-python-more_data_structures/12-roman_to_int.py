#!/usr/bin/python3
def roman_to_int(roman_string):
    # handle bad input
    if roman_string is None or type(roman_string) is not str:
        return 0
    if len(roman_string) == 0:
        return 0

    # reference to a few common/reused numerals, up to 1000
    table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    answer = 0  # will store the final result
    skip = 0  # number of times I is skipped
    previous = ""  # reference to the previous letter

    for letter in roman_string:
        # count I's as a group
        if letter == "I":
            skip += 1
        # when X or V is encountered, subtract the number of I's
        # that appeared before X or V
        elif letter == "X":
            if previous == "I":
                answer = answer + table[letter] - skip
            else:
                answer = answer + table[letter]
            skip = 0

        elif letter == "V":
            if previous == "I":
                answer = answer + table[letter] - skip
            else:
                answer = answer + table[letter]
            skip = 0

        else:
            answer = answer + table[letter] + skip
            skip = 0

        previous = letter

    # add trailing I's
    answer += skip

    return answer
