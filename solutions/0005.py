def divisible_by_range(lower=1, upper=10):
    num = upper
    while True:
        #print num, 
        if all(not (num % x) for x in xrange(lower, upper + 1)):
            break
        num += 1
    
    print '=' * 79
    print num
    raw_input()

divisible_by_range(1,10)
divisible_by_range(11,20)
