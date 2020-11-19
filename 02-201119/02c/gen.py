#!/usr/bin/env python3
from random import *

n = int(1e5)
l = list(range(1, n + 1))
shuffle(l)

print(n)
#print(' '.join(map(str, l)))
print(*l)
