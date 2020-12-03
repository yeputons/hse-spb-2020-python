#!/usr/bin/env python

def my_decorator(n):
    def impl(f):
        def decorated_f():
            print(n, f.__name__)
            return f()
        decorated_f.__name__ = f.__name__
        return decorated_f
    return impl


@my_decorator(20)
@my_decorator(10)  # foo = my_decorator(20)( my_decorator(10)(foo) )
def foo():
    pass

print(foo.__name__)
foo()
