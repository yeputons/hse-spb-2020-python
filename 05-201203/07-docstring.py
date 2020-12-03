#!/usr/bin/env python3
import datetime


def foo1(n):
    """
    This is the 'docstring' for foo1 (string literal in the very beginning).
    
    foo1(n) creates a list of length 10 ** 6.
    """
    assert n == 10 ** 6
    [x ** 2 for x in range(10 ** 6)]

print(repr(foo1.__doc__))
help(foo1)
