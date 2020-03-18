IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def _name_has_digit(name):
    return any(c.isdigit() for c in name)


def filter_names(names):
    count = 0
    for name in names:
        if name.startswith(IGNORE_CHAR) or _name_has_digit(name):
            continue
        elif name.startswith(QUIT_CHAR) or count >= MAX_NAMES:
            break
        count += 1
        yield name
