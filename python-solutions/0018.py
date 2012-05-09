"""
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23     
"""
from functools import total_ordering

@total_ordering
class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value

    def __repr__(self):
        lvalue = self.left.value if self.left is not None else 'None'
        rvalue = self.right.value if self.right is not None else 'None'
        return "<Node (%s) [%s, %s]>" % (self.value, lvalue, rvalue)

def parse_triangle():
    def map_nodes(a, b):
        for index, item in enumerate(a):
            item.left = b[index]
            item.right = b[index + 1]

    head = None
    rows = [row.strip() for row in __doc__.split('\n') if row]
    previous = []
    for row in rows:
        current = [Node(int(item)) for item in row.split(' ') if item]
        map_nodes(previous, current)
        previous = current
        if head is None:
            head = current[0]

    return head

def greedy(head):
    print head
    big_kid = max(head.left, head.right)
    if big_kid is None:
        return head.value

    return head.value + greedy(big_kid)

print greedy(parse_triangle())
