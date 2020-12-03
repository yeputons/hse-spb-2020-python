#!/usr/bin/env python3
import datetime


def timed(f, *args, **kwargs):
    start = datetime.datetime.now()
    f(*args, **kwargs)
    print(
        f.__name__ + "(" + ", ".join(map(str,
            list(args) + [f"{key}={value}" for key, value in kwargs.items()]
        )) + "): ",
        datetime.datetime.now() - start
    )


def foo1(n):
    """
    This is foo1.
    
    It creates a list of length 10 ** 6.
    """
    assert n == 10 ** 6
    [x ** 2 for x in range(10 ** 6)]


def foo2():
    l = []
    for x in range(10 ** 6):
        l.append(x ** 2)


def bar1():
    l = [100 for _ in range(10 ** 6)]
    l.insert(0, 20)  # [20, 100]
    l.append(50)  # [20, 100, 50]


def bar2():
    l = [100 for _ in range(10 ** 6)]
    l = [20] + l + [50]


foo1(10 ** 6)
timed(foo1, 10 ** 6)
timed(foo2)
timed(bar1)
timed(bar2)
