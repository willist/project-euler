def fib(cap=None):
    a = 0
    yield a
    b = 1
    while True:
       yield b
       a, b = b, a + b
       if b > cap:
           break
 
print sum(x for x in fib(4000000) if not x % 2)
