#!/usr/bin/env python3
import itertools

def gen():
    i = 1
    while i ** 2 <= 100:
        yield i
        i += 1

# print(itertools.len(gen()))
# print(len(gen()))

# https://docs.python.org/3/library/itertools.html
print(list(
    itertools.chain(gen(), gen())
))
print(list(itertools.zip_longest([1, 2, 3], [4, 5, 6, 7, 8])))
