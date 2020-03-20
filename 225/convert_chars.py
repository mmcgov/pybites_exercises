PYBITES = "pybites"


def convert_pybites_chars(text):
    """Swap case all characters in the word pybites for the given text.
       Return the resulting string."""
 #   return [c.upper() if c.islower() else c.lower() for c in text if c.lower() in PYBITES]
    for char in text:
        if (char.lower() in PYBITES) and (char.islower()):
            text = text.replace(char, char.upper())
        elif (char.lower() in PYBITES) and (char.isupper()):
            text = text.replace(char, char.lower())
    return text
