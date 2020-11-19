#!/usr/bin/env python3
l = [1, 2, 3, 4]
it = iter(l)
print(it)
print(next(it))
print(next(it))
print(next(it))
print(next(it))

try:
    print(next(it))
except StopIteration:
    print('stopped')

r = range(10 ** 9)
print(len(r))
print(r[100])

x = map(str, [1, 2, 3])
print(list(x))
print(list(x))

gen = (x * x for x in range(10 ** 9))
print(next(gen))
print(next(gen))
#print(len(y))
