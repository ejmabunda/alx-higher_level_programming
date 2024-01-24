#!/usr/bin/python3
def best_score(a_dictionary):
    if a_dictionary is None:
        return None

    best_student = ""
    biggest = 0

    for student, score in a_dictionary.items():
        if score > biggest:
            best_student = student
            biggest = score

    return best_student
