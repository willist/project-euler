from itertools import permutations
from utilities import nth

print ''.join(nth(permutations('0123456789'), 999999))
