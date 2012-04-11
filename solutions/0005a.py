import utilities

def divisible_by_range(lower=1, upper=10):
    pfacts = set()
    for num in range(lower, upper + 1):
        for fact in utilities.factors(num):
            pfacts.add(fact)

    print pfacts


divisible_by_range(upper=20)
