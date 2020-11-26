#!/usr/bin/env python3
# 4.1, шаг 10

fs = []
for i in range(1, 10):
    def f(x):
        return x + i
    fs.append(f)

# i = 9
print(fs[0](100))
print(fs[1](100))
i = 1000000
print(fs[4](100))

fs = []
for i in range(1, 10):
    def create_f(arg):
        def f(x):
            return x + arg
        return f
    fs.append(create_f(i))

print(fs)
print(fs[0](100))
print(fs[1](100))
print(fs[4](100))
