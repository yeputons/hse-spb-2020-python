#!/usr/bin/env python3
a = [0] * 10
a[2] += 5
print(a)

b = [[0] * 10 for _ in range(10)]
b[0][2] += 5
print(b)
