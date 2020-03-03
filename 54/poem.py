INDENTS = 4
indent_check = 1


def print_hanging_indents(poem):
    clean_poem = poem.split('\n')
    for line in clean_poem:
        line = line.strip()
        if len(line) == 0:
            indent_check = 0
        if (len(line) > 0) and (indent_check == 0):
            print(line)
            indent_check = 1
        if (len(line) > 0) and (indent_check == 1):
            print(' '*4, line)
            indent_check = 1
