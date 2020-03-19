def countdown():
    """Write a generator that counts from 100 to 1"""
    n=100
    while n>1:
        yield n
        n -= 1