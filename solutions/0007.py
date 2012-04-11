import itertools
import utilities

def prime_generator():
    for num in itertools.count():
        if utilities.is_prime(num):
            yield num

def nth_prime(n):
    if n <= 0:
        raise ValueError("n must be 1 or greator")
    for index, item in enumerate(prime_generator(), 1):
        if index == n:
            print item
            break

nth_prime(10001)
