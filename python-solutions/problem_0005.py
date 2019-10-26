"""
Link: https://projecteuler.net/problem=5
Description:
    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of the
    numbers from 1 to 20?
"""


def divisible_by_range(num, lower=1, upper=10):
    return all(not (num % x) for x in xrange(lower, upper + 1))


def solution():
    """
    1. Start at product of range
    2. Divide by each number until the result no longer satisfies the criteria

    Result is our answer.
    """
    low = 1
    high = 20

    numbers = range(low, high + 1)

    product = lambda x, y: x * y
    start = reduce(product, numbers)

    prev, curr = start, start
    for i in numbers:
        while divisible_by_range(curr, low, high):
            prev, curr = curr, curr / i
            if prev == curr:
                break
        curr = prev

    return curr

print solution()
