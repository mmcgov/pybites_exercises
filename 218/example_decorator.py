#!usr/bin/python

from functools import wraps

def multiply(func):
    @wraps(func)
    def wrapped(*args, **kwargs):
        return 5*func(*args, **kwargs)
    return wrapped




@multiply
@multiply
def add(number):
    return number


