#!/usr/bin/env python3

a = {
    'key': 1 + 1,
    (1, 2): 'value'
}
print(a)
print(a['key'])
print(a[(1, 2)])

a['botva'] = 'world'
print(a)

b = a
print(type(a))

print({x: x ** 2 for x in range(10)})

l = [1, 2, 3]
l2 = list(l)
l3 = l[:]
