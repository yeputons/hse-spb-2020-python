#!/usr/bin/env python3
import sys

def foo(a, b):
    print(a, b)
foo(b=10, a=20)

def bar(a, b, c=[], d=[], e=[], f=[]):
    print(a, b, c, d, e, f)
bar(10, 20, e=40)

print('hello', 1, 2, sep=' ', end='')
sys.stdout.write('hello')
print('world')

def baz(a, b, c=[]):
    c.append(100)
    return c
print(baz(10, 20))
print(baz(10, 20))
print(baz(10, 20))

def baz2(a, b, c=None):
    #c = c or []  # falsy: [], (), {}, "", 0, 0.0, False, None
    if c is None:  # if c is not None
        c = []
    c.append(100)
    return c

print(baz2(10, 20))
print(baz2(10, 20))
print(baz2(10, 20))
