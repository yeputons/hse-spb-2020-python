#!/usr/bin/env python3
print(2 + 2, 2 ** 3, 2 / 3, 2 // 3)
print(-2 % 3, 2 % -3, -2 % -3)
print(0.5 + 0.25)

print('hello world')
print("hello world")
print('hello \'world\'\nwow\n')

print('hello ' + str(12))
print(int('10') + 5)

a = [10, 20, 30]
a = 123
b = 456
print(a + b)
# print("10" + 10)
print(globals()["a"])
globals()["a" + str(5 + 5)] = 239
print(a10)

lst = [10, "hello", [1, [3, 4]]]
# lst.sort()
print(lst, lst[0], lst[2], len(lst))

t = (1, 2, 3)  # pair/tuple
t = 4, 5, 6
print(t, t[0], len(t))
t = (4,)
print(t, t[0], len(t))
