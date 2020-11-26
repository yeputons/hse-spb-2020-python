#!/usr/bin/env python3

class Node:
    def __init__(self, value):
        self.value = value
        self.prev = self.next = None

a = Node(10)
b = Node(20)

a.next = b
b.prev = a

print(a.value)
print(a.next.value)
