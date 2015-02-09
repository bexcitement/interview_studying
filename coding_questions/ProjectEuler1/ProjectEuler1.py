def sumMultiples():
    total = 0
    for num in xrange(1000):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total 

print sumMultiples()
