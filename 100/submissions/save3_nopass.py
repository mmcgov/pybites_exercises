def tail(filepath, n):
    """Similate Unix' tail -n, read in filepath, parse it into a list,
       strip newlines and return a list of the last n lines"""
    with open(filepath) as f:
        txt = f.read()
        lines = txt.splitlines()
        return lines[-2:] 