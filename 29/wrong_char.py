def get_index_different_char(chars):
    alpha = list()
    non_alpha = list()
    for x in chars:
        if str(x).isalnum():
            alpha.append(chars.index(x))
        else:
            non_alpha.append(chars.index(x))

    if len(alpha) == 1:
        return alpha[0]
    else:
        return non_alpha[0]

