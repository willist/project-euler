import math

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


