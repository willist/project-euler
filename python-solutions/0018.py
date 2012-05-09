"""
     10
   12  14
 16  18  20
"""

class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

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

print parse_triangle()
