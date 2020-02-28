def countdown_for(start=10):
    for i in reversed(range(1, start + 1)):
        print(i)
    print('time is up')


def countdown_recursive(start=10):
    while start>=1:
        print(start)
        start = start - 1
    print('time is up')
