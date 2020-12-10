#!/usr/bin/env python
import inspect

def foo(a=42, *, c=90, b=30):
    print(a, b, c)

foo()
foo(45)
foo(a=45)
foo(45, b=40)

# foo(45, a=45)
# foo(45, 40)

foo(b=40, a=45)
foo(b=40)

# foo(b=40, 45)

def bar(x, y=10):
    print(x, y)

bar(100)
bar(x=100)
bar(100, 200)
bar(100, y=200)
bar(x=100, y=200)
bar(y=200, x=100)

s = inspect.signature(foo)
args = s.bind(b=40, a=45)
args.apply_defaults()
print(args)
print(args.arguments)
print(args.args, args.kwargs)
