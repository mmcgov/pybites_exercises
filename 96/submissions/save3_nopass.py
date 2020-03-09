def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    lines = 0
    words = 0
    characters = 0
    with open('file_', 'r') as f:
        text = f.read()
        for line in text.splitlines(True):
            wordslist = line.split()
            lines = lines + 1
            words = words + len(wordslist)
            characters = characters + len(line)
    return (f"{lines}+' '*5+{words}+' '*5+{characters}+' '*5")

if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))