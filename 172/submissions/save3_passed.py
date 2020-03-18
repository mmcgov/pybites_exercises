from functools import partial

# create 2 partials:
# - 'rounder_int' rounds to int (0 places)
# - 'rounder_detailed' rounds to 4 places

def round_new(number, places):
    return round(number, places)
    

rounder_int = partial(round_new, places=0)
rounder_detailed =  partial(round_new, places=4)