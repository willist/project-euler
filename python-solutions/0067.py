from triangle_utilities import parse_triangle, calculate_weights

print calculate_weights(parse_triangle(open('triangle.txt').read()))
#print greedy(parse_triangle(__doc__))
