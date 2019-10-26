"""
Link: https://projecteuler.net/problem=4
Description:
    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 x 99.

    Find the largest palindrome made from the product of two 3-digit numbers.
"""
from utilities import is_palindrome


def solution():
    palindromes = [(x * y, x, y)
        for x in range(1000)
        for y in range(1000)
        if is_palindrome(x * y)]

    return max(palindromes)[0]


if __name__ == "__main__":
    print solution()
