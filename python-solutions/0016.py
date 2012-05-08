def big_number_iterator(number):
    while number:
        yield number % 10
        number = int(number / 10)

print sum(big_number_iterator(pow(2, 1000)))
