IGNORE_CHAR = 'b'
QUIT_CHAR = 'q'
MAX_NAMES = 5


def filter_names(names):
    results = list()
    for name in names:
        if name[0] == IGNORE_CHAR:
            continue
        elif any(char.isdigit() for char in name):
            continue
        elif name[0] == QUIT_CHAR:
            break
        elif len(results) < MAX_NAMES:
            results.append(name)
        else:
            print('break')
            break
    return results
