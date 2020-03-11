def sort_words_case_insensitively(words):
    """Sort the provided word list ignoring case, and numbers last
       (1995, 19ab = numbers / Happy, happy4you = strings, hence for
        numbers you only need to check the first char of the word)
    """
    numbers = list()
    strings = list()
    for word in words:
        if word[0].isdigit():
            numbers.append(word)
        else:
            strings.append(word)

    numbers = sorted(numbers)
    strings = sorted(strings, key=str.casefold)
    return strings+numbers
