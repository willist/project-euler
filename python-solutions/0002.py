from itertools import takewhile

from utilities import fibonacci


def is_less_than(cutoff):
    def inner(num):
        return num < cutoff
    return inner


print sum(x for x in takewhile(is_less_than(4000000), fibonacci()) if not x % 2)
