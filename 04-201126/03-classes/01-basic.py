#!/usr/bin/env python3

class Foo:
    static_x = []  # CAREFUL: static
    THIS_IS_CONST = 10

    def __init__(self, *, x=None, y=None):  # Python's self ~~ C++'s *this
        self.x = x or 100
        self.y = y or 200

    def to_string(self):
        return f'Foo(x={self.x}, y={self.y})'

    def __str__(self):
        return self.to_string()


a = Foo()
b = Foo(x=1, y=2)

a.static_x = 30
Foo.static_x = 20
print(Foo.static_x, a.static_x, b.static_x)

a.foobarbaz = 100500
print(a.foobarbaz)
#print(b.foobarbaz)

Foo.THIS_IS_CONST = 30  # Please don't do that.

print(a.to_string())
print(str(a))
print(a)
