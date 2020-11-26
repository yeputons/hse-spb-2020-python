#!/usr/bin/env python3

class Foo:
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Foo({self.x}, {self.y})'

    def foo(self):
        print("fooed")

    def dist2(self):
        return self.x ** 2 + self.y ** 2


a = Foo()
print(vars(a))
vars(a)["x"] = 10
print(a.x)

vars(a)["z"] = 10
print(vars(a))
print(a.z)

a.foo()
print(a.foo)  # Bound method
print(Foo.foo)  # Unbound method
Foo.foo(a)

print(list(map(Foo.dist2, [Foo(10, 20), Foo(3, 4)])))
