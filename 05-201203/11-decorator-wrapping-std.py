#!/usr/bin/env python3
import datetime
import functools


def create_timed(f):
    @functools.wraps(f)
    def timed_f(*args, **kwargs):  # timed_f = functools.wraps(f)(timed_f)
        start = datetime.datetime.now()
        res = f(*args, **kwargs)
        print(datetime.datetime.now() - start)
        return res
    return timed_f


@create_timed  # foo1 = create_timed(foo1)
def foo1(n):
    "This is foo1!"
    assert n == 10 ** 6
    [x ** 2 for x in range(10 ** 6)]


foo1(10 ** 6)
print(foo1.__name__)
help(foo1)
