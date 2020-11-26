#!/usr/bin/env python3
assert 1 in set([1, 2, 3])
assert not (10 in set([1, 2, 3]))  # Worse
assert 10 not in set([1, 2, 3])  # Better

assert "key" in {"key": 10, "key2": 20}
assert "key3" not in {"key": 10, "key2": 20}

assert "needle" in "haystack-haystack-needle-haystack"
assert "иголка" not in "haystack-haystack-needle-haystack"

assert "a" in "hello a botva" in "wtf hello a botva wtf" <= "z" == "z" > "a"
