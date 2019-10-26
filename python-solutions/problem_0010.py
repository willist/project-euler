import utilities
import itertools

def solution():
    return sum(
        itertools.takewhile(lambda x: x < 2000000, utilities.prime_generator()))
