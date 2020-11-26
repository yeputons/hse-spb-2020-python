#!/usr/bin/env python
from typing import List


class HasDist2:
    def dist2(self):
        pass

    def dist(self):
        return self.dist2() ** 0.5


class Foo(HasDist2):  # Foo наследуется от HasDist2
    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y

    def __str__(self):
        return f'Foo({self.x}, {self.y})'

    def dist2(self):
        #assert isinstance(self, Foo)
        return self.x ** 2 + self.y ** 2


class Bar(HasDist2):
    def __init__(self, x=None, y=None):
        self.x = -1
        self.y = -1
        self.xx = x
        self.yy = y

    def __str__(self):
        return f'Bar({self.xx}, {self.yy})'

    def dist2(self):
        return self.xx ** 2 + self.yy ** 2


l: List[HasDist2] = [Foo(10, 20), Bar(30, 40)]
print(l[0].dist2())
print(l[1].dist2())
print(l[0].dist())
print(l[0].x)  # typing fail.
