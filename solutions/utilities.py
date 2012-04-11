import math
import itertools

def factors(num):
    sqrt_num = int(math.sqrt(num))

    possible_left_factors = xrange(1, sqrt_num + 1)

    for possible_factor in possible_left_factors:
        if not num % possible_factor:
            yield possible_factor
            if possible_factor != (num / possible_factor):
                yield num / possible_factor

def prime_factors(num):
    if num >= 1:
        yield 1
    for item in factors(num):
        if is_prime(item):
            yield item

def prime_generator():
    for num in itertools.count():
        if is_prime(num):
            yield num

def nth_prime(n):
    if n <= 0:
        raise ValueError("n must be 1 or greator")
    for index, item in enumerate(prime_generator(), 1):
        if index == n:
            print item
            break

def fibonacci(cap=None):
    a = 0
    yield a
    b = 1
    while True:
       yield b
       a, b = b, a + b
       if b > cap:
           break

def is_prime(num):
    index = -1
    for index, item in enumerate(factors(num)):
        if index == 2:
            break
    return index == 1
 
def is_palindrome(number):
    return str(number) == str(number)[::-1]


