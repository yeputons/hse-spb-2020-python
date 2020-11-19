#!/usr/bin/env python3
my_dict = {}
#def sum(a, b):
def sum(a: int, b: int) -> int:
    # No overloads
    print(type(a), isinstance(a, int))
    return a + b

my_dict['wtf'] = sum
print(my_dict['wtf'](1, 2))
print(sum([1, 2, 3, 4]))  # mypy 09.py
