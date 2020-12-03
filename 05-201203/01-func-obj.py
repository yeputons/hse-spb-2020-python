#!/usr/bin/env python3

def foo(a, b):
    return a + b

print(foo(2, 3))

bar = foo
print(bar(10, 20))

foo.xxx = 123
print(foo.xxx)
print(bar.xxx)

def create_bar(a):
    def bar(b):
        return a + b
    return bar

x = create_bar(100)
print(x(400))  # 500
