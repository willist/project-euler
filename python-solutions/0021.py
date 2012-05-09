from itertools import ifilter
from utilities import factors

class AmicableNumberFinder(object):
    def __init__(self):
        self.cache = {}

    def __call__(self, num):
        a = self.amicable(num)
        b = self.amicable(a)
        return a != num and num == b

    def amicable(self, num):
        if num not in self.cache:
            self.cache[num] = sum(factors(num)) - num

        return self.cache[num]


is_amicable = AmicableNumberFinder()
print sum(ifilter(is_amicable, range(0, 10001)))
