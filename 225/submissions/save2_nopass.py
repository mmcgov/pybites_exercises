PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
    return [c.upper() if c.islower() else c.lower() for c in text if c.lower() in PYBITES]
        