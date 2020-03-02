def fizzbuzz(num):
    result = num
    if num % 3 == 0 and num % 5 == 0:
        result = 'Fizz Buzz'
        continue
    if num % 3 == 0:
        result = 'Fizz'
        continue
    elif num % 5 == 0:
        result = 'Buzz'
        continue
    else:
        result == num
    return result