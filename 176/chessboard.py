WHITE, BLACK = ' ', '#'


def create_chessboard(size=8):
    """Create a chessboard with of the size passed in.
       Don't return anything, print the output to stdout"""
    odd = 0
    length = int(size/2)
    for i in range(size+1):
        if odd == 0:
            print((WHITE+BLACK)*length)
            odd = 1
        if odd == 1:
            print((BLACK+WHITE)*length)
            odd = 0
