from utilities import is_palindrome

palindromes = [(x*y, x, y)
    for x in range(1000) 
    for y in range(1000) 
    if is_palindrome(x*y)]

print sorted(palindromes)
