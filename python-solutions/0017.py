from utilities import big_number_iterator

def num_to_words(num):
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
        #10: 'ten',
        #11: 'eleven',
        #12: 'twelve',
        #13: 'thirteen',
        #14: 'fourteen',
        #15: 'fifteen',
        #16: 'sixteen',
        #17: 'seventeen',
        #18: 'eighteen',
        #19: 'nineteen',
    }

    if num in mapping:
        return mapping[num]
    else:
        return 'unknown'

for piece in reversed(big_number_iterator()):
    print num_to_words(piece)
