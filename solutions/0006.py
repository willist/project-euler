import math

def sum_of_squares(num):
    return sum(x*x for x in xrange(1, num + 1))

def square_of_sums(num):
    return math.pow(sum(xrange(1, num + 1)), 2)

def diff(num):
    a = sum_of_squares(num)
    print a
    b = square_of_sums(num)
    print b
    return abs(a - b)

print diff(100)
