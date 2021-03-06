import math


def round_even(number):
    """Takes a number and returns it rounded even"""
    if number > 1 and math.ceil(number) % 2 == 0:
        return math.ceil(number)
    else:
        return math.floor(number)