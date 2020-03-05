import itertools


def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    sums = itertools.accumulate(sequence)
    for i, accum in enumerate(sums, start=1):
        if float(accum/i).is_integer():
            yield int(accum/i)
        else:
            yield round(accum/i, 2)
