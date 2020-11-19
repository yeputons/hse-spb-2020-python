#!/usr/bin/env python3

def bar():
    print(x)

def foo():
    if True:
        x = 4
    else:
        y = 5
    print(i, x)
    bar()

for i in range(10):
    print(i)
print(f'i={i}')

foo()
