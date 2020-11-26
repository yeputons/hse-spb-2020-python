#!/usr/bin/env python3
assert -5 <= -3 <= -1
assert (-5 <= -3) and (-3 <= -1)
#(-5 <= -3) <= -1
#False <= -1
#0 <= -1

# Плохо читается, зато весело.
assert -3 <= -2 == -2 <= 10 >= 5
assert (-3 <= -2) and (-2 == -2) and (-2 <= 10) and (10 >= 5)

n = 3
if 1 <= n <= 5:
    print("hurray")
