VOWELS = 'aeiou'
PYTHON = 'python'


def contains_only_vowels(input_str):
    """Receives input string and checks if all chars are
       VOWELS. Match is case insensitive."""
    result = ''.join([letter for letter in input_str if letter.lower() in VOWELS])
    return result == input_str


def contains_any_py_chars(input_str):
    """Receives input string and checks if any of the PYTHON
       chars are in it. Match is case insensitive."""
    result = ''.join([letter for letter in input_str if letter.lower() in PYTHON])
    return result == input_str


def contains_digits(input_str):
    """Receives input string and checks if it contains
       one or more digits."""
    return any(i.isdigit() for i in input_str)
