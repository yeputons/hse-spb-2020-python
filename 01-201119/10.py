#!/usr/bin/env python3
print(list(map(lambda x: x + 2, [1, 2, 3, 4])))
f = lambda x, y: x + y
print(f(10, 20))


def foo():
    for i in range(10):
        def map_operation(x):
            print(x)
            return x + i
        print(list(map(map_operation, [1, 2, 3, 4])))  # 'for' is better here.

foo()
