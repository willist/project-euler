import itertools
import utilities

rows = itertools.ifilter(lambda x: len(x) % 2 == 1, 
    utilities.pascals_triangle())

for index, item in enumerate(itertools.islice(rows, 30)):
    print index, item[len(item) / 2]
