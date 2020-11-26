#!/usr/bin/env python3
from collections import defaultdict

d = {}
try:
    d["key"] += 1
except KeyError:
    print("oops :(")
print(d)

# C++:
#   map<string, int> d;
#   d["key"] += 1;
#   assert(d["key"] == 1);

d = {}
if "key" not in d:
    d["key"] = int()
d["key"] += 1
print(d)

print(int())  # 0
d = defaultdict(int)
d["key"] += 1
print(d)

d = defaultdict(lambda: 100)
d["key"] += 1
print(d)
