import itertools
import utilities


def has500factors(num):
    factors = list(utilities.factors(num))
    return len(factors) > 500

over500 = itertools.ifilter(has500factors, utilities.triangle_numbers())
print list(itertools.islice(over500, 1))
