def find_number_pairs(numbers, N=10):
    results = list()
    numbers.sort()
    for num in numbers[:-1]:
        i=numbers.index(num)+1
        for n in numbers[i:]:
            if num+n == N:
                results.append((num,n))
                i+=1
            else:
                i+=1
    return results

