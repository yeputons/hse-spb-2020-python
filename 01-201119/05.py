#!/usr/bin/env python3

l1 = [1, 2, 3, 4]
l2 = [10, 100]
print([x * y for x in l1 for y in l2 if x % 2 == 0])
# map, filter

print(' '.join([str(x) for x in l1]))
