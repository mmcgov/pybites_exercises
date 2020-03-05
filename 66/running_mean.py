import itertools

def running_mean(sequence):
    """Calculate the running mean of the sequence passed in,
       returns a sequence of same length with the averages.
       You can assume all items in sequence are numeric."""
    sums = itertools.accumulate(sequence)
    yield [int(accum/i) if float(accum/i).is_integer() else round(accum/i, 2)  for i, accum in enumerate(sums, start=1)]
