import math
import numpy

def factors(num):
    sqrt_num = int(math.sqrt(num))

    poss_left_factors = numpy.arange(1, sqrt_num + 1)

    facts = set()
    for poss_factor in poss_left_factors:
        if not num % poss_factor:
            facts.add(poss_factor)
            facts.add(num / poss_factor)

    return sorted(list(facts))

def prime_factors(num):
    facts = []
    if num >= 1:
        facts.append(1)
    for item in factors(num):
        all_factors = factors(item)
        if len(all_factors) == 2:
            facts.append(item)

    return facts

def fibonacci(cap=None):
    a = 0
    yield a
    b = 1
    while True:
       yield b
       a, b = b, a + b
       if b > cap:
           break
 
def is_palindrome(number):
    return str(number) == str(number)[::-1]


