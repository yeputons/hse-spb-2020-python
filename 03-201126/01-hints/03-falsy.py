#!/usr/bin/env python3

if 2 * 2:
    print("YES")
else:
    print("NO")

# Также: while, bool(....)

assert not 0
assert not 0.0
assert not None
assert not []
assert not {}
assert not ""
assert not set()
assert not False

assert 0.01
assert 1
assert [1]
assert " "
assert True
assert [0]
assert [None]

l = [1, 2, 3]
# Bad python
if len(l) == 0:
    print("oops")
# Good python
if not l:
    print("oops")

# PEP 8
# flake8 - static analysis
