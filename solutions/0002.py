from utilities import fibonacci

print sum(x for x in fibonacci(4000000) if not x % 2)
