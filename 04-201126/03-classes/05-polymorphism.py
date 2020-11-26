#!/usr/bin/env python3
def print_all(l):
    for x in l:
        print(x)

print_all([1, 2, 3])
print_all(["hi", "world"])
print_all({"key1": 10, "key2": 20})

if input() == "0":
    x = [1, 2, 3]
else:
    x = ["hi", "world"]
print_all(x)
