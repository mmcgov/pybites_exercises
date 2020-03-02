def fizzbuzz(num):
    result = num
    if num % 3 == 0:
        result = 'Fizz'
    elif num % 5 == 0:
        result = 'Buzz'
    elif num % 3 == 0 and num % 5 == 0:
        result = 'Fizz Buzz'
    else:
        result == num
    return result