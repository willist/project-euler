from utilities import factors

def divisible_by_range(lower=1, upper=10):
    num = upper
    while True:
        result = factors(num)
        if set(range(lower,upper + 1)) < set(result):
            break
        num +=  1

    return num

print divisible_by_range(1,10)
print divisible_by_range(1,20)
