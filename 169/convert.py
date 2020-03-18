def convert(value: float, fmt: str) -> float:
    """Converts the value to the designated format.

    :param value: The value to be converted must be numeric or raise a TypeError
    :param fmt: String indicating format to convert to
    :return: Float rounded to 4 decimal places after conversion
    """
    inchtocm = 2.54

    if isinstance(value, int) or isinstance(value, float):
        value = value
    else:
        raise TypeError

    if 'cm' in fmt.lower():
        return round(value*inchtocm, 4)
    elif 'in' in fmt.lower():
        return round(value/inchtocm, 4)
    else:
        raise ValueError
