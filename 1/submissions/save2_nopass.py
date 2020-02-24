def sum_numbers(numbers=None):
    if numbers:
        if numbers==[]:
            return None
        else:
            return sum(list(numbers))
    else:
        return sum(range(1,101))
        

sum_numbers()