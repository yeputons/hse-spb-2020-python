#!/usr/bin/env python
import numpy as np
import time

def timed(f, *args, **kwargs):
    min_time = float('inf')
    for _ in range(3):
        start = time.perf_counter()
        f(*args, **kwargs)
        end = time.perf_counter()
        min_time = min(min_time, end - start)
    print(min_time)

N = int(1e7)
a = [i ** 2 for i in range(N)]
b = [i ** 3 for i in range(N)]

def sum1(a, b):
    return [x + y for x, y in zip(a, b)]

a_np = np.array(a)
b_np = np.array(b)

def sum2(a, b):
    return a + b

timed(sum1, a, b)
timed(sum2, a_np, b_np)
