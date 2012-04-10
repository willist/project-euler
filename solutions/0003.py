print int('600851475143')
import numpy
import math
def prime(upto=100):
    """Stolen from http://rebrained.com/?p=458
    """
    return filter(lambda num: (num % numpy.arange(2,1+int(math.sqrt(num)))).all(), xrange(2,upto+1))

print max(prime(600851475143))
