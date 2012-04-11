import utilities

def divisible_by_range(lower=1, upper=10):
    pfacts = set()
    for num in range(lower, upper + 1):
        for fact in utilities.prime_factors(num):
            pfacts.add(fact)

    return reduce(lambda x,y: x*y, pfacts)

print divisible_by_range(upper=20)
