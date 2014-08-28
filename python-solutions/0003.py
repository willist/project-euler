"""
Link: https://projecteuler.net/problem=3
Description:
    The prime factors of 13195 are 5, 7, 13 and 29.

    What is the largest prime factor of the number 600851475143 ?
"""
from utilities import prime_factors

num = 600851475143
print max(prime_factors(num))
