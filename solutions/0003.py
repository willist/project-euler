a = 600851475143

import math
import numpy

def factors(num):
    sqrt_num = int(math.sqrt(num))

    poss_left_factors = numpy.array([1,2] + list(xrange(3, sqrt_num , 2)))

    facts = []
    for poss_factor in poss_left_factors:
        if not num % poss_factor:
            facts.append(poss_factor)
            facts.append(num / poss_factor)

    return sorted(facts)

def prime_factors(num):
    facts = []
    for item in factors(num):
        all_factors = factors(item)
        print item, all_factors
        if len(all_factors) == 2:
            facts.append(item)

    return facts

print prime_factors(a)
