import itertools
import utilities


def has500factors(num):
    factors = list(utilities.factors(num))
    print factors
    return len(factors) > 500

print list(utilities.factors(28))
#over500 = itertools.takewhile(has500factors, utilities.triangle_numbers())
#print list(itertools.islice(over500, 1))
