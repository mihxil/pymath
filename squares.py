#!/usr/bin/env python3

import itertools

def number(digits: list):
    result = 0
    pow = 1
    for d in reversed(digits):
        result += d * pow
        pow = pow * 10
    return result


def is_square(i):
    if i == 1:
        return True
    x = i // 2
    seen = {x}
    while x * x != i:
        x = (x + (i // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True


for i in range(1, 10):
    print(i)
    for perm in list(itertools.permutations(range(1, i + 1))):
        n = number(list(perm))
        if is_square(n):
            print("\t" + str(n))

