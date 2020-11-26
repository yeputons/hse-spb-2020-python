#!/usr/bin/env python3
# 1. True and False - как обычно.
# 2. a and b - лениво. Не вычисляем правый операнд, если можем.
# 3. Возвращаем не True/False, а какой-то из операндов.

# a and b: (псевдокод)
#   if a { return b }
#   else { return a }
print("hello" and "world")
print("hello" and 0)
print("hello" and None)

def foo():
    print("foo()")
    assert False

print(0 and foo())
print(None and foo())

def bar(x):
    if x == 2:
        return "hello"
    print("bar()")
    return  # == return None
    # return None
print(bar(10))

print("===== or =====")
# a or b: (псевдокод)
#   if a { return a
#   else { return b }
print("hello" or "world")
print(0 or "world")
print(None or "world")
print(None or 0)
print(None or 0.0)


if False and foo():  # short-circuit, like in C++
    print("if")


def baz(x=None):
    x = x or []
    print(x)
