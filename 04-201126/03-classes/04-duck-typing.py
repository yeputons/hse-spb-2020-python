#!/usr/bin/env python3

class Foo:  # CamelCase
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Foo({self.x}, {self.y})'

    def dist2(self):
        #assert isinstance(self, Foo)
        return self.x ** 2 + self.y ** 2


class Bar:
    def __init__(self, x=None, y=None):
        self.x = -1
        self.y = -1
        self.xx = x
        self.yy = y

    def __str__(self):
        return f'Bar({self.xx}, {self.yy})'

    def dist2(self):
        return self.xx ** 2 + self.yy ** 2


print(globals()['Foo'])
l = [Foo(3, 4), Bar(10, 20)]
for p in l:
    print(p.dist2())
#             [](auto x) { return x.dist2(); }
print([         item.dist2()        for item item in l  ])
print([ (lambda x: x.dist2())(item) for item item in l  ])
print(list(map(lambda x: x.dist2(), l)))

# dict(), {} ~ unordered_map
# SortedDict?

Foo.dist2(l[0])
l[0].dist2()
Foo.dist2(l[1])
l[1].dist2()
print(list(map(Foo.dist2, l)))

# ABC, mypy
