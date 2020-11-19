import itertools

def nats():
    i = 1
    while True:
        yield i
        i += 1

n = nats()
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(next(n))
print(list(itertools.islice(n, 10)))
print(next(n))

def fibs():
    print("a")
    a, b = 0, 1
    while True:
        print("b")
        yield a
        print("c")
        a, b = b, a + b


#print(list(itertools.islice(fibs(), 20)))
n = fibs()
print(next(n))
print(next(n))

def map(f, l):
    for elem in l:
        yield f(elem)
