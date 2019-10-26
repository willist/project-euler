from itertools import ifilter
from utilities import is_amicable

print sum(ifilter(is_amicable, range(0, 10001)))
