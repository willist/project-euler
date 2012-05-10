from itertools import count, takewhile, product, ifilter
from utilities import is_abundant

def abundant_generator():
    for item in count(): 
        if is_abundant(item):
            yield item

cutoff = lambda x: x <= 28123
abundants = list(takewhile(cutoff, abundant_generator()))
two_abundants = (x+y for x,y in product(abundants, abundants))
two_abundants = ifilter(cutoff, two_abundants)

all_ints = set(range(0, 28123))
no_two_abundants = all_ints - set(two_abundants)
print sum(no_two_abundants)
