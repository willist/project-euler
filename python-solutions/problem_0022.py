import string

def alphabetical_value(s):
    ref = {letter: index
        for index, letter in enumerate(string.ascii_lowercase, 1)}
    s = s.lower()
    return sum(ref[x] for x in s)

names = (item.replace('"', '') for item in open('names.txt').read().split(','))

print sum(index*alphabetical_value(name) 
    for index, name in enumerate(sorted(names), 1))
