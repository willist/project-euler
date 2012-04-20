import utilities
import itertools

print sum(
    itertools.takewhile(lambda x: x < 2000000, utilities.prime_generator()))
