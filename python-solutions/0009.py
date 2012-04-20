def triplets(num):
    for a in range(1, num + 1):
        for b in range(1, num - a + a):
            c = num - a - b
            yield a, b, c

def is_pythagorean(a, b, c):
    return (a*a) + (b*b) == (c*c)

for a,b,c in triplets(1000):
    if is_pythagorean(a,b,c):
        print a,b,c,a*b*c
