#!/usr/bin/env python3
import datetime


def wraps(old_f):
    def impl(new_f):
        new_f.__name__ = old_f.__name__
        new_f.__doc__ = old_f.__doc__
        return new_f
    return impl


def create_timed(f):
    @wraps(f)
    def timed_f(*args, **kwargs):  # timed_f = wraps(f)(timed_f)
        start = datetime.datetime.now()
        res = f(*args, **kwargs)
        print(datetime.datetime.now() - start)
        return res
    # timed_f.__name__ = f.__name__
    # timed_f.__doc__ = f.__doc__
    return timed_f


@create_timed  # foo1 = create_timed(foo1)
def foo1(n):
    "This is foo1!"
    assert n == 10 ** 6
    [x ** 2 for x in range(10 ** 6)]


foo1(10 ** 6)
print(foo1.__name__)
help(foo1)
