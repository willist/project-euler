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

def parse_triangle(s):
    def map_nodes(a, b):
        for index, item in enumerate(a):
            item.left = b[index]
            item.right = b[index + 1]

    head = None
    rows = [row.strip() for row in s.split('\n') if row]
    previous = []
    for row in rows:
        current = [Node(int(item)) for item in row.split(' ') if item]
        map_nodes(previous, current)
        previous = current
        if head is None:
            head = current[0]

    return head

def calculate_weights(head):
    if head is None:
        return 0

    if hasattr(head.left, 'weight'):
        left_weight = head.left.weight
    else:
        left_weight = calculate_weights(head.left)

    if hasattr(head.right, 'weight'):
        right_weight = head.right.weight
    else:
        right_weight = calculate_weights(head.right)

    head.weight = head.value + max(left_weight, right_weight)
    return head.weight
