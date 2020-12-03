#!/usr/bin/env python3
import functools


def memorization(f):
    f.cache = {}
    @functools.wraps(f)
    def wrapped(*args):
        if args not in f.cache:
            f.cache[args] = f(*args)
        return f.cache[args]
    return wrapped


#@functools.lru_cache
@memorization
def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)


print(fib(100))
print(fib.cache)
