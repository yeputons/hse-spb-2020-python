#!/usr/bin/env python3

# 4.1, шаг 3.

try:
    n = int('10f')
    print(n * 2)
except ValueError as e:
    print('oops ' + str(e))

try:
    n = int('10f')
    print(n * 2)
except ValueError:
    print('oops')

try:
    n = int('10')
except ValueError:
    print('oops')
else:
    print(n * 2)

with open("file.txt", "w") as f:  # try-with-resources: try (FileWriter fw = new FileWriter(...)) { ... }
    f.write("hello")
    raise ValueError("oops")
