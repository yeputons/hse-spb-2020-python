#!/usr/bin/env python
import inspect

#@typing
def foo(a: int, b: int) -> int:
    return a + b

x: int = 10
y: str = 'ystr'
print(foo(x, x))
print(y * x)

s = inspect.signature(foo)
print(s)
print(s.return_annotation)
print(int)
print(s.parameters["a"].annotation)

#y = 50
print(foo("a", "b"))
