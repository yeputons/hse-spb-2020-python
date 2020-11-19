# std::tie
x, y = [10, 20]
print(x, y)

x, y = y, x
print(x, y)

lst = [10, 20, 30]
lst2 = lst
lst.append(40)
lst2 += [100]
print(lst)
print(lst2)

x = 10 ** 100
y = x
x += 1
print(x, y)
