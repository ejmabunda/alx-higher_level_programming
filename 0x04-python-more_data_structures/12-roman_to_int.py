#!/usr/bin/python3
def roman_to_int(roman_string):
    # handle bad input
    if roman_string is None or type(roman_string) is not str:
        return 0

    # reference to a few common/reused numerals
    table = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }

    answer = 0  # will store final resuls
    skip = 0  # number of times I is skipped
    previous = ""  # reference to the previous letter

    for letter in roman_string:
        if letter == "I":
            skip += 1
        # when X is encountered, subtract the number of I's
        # that appear before X
        elif letter == "X":
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
