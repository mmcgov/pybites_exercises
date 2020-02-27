from datetime import datetime, timedelta

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    final_dates = list()
    for i in range(1, 11):
        if i%4==0:
            factor = i/4
            yield PYBITES_BORN + timedelta(days=365*factor)
        else:
            yield PYBITES_BORN + timedelta(days=100*i)

