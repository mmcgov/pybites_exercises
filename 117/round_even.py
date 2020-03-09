import math


def round_even(number):
    """Takes a number and returns it rounded even"""
    dec = number - int(number)
    if dec > 0.5:
        return math.ceil(number)
    elif number > 1 and dec == 0.5 and math.ceil(number) % 2 == 0:
        return math.ceil(number)
    else:
        return math.floor(number)
