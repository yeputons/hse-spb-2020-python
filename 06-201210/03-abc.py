#!/usr/bin/env python3
from typing import List, TypeVar

def length(a: List) -> int:
    return len(a)

print(length([1, 2]))
print(length(['1', '2']))
# print(length('123'))
# print(length(123))

# template<typename T> vector<T> repeat(T a, int n);

T = TypeVar('T')
def repeat(a: T, n: int) -> List[T]:
    return [a] * n

a: List[int] = repeat(10, 4)
b: List[str] = repeat(10, 4)
