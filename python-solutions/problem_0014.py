import utilities

print max(((len(list(utilities.collatz(x)))), x) for x in range(1, 1000000))
