def wc(file_):
    """Takes an absolute file path/name, calculates the number of
       lines/words/chars, and returns a string of these numbers + file, e.g.:
       3 12 60 /tmp/somefile
       (both tabs and spaces are allowed as separator)"""
    with open(file_) as f:
        content = f.read()
        num_lines = len(content.splitlines())
        num_words = len(content.split())
        num_chars = len(content)
        numbers = f'{num_lines}\t{num_words}\t{num_chars}'
        return f'{numbers} {file_}'

if __name__ == '__main__':
    # make it work from cli like original unix wc
    import sys
    print(wc(sys.argv[1]))
