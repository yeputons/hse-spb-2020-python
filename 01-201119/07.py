#!/usr/bin/env python3

l = [1, 2, 3, 10, 5, 20]
for x in l:
    if x % 10 == 0:
        print(f'Hurray {x}')
        break
else:
    print('Oops')

s = f'{2 + 2}'
assert s == '4'

i = 0
while i < 10:
    print(i)
    i += 1
