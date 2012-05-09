import math
import itertools

def factors(num):
    sqrt_num = int(math.sqrt(num))

    possible_left_factors = xrange(1, sqrt_num + 1)

    for possible_factor in possible_left_factors:
        if not num % possible_factor:
            yield possible_factor
            if possible_factor != (num / possible_factor):
                yield num / possible_factor

def prime_factors(num):
    if num >= 1:
        yield 1
    for item in factors(num):
        if is_prime(item):
            yield item

def prime_generator():
    for num in itertools.count():
        if is_prime(num):
            yield num

def nth_prime(n):
    if n <= 0:
        raise ValueError("n must be 1 or greator")
    for index, item in enumerate(prime_generator(), 1):
        if index == n:
            print item
            break

def fibonacci(cap=None):
    a = 0
    yield a
    b = 1
    while True:
       yield b
       a, b = b, a + b
       if b > cap:
           break

def triangle_numbers():
    value = 0
    for num in itertools.count(1):
        value += num
        yield value

def parse_grid(grid):
    """Parse a grid into a two dimensional list.
    """
    return [[int(item) for item in row.split(' ') if item != '']
            for row in grid.split('\n') if row.strip()]

def grid_vertical(grid):
    y_len = len(grid)
    x_len = len(grid[0])

    return [[grid[x][y] for x in range(x_len)] for y in range(y_len)]

def grid_diagonal_left(grid):
    rotated_grid = []
    for pivot, row in enumerate(grid):
        rotated_grid.append(row[pivot:] + row[:pivot])

    vertical_rotated_grid = grid_vertical(rotated_grid)

    diagonals = []
    for pivot, row in enumerate(vertical_rotated_grid):
        pivot = len(row) - pivot
        diagonals.append(row[:pivot])
        diagonals.append(row[pivot:])
    return filter(None, diagonals)

def grid_diagonal_right(grid):
    rotated_grid = []
    for pivot, row in enumerate(grid):
        pivot = len(row) - pivot - 1
        rotated_grid.append(row[pivot:] + row[:pivot])

    vertical_rotated_grid = grid_vertical(rotated_grid)

    diagonals = []
    for pivot, row in enumerate(vertical_rotated_grid):
        diagonals.append(row[:pivot])
        diagonals.append(row[pivot:])
    return filter(None, diagonals)

def product(*items):
    return reduce(lambda a,b: a*b, items)

def chunker(iterable, chunk_size):
    """Returns overlapping chunks of an iterable, sliding the window by 1
    each step.
    chunker([1,2,3,4,5,6], 3) --> [1,2,3] [2,3,4] [3,4,5] [4,5,6]
    """
    iterable = iter(iterable)
    chunk = []
    while len(chunk) < chunk_size:
        chunk.append(next(iterable))
    yield chunk
    for item in iterable:
        chunk = chunk[1:] + [item]
        yield chunk

def max_product(grid, adjacent_size):
    chunked_rows = (chunker(row, adjacent_size) for row in grid)
    chunked_products = (product(*chunk)
        for row in chunked_rows for chunk in row)
    return max(chunked_products)

def is_prime(num):
    index = -1
    for index, item in enumerate(factors(num)):
        if index == 2:
            break
    return index == 1
 
def is_palindrome(number):
    return str(number) == str(number)[::-1]

def collatz(number):
    yield number
    while number != 1:
        if number % 2 == 1:
            number = 3 * number + 1
        else:
            number /= 2
        yield number

def pascals_triangle():
    def next_triangle_piece(step):
        #import pdb; pdb.set_trace()
        new_step = []
        previous = None
        for current in step:
            if previous is not None:
                new_step.append(previous + current)
            previous = current
        return [1] + new_step + [1]

    current_step = [1]
    while True:
        yield current_step
        current_step = next_triangle_piece(current_step)

def nth(iterable, n, default=None):
    return next(itertools.islice(iterable, n, None), default)

def big_number_iterator(number):
    if number == 0:
        yield number
    while number:
        yield number % 10
        number = int(number / 10)

