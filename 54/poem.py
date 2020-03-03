INDENTS = 4
indent_check = 1


def print_hanging_indents(poem):
    final_poem = ['\n']
    clean_poem = poem.split('\n')
    for line in clean_poem:
        line = line.strip()
        if len(line) == 0:
            indent_check = 0
        elif (len(line) > 0) and (indent_check == 0):
            final_poem.append(line)
            indent_check = 1
        elif (len(line) > 0) and (indent_check == 1):
            final_poem.append(' '*4+line)
            indent_check = 1
    print(final_poem)
