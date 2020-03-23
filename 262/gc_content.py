from collections import Counter


def calculate_gc_content(sequence):
    """
    Receives a DNA sequence (A, G, C, or T)
    Returns the percentage of GC content (rounded to the last two digits)
    """
    seq = sequence.lower()
    count = Counter(seq)
    return round(100*(count['g']+count['c'])/(count['a']
                 + count['g']+count['c']+count['t']), 2)
