#!/usr/bin/env python3

import itertools
import math


def number(digits: list):
    result = 0
    pow = 1
    for d in reversed(digits):
        result += d * pow
        pow = pow * 10
    return result


# Newton's method works perfectly well on integers:
def isqrt(n):
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


for i in range(1, 10):
    print(i)
    for perm in list(itertools.permutations(range(1, i + 1))):
        n = number(list(perm))
        isq = isqrt(n)
        if isq ** 2 == n:
            print("\t" + str(n) + "\t=" + str(isq) + "*" + str(isq))

