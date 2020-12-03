#!/usr/bin/env python3
import datetime


def create_timed(f):
    def timed_f(*args, **kwargs):
        start = datetime.datetime.now()
        res = f(*args, **kwargs)
        print(datetime.datetime.now() - start)
        return res
    return timed_f


def foo1(n):
    assert n == 10 ** 6
    [x ** 2 for x in range(10 ** 6)]
foo1 = create_timed(foo1)


foo1(10 ** 6)
