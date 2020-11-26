#!/usr/bin/env python3
a = [1, 2, 3]
b = [10, 20, 30, 40, 50]

z = zip(a, b)
#it = iter(z)
#print(next(it))
#print(next(it))
#print(next(it))
#print(next(it))
print(list(z))

for x, y in zip(a, b):
    print(x + y)

# Раздел 3.2, шаг 3-4.
for x, y in zip(a, a[1:]):
    print(x, y)
