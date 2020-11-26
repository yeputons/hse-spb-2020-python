#!/usr/bin/env python3

x, y = [1, 2]
print(x, y)

head, *tail = [1, 2, 3, 4, 5]
print(head, tail)

head, *tail = [1, 2]
print(head, tail)

a, *b, c, d = [1, 2, 3, 4, 5]
print(a, b, c, d)

# a, *b, c, *d, e = [1, 2, 3, 4, 5]
# print(a, b, c, d, e)

a, *b, c, d = [1, 2, 5]
print(a, b, c, d)

#a, *b, c, d = [1, 5]
#print(a, b, c, d)

for head, *tail in [[1, 2, 3], [4, 5]]:
    print("inside for:", head, tail)

a, _, _, b = [1, 2, 3, 4]
print(a, b)
print(_)  # '_' обычно означает "не надо использовать", но вообще это просто переменная
