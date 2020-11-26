#!/usr/bin/env python3
print(list(enumerate("abcde")))
for i, ch in enumerate('abcde'):
    print(f's[{i}] = {ch}')


print(all([10, 20, 30]))
print(all([10, 2, None]))
print(any([10, 2, None]))
print(any([0.0, None]))
