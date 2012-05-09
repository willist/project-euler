import string

mapping = {
    0: 'zero',
    1: 'one',
    2: 'two',
    3: 'three',
    4: 'four',
    5: 'five',
    6: 'six',
    7: 'seven',
    8: 'eight',
    9: 'nine',
    10: 'ten',
    11: 'eleven',
    12: 'twelve',
    13: 'thirteen',
    14: 'fourteen',
    15: 'fifteen',
    16: 'sixteen',
    17: 'seventeen',
    18: 'eighteen',
    19: 'nineteen',
    20: 'twenty',
    30: 'thirty',
    40: 'forty',
    50: 'fifty',
    60: 'sixty',
    70: 'seventy',
    80: 'eighty',
    90: 'ninety',
}

def num_to_words(num):
    if num in mapping:
        return mapping[num]

    s = ""
    million = num / 1000000
    if million:
        s += "%s million" % num_to_words(million)
    num = num % 1000000

    thousand = num / 1000
    if thousand:
        if s: s += " "
        s += "%s thousand" % num_to_words(thousand)
    num = num % 1000

    hundred = num / 100
    if hundred:
        if s: s += " "
        s += "%s hundred" % num_to_words(hundred)
    num = num % 100

    ones = num % 10
    tens = num - ones
    if num:
        if s: s += " and "
        if 0 <= num <= 20:
            s += "%s" % num_to_words(num)
        else:
            s += "%s" % num_to_words(tens)
            if ones:
                s += "-%s" % num_to_words(ones)

    return s
        

def count_letters(s):
    count = 0
    for item in str(s):
        if item in string.ascii_lowercase:
            count += 1
    return count

print sum(count_letters(num_to_words(x)) for x in range(1, 1001))
