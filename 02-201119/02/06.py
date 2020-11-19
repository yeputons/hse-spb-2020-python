#!/usr/bin/env python

def foo(a, b, c, d):
    print(a, b, c, d)

x = [1, 2]
y = [3, 4]
foo(*x, *y)

d = {'a': 50, 'd': 40}
foo(**d, b=1, c=4)
