def fizzbuzz(num):
    result = num
    if num % 3 == 0:
        result = 'Fizz'
        break
    elif num % 5 == 0:
        result = 'Buzz'
        break
    else:
        result == num
    return result