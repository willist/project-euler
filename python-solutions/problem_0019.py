from pprint import pprint
from itertools import cycle, takewhile, ifilter, dropwhile

def day_generator():
    def is_leap_year(year):
        # weed out years which can't possibly be leap years
        if year % 4:
            return False

        if not year % 100 and year % 400:
            return False

        return True

    days_in_month = {
        1: 31, 2: 28, 3: 31, 4:30, 5:31, 6:30, 
        7:31, 8:31, 9:30, 10: 31, 11: 30, 12:31
    }

    days = cycle(["Monday", "Tuesday", "Wednesday", "Thursday", 
        "Friday", "Saturday", "Sunday", ])

    month, day, year = 1, 1, 1900

    while True:
        yield year, month, day, next(days)

        day += 1
        if day > days_in_month[month]:
            day = 1
            month += 1

        if month > 12:
            month = 1
            year += 1
            days_in_month[2] = 29 if is_leap_year(year) else 28

def is_first_sunday(date):
    year, month, day, name = date
    return name == "Sunday" and day == 1

def in_date_range(start, end):
    def inner(date):
        return start <= date <=end
    return inner

in_twentieth_century = in_date_range((1901, 1, 1), (2000,12,31))

days = day_generator()
days = dropwhile(lambda x: not in_twentieth_century(x), days)
days = takewhile(in_twentieth_century, days)
print len(filter(is_first_sunday, days))
