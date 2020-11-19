def func(*args, **kwargs):  # func(*a, **b)
    print(args, kwargs)

func(1, 2, 3, c=4, d=5)

def foo(a, b, c=4, d=5, e=6, f=7, *args, **kwargs):
    print(a, b, c, d, e, f, args, kwargs)
foo(10, 15, 20, f=21, x=50)
foo(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, y=100)

def bar(a, b, *args, c, d=5, e=6, f=7, **kwargs):
    print(a, b, c, d, e, f, args, kwargs)
bar(10, 15, 20, c=4, f=21, x=50)

def baz(a, b, *, c, d=5, e=6, f=7, **kwargs):
    print(a, b, c, d, e, f, kwargs)
# baz(10, 15, 20)
baz(10, 15, c=20)
