from utilities import num_to_words, count_letters

print sum(count_letters(num_to_words(x)) for x in range(1, 1001))
