#!/usr/bin/env python

x = (10,)
print(len(x))
print(x[0])
x = (
    10,
    20,
    30,  # Mind the trailing comma: better diff.
)
print(x)
y = [
    10,
    20,
    30,
]
print(y)
