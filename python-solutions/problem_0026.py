"""
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

    1/2 =   0.5
    1/3 =   0.(3)
    1/4 =   0.25
    1/5 =   0.2
    1/6 =   0.1(6)
    1/7 =   0.(142857)
    1/8 =   0.125
    1/9 =   0.(1)
    1/10    =   0.1
    Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

    Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
"""
import re

capture = re.compile('\d*?(?P<rep>\d+?)(?P=rep){2}')

def find_repeat(num):
    value = ''
    remainder = 10
    remainer_set = set()
    remainder_list = []

    value += str(remainder / num)
    remainder = remainder % num * 10

    while True:
        value += str(remainder * 10 / num)
        remainder = remainder * 10 % num
        yield value.lstrip('0')


winner = 0
winner_size = 0

for i in range(1,1001):
    divider = fun(i)
    remainders_list = []
    remainders_set = set()

    while True:
        curr = next(divider)
        y = capture.search(curr)
        if y:
            repeat = y.group('rep')
            repeat_size = len(repeat)
            if repeat_size > winner_size:
                winner_size = repeat_size
                winner = i

            print i, repeat_size, repeat
            break

print winner, winner_size
