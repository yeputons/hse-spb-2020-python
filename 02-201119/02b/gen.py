#!/usr/bin/env python3
from random import *

#MAXN = MAXQ = int(3e5)
n = q = int(3e5)
MAXV = int(1e9) - 1

#n = randint(1, MAXN)

print(n)
print(" ".join(str(randint(0, MAXV)) for _ in range(n)))

#q=randint(1, MAXQ)
print(q)
for _ in range(q):
    op = choice("?=")
    if op == "?":
        print(op)
    else:
        print(op, randrange(n), randint(0, MAXV))
