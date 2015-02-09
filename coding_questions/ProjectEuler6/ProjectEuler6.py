def sumSquares():
    sum_total = 0
    sq_total = 0

    for x in xrange(1, 101):
        sq_total+= (x*x)
        sum_total+= x

    return (sum_total * sum_total) - sq_total

print sumSquares()

